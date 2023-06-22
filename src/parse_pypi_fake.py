from pathlib import Path
import json
import sqlite3
import random
import names
import lorem
from wonderwords import RandomWord

DATABASE_FILE = "plugins.db"
rows = ['name', 'pycsou_version', 'version', 'author', 'author_email', 'docs_url', 'home_page', 'short_description', 'description', 'license', 'development_status', 'entrypoints']

n_entries = 10

devstat = [
    "Development Status :: 1 - Planning",
    "Development Status :: 2 - Pre-Alpha",
    "Development Status :: 3 - Alpha",
    "Development Status :: 4 - Beta",
    "Development Status :: 5 - Production/Stable",
    "Development Status :: 6 - Mature",
    "Development Status :: 7 - Inactive"
]
eps = [
    "operator",
    "solver",
    "stop",
    "math",
    "contrib",
]

r = RandomWord()
adjective = lambda: r.word(include_parts_of_speech=["adjectives"], word_max_length=6)


plugin_list = [
    ("pycNUFFT", "Scalable and distributed implementation non-uniform FFT for Pycsou"),
     ("PYFW", "Polyatomic Frank-Wolfe for the LASSO problem"),
     ("pycWavelet", "Optimized and accurate wavelet transforms for Pycsou"),
     ("Palentologist", "Toolset for single-cell track analysis in Python"),
     ("TokemakRec", "Plasma imaging for tokemak data"),
     ("OrientationPy", "Analysis of greyscale orientations from 2D or 3D image"),
     ("WaveProp", "Wave propagation reconstruction"),
     ("HoughDetector", "A plugin for napari that detects circles using the Hough transform"),
     ("CSEEG", "Compressed Sensing for EEG reconstruction"),
     ("PhaseRet", "Phase retrieval"),
     ("PycGSP", "Inverse problems on graphs"),
     ("TVDenoiser", "Total variation image denoising plugin for Napari"),
     ("PycSphere", "Inverse problems on the sphere"),
     ("DSP-Notebooks", "Jupyter notebooks for teaching advances concepts in digital signal processing with Pycsou"),
     ("HVOX", "RadioAstronomy gridder based on the Heisenberg voxelisation"),
     ("UncertaintyQuant", "Computational Uncertainty Quantification for Inverse Problems in Python"),
     ("EnvironTracker", "A plugin to image environmental signals"),
]

def main():
    Path.unlink(DATABASE_FILE)
    # Connect to the database
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()

    # Create the plugins table
    c.execute('''CREATE TABLE IF NOT EXISTS plugins
                 (name text, pycsou_version text, version text, author text, author_email text, docs_url text, home_page text, short_description text, description text, license text, development_status text, entrypoints text)''')

    for plugin in plugin_list:
        name = plugin[0]
        pycsou_version = "2.0.0"
        version = "0.1.0"
        author = names.get_full_name()
        author_email = f"{author.lower().replace(' ', '.')}@pycsou_user.org"
        user_name = author.split()[0][0].lower() + author.split()[1].lower()
        docs_url = f"https://{user_name}.github.io/{name}/html/index"
        home_page = f"https://github.com/{user_name}/{name}"
        short_description = plugin[1]
        description = lorem.text()
        license = "MIT"
        development_status = random.choice(devstat)
        development_status = development_status.split("::")[1][1]
        n_eps = random.randint(1, 10)
        entrypoints = {}
        for _ in range(n_eps):
            ep_type = random.choice(eps)
            ep_name = "_".join([adjective(), ep_type])
            ep_key = 'pycsou.' + ep_type
            if entrypoints.get(ep_key):
                ep_dict = json.loads(
                    '{"' + ep_name + '": "' + name.replace('-', '_') + ":" + ep_name + '"}')
                entrypoints[ep_key].update(ep_dict)
            else:
                ep_dict = json.loads(
                    '{"' + ep_key + '": {"' + ep_name + '": "' + name.replace('-', '_') + ":" + ep_name + '"}}')
                entrypoints.update(ep_dict)
        entrypoints = json.dumps(entrypoints)
        c.execute("INSERT INTO plugins VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, pycsou_version, version, author, author_email, docs_url, home_page, short_description, description, license, development_status, entrypoints))

    # Commit changes to the database and close the connection
    conn.commit()
    conn.close()

main()