import sqlite3
import re
from typing import Dict

import requests
from requests.utils import requote_uri

DATABASE_FILE = "plugins.db"
#TROVE_CLASSIFIER = "Framework :: pycsou"
TROVE_CLASSIFIER = "Framework :: AiiDA"


def query_pypi() -> Dict[str, str]:
    """
    Query pypi to get all plugins.
    :return: all plugin names and latest version
    """
    packages = {}
    page = 1
    name_pattern = re.compile('class="package-snippet__name">(.+)</span>')
    version_pattern = re.compile(
        'class="package-snippet__version">(.+)</span>')
    url = requote_uri(f"https://pypi.org/search/?q=&o=-created&c={TROVE_CLASSIFIER}")
    response = requests.get(f'{url}')
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
    html = response.text
    names = name_pattern.findall(html)
    versions = version_pattern.findall(html)
    if len(names) != len(versions):
        return {}
    for name, version in zip(names, versions):
        packages[name] = version
    page += 1
    return packages

def main():
    # Connect to the database
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()

    # Create the plugins table
    c.execute('''CREATE TABLE IF NOT EXISTS plugins
                 (name text, pycsou_version text, version text, author text, author_email text, docs_url text, home_page text, short_description text, description text, license text, development_status text, entrypoints text)''')

    # Query the PyPI API for plugins of the Pycsou framework
    plugin_names = query_pypi()

    # Extract metadata from each plugin's configuration file and store it in the database
    for plugin_name in plugin_names:
        url = f"https://pypi.org/pypi/{plugin_name}/json"
        response = requests.get(url)
        plugin_data = response.json()

        name = plugin_data["info"]["name"]
        pycsou_version = "2"
        version = plugin_data["info"]["version"]
        author = plugin_data["info"]["author"]
        author_email = plugin_data["info"]["author_email"]
        docs_url = plugin_data["info"]["docs_url"]
        home_page = plugin_data["info"]["home_page"]
        short_description = "Not Available"
        description = plugin_data["info"]["description"]
        license = plugin_data["info"]["license"]
        development_status = plugin_data["info"].get("development_status", "planning")
        entrypoints = None

        c.execute("INSERT INTO plugins VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, pycsou_version, version, author, author_email, docs_url, home_page, short_description, description, license, development_status, entrypoints))

    # Commit changes to the database and close the connection
    conn.commit()
    conn.close()

main()