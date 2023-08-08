import sqlite3
import re
from typing import Dict

import warnings
import requests
from requests.utils import requote_uri
import configparser
import tempfile
import zipfile
import json
from pathlib import Path

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

class CaseSensitiveConfigParser(configparser.ConfigParser):
    """Case sensitive config parser."""

    optionxform = staticmethod(str)

def parse_entrypoints(plugin_data, parse_wheel=True):
    # We cannot read 'entry_points' from PyPI JSON so must download the wheel file
    build_types = {}
    for data in plugin_data.get("urls"):
        if data.get("packagetype"):
            build_types[data.get("packagetype")] = data.get("url")
    if "bdist_wheel" not in build_types:
        warnings.warn("No bdist_wheel available for PyPI release")

    if not build_types.get("bdist_wheel") or not parse_wheel:
        return "{}"

    try:
        with requests.get(
                build_types["bdist_wheel"], stream=True, timeout=120
        ) as download:
            download.raise_for_status()
            with tempfile.TemporaryDirectory() as tmpdirname:
                with Path(tmpdirname, "wheel.whl").open("wb") as handle:
                    for chunk in download.iter_content(chunk_size=8192):
                        handle.write(chunk)
                with zipfile.ZipFile(Path(tmpdirname, "wheel.whl")) as whl:
                    # see https://packaging.python.org/en/latest/specifications/entry-points/#file-format
                    entry_points_content = None
                    for name in whl.namelist():
                        if name.endswith(".dist-info/entry_points.txt"):
                            entry_points_content = whl.read(name).decode("utf-8")
                    if entry_points_content is None:
                        raise IOError("No entry_points.txt found in wheel")
                    parser = CaseSensitiveConfigParser()
                    parser.read_string(entry_points_content)
                    entry_points = {}
                    for key, value in parser.items():
                        if key == "DEFAULT":
                            continue
                        entry_points[key] = dict(value.items())
    except Exception as err:  # pylint: disable=broad-except
        warnings.warn(f"Unable to read wheel file from PyPI release: {err}")
    return json.dumps(entry_points)

def main():
    # Connect to the database
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()

    # Create the plugins table
    c.execute('''CREATE TABLE IF NOT EXISTS plugins
                 (name text, pyxu_version text, version text, author text, author_email text, docs_url text, home_page text, short_description text, description text, license text, development_status text, entrypoints text)''')

    # Query the PyPI API for plugins of the Pyxu framework
    plugin_names = query_pypi()

    # Extract metadata from each plugin's configuration file and store it in the database
    for plugin_name in plugin_names:
        url = f"https://pypi.org/pypi/{plugin_name}/json"
        response = requests.get(url)
        plugin_data = response.json()

        name = plugin_data["info"]["name"]
        pyxu_version = "2"
        version = plugin_data["info"]["version"]
        author = plugin_data["info"]["author"]
        author_email = plugin_data["info"]["author_email"]
        docs_url = plugin_data["info"]["docs_url"]
        home_page = plugin_data["info"]["home_page"]
        short_description = "Not Available"
        description = plugin_data["info"]["description"]
        license = plugin_data["info"]["license"]
        development_status = plugin_data["info"].get("development_status", "planning")
        entrypoints = parse_entrypoints(plugin_data)

        c.execute("INSERT INTO plugins VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, pyxu_version, version, author, author_email, docs_url, home_page, short_description, description, license, development_status, entrypoints))

    # Commit changes to the database and close the connection
    conn.commit()
    conn.close()

main()