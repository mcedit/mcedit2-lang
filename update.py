
import PySide
import os
from os import path
import subprocess

ps_dir = path.dirname(PySide.__file__)

ps_lupdate = path.join(ps_dir, "pyside-lupdate.exe")

ps_lconvert = path.join(ps_dir, "lconvert.exe")

git_repo = "https://github.com/mcedit2/mcedit2"

subprocess.check_call(['git', 'clone', '--depth=1', git_repo])

m2_dir = path.join(path.dirname(__file__), 'mcedit2', 'src', 'mcedit2')

pyfiles = []
uifiles = []

for parent, dirs, files in os.walk(m2_dir):
    if "ui" not in parent:
        for fn in files:
            if fn.endswith(".py"):
                pyfiles.append(path.join(parent, fn))
    else:
        for fn in files:
            if fn.endswith(".ui"):
                uifiles.append(path.join(parent, fn))

proj = open("mcedit2_lupdate.pro", "w")

proj.write("SOURCES = \\\n")

for pf in pyfiles:
    proj.write(pf + " \\\n")

proj.write("\nFORMS = \\\n")

for uf in uifiles:
    proj.write(uf + " \\\n")
    
proj.write("\nTRANSLATIONS = \\\n")

tsfiles = []

for l in ['en', 'jp', 'cn', 'es', 'fr']:
    f = "i18n/%s.ts" % l
    tsfiles.append(f)
    proj.write(f + "\\\n")
    
proj.close()

subprocess.check_call([ps_lupdate, "mcedit2_lupdate.pro"])

for ts in tsfiles:
    po = ts.replace(".ts", ".po")
    subprocess.check_call([ps_lconvert, ts, "-of", "po", "-o", po])

os.remove("mcedit2_lupdate.pro")
