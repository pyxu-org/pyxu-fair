import os
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader
import sqlite3

# from . import status_dict, entrypoint_metainfo

entrypoint_metainfo = {

    "pycsou.map": {
        "shortname": "Map",
        "longname": "Map operators, such as Map and DiffMap",
        "colorclass": "blue",
    },
    "pycsou.func": {
        "shortname": "Func",
        "longname": "Functional operators, such as Func, DiffFunc, ProxFunc, LinFunc and QuadraticFunc",
        "colorclass": "blue",
    },
    "pycsou.operator": {
        "shortname": "LinOp",
        "longname": "Linear operators such as LinOp, SquareOp, NormalOp, SelfAdjointOp, UnitOp, ProjOp, OrthProjOp and PosDefOp ",
        "colorclass": "blue",
    },
    "pycsou.solver": {
        "shortname": "Solvers",
        "longname": "Optimization algorithms",
        "colorclass": "brown",
    },
    "pycsou.stop": {
        "shortname": "Stop",
        "longname": "Stopping criteria for optimization algorithms",
        "colorclass": "red",
    },
    "pycsou.math": {
        "shortname": "Math",
        "longname": "Mathematical utility functions and classes",
        "colorclass": "yellow",
    },
    "pycsou.data": {
        "shortname": "Data",
        "longname": "Data loading/downloading/creation/simulation/splitting utility functions and classes",
        "colorclass": "red",
    },
    "pycsou.io": {
        "shortname": "I/O",
        "longname": "Data reading/saving utility functions and classes",
        "colorclass": "red",
    },
    "pycsou.pipeline": {
        "shortname": "Pipelines",
        "longname": "Optimization workflows",
        "colorclass": "green",
    },
}
# User-facing description of plugin development status
status_dict = {
    "planning": [
        "Not yet ready to use. Developers welcome!",
        "status-planning-d9644d.svg",
    ],
    "pre-alpha": [
        "Not yet ready to use. Developers welcome!",
        "status-planning-d9644d.svg",
    ],
    "alpha": [
        "Adds new functionality, not yet ready for production. Testing welcome!",
        "status-alpha-d6af23.svg",
    ],
    "beta": [
        "Adds new functionality, not yet ready for production. Testing welcome!",
        "status-beta-d6af23.svg",
    ],
    "stable": [
        "Ready for production calculations. Bug reports welcome!",
        "status-stable-4cc61e.svg",
    ],
    "mature": [
        "Ready for production calculations. Bug reports welcome!",
        "status-stable-4cc61e.svg",
    ],
    "inactive": [
        "No longer maintained.",
        "status-inactive-bbbbbb.svg",
    ],
}


entrypoints_count = defaultdict(list)

def get_summary_info(entry_points):
    """Get info for plugin detail page.

    Note: this updates the global variables entrypoints_count and other_entrypoint_names.
    """
    summary_info = []
    ep = (entry_points or {}).copy()

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
            # No pycsou-specific entrypoints, pass
            pass

    return summary_info


# Load the Jinja2 catalogue_template
env = Environment(loader=FileSystemLoader('.'))
catalogue_template = env.get_template(os.path.join("templates", "catalogue.html"))
plugin_template = env.get_template(os.path.join("templates", "plugin.html"))

# Connect to the SQLite database and retrieve the plugins
conn = sqlite3.connect('plugins.db')
c = conn.cursor()
c.execute("SELECT name, pycsou_version, version, author, author_email, docs_url, home_page, short_description, description, license, development_status, entrypoints FROM plugins")
plugins = []
for row in c.fetchall():
    plugins.append({
        'name': row[0],
        'pycsou_version': row[1],
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
        # 'score': row[12]
    })
conn.close()

plugins_info = {"summary_info": {}, "dev_status": {}}
# Render the plugin_template for each specific plugin data
for plugin in plugins:
    summary_info = get_summary_info(plugin["entrypoints"])
    dev_status = status_dict[plugin["development_status"]]
    plugins_info["summary_info"].update({plugin["name"]: summary_info})
    plugins_info["dev_status"].update({plugin["name"]: dev_status})
    html = plugin_template.render(plugin=plugin, summary_info=summary_info, dev_status=dev_status)
    with open(f'html/plugins/{plugin["name"]}.html', 'w') as f:
        f.write(html)


# Render the catalogue_template with the data for all the plugins
html = catalogue_template.render(plugins=plugins, summary_info=plugins_info["summary_info"],
                                 dev_status=plugins_info["dev_status"])

# Write the HTML to a file
with open('html/index.html', 'w') as f:
    f.write(html)
