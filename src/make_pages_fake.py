import os
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader
import sqlite3
import json

entrypoint_metainfo = {

    "pyxu.operator": {
        "shortname": "Operator",
        "colorclass": "blue",
    },
    "pyxu.solver": {
        "shortname": "Solver",
        "colorclass": "brown",
    },
    "pyxu.stop": {
        "shortname": "Stop",
        "colorclass": "purple",
    },
    "pyxu.math": {
        "shortname": "Math",
        "colorclass": "green",
    },
    "pyxu.contrib": {
        "shortname": "Contrib",
        "colorclass": "orange",
    },
}
# User-facing description of plugin development status
status_dict = {
    "1": [
        "Planning: Not yet ready to use. Developers welcome!",
        "status-planning-d9644d.svg",
    ],
    "2": [
        "Pre-alpha: Not yet ready to use. Developers welcome!",
        "status-planning-d9644d.svg",
    ],
    "3": [
        "Alpha: Adds new functionality, not yet ready for production. Testing welcome!",
        "status-alpha-d6af23.svg",
    ],
    "4": [
        "Beta: Adds new functionality, not yet ready for production. Testing welcome!",
        "status-beta-d6af23.svg",
    ],
    "5": [
        "Production/Stable: Ready for production calculations. Bug reports welcome!",
        "status-stable-4cc61e.svg",
    ],
    "6": [
        "Mature: Ready for production calculations. Bug reports welcome!",
        "status-stable-4cc61e.svg",
    ],
    "7": [
        "Inactive: No longer maintained.",
        "status-inactive-bbbbbb.svg",
    ],
}


entrypoints_count = defaultdict(list)

def get_summary_info(entry_points):
    """Get info for plugin detail page.

    Note: this updates the global variables entrypoints_count and other_entrypoint_names.
    """
    summary_info = []
    ep = json.loads(entry_points)

    # Collect entry points
    for entrypoint_name in entrypoint_metainfo.keys():
        try:
            num = len(ep.pop(entrypoint_name))
            if num > 0:
                summary_info.append(
                    {
                        "colorclass": entrypoint_metainfo[entrypoint_name][
                            "colorclass"
                        ],
                        "text": entrypoint_metainfo[entrypoint_name]["shortname"],
                        "count": num,
                    }
                )
                entrypoints_count[entrypoint_name].append(num)
        except KeyError:
            # No pyxu-specific entrypoints, pass
            pass

    return summary_info


# Load the Jinja2 catalogue_template
env = Environment(loader=FileSystemLoader('.'))

# Connect to the SQLite database and retrieve the plugins
conn = sqlite3.connect('plugins_fake.db')
c = conn.cursor()
c.execute("SELECT name, pyxu_version, version, author, author_email, docs_url, home_page, short_description, description, license, development_status, entrypoints, score FROM plugins_fake ORDER BY name COLLATE NOCASE ASC")
plugins_fake = []
for row in c.fetchall():
    plugins_fake.append({
        'name': row[0],
        'pyxu_version': row[1],
        'version': row[2],
        'author': row[3],
        'author_email': row[4],
        'docs_url': row[5],
        'home_page': row[6],
        'short_description': row[7],
        'description': row[8],
        'license': row[9],
        'development_status': row[10],
        'entrypoints': row[11],
        'score': row[12],
    })
conn.close()

plugins_info = {
    "summary_info": {},
    "dev_status": {},
    "summary_info_count": {epm["shortname"]: {"colorclass": epm["colorclass"], "num_entries": 0, "name": epm["shortname"], "total_num": 0} for epm in entrypoint_metainfo.values()},
    "dev_status_count":   {k: {"badge": v[1], "num_entries": 0} for k, v in status_dict.items()}
}

if os.path.exists("rst/"):
    for f in os.listdir("rst/"):
        if not f.endswith(".rst"):
            continue
        os.remove(os.path.join("rst/", f))
else:
    os.mkdir("rst")

# Render the plugin_template for each specific plugin data
for plugin in plugins_fake:
    summary_info = get_summary_info(plugin["entrypoints"])
    dev_status = status_dict[plugin["development_status"]]
    plugins_info["summary_info"].update({plugin["name"]: summary_info})
    plugins_info["dev_status"].update({plugin["name"]: dev_status})
    for entry in summary_info:
        plugins_info["summary_info_count"][entry["text"]]["num_entries"] += 1
        plugins_info["summary_info_count"][entry["text"]]["total_num"] += entry["count"]
    plugins_info["dev_status_count"][plugin["development_status"]]["num_entries"] += 1
    entrypoints = json.loads(plugin["entrypoints"])

    rst_plugin_template = env.get_template(os.path.join("templates", "plugin.rst"))
    rst = rst_plugin_template.render(plugin=plugin,
                                  summary_info=summary_info,
                                  dev_status=dev_status,
                                  entry_points=entrypoints,
                                  entrypointtypes=entrypoint_metainfo)
    with open(f'../../pyxu/doc/fair/plugins_preview/{plugin["name"]}.rst', 'w') as f:
        f.write(rst)

# Render the catalogue_template with the data for all the plugins

rst_catalogue_template = env.get_template(os.path.join("templates", "catalogue.rst"))
rst = rst_catalogue_template.render(plugins=plugins_fake,
                                     summary_info=plugins_info["summary_info"],
                                     dev_status=plugins_info["dev_status"],
                                     dev_status_count=plugins_info["dev_status_count"],
                                     summary_info_count=plugins_info["summary_info_count"].values(),)

# Write the RST to a file
with open('../../../git/pyxu/doc/fair/plugins_preview/index.rst', 'w') as f:
    f.write(rst)