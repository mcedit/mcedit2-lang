
import PySide
import os
from os import path
import subprocess

ps_dir = path.dirname(PySide.__file__)

ps_lupdate = path.join(ps_dir, "pyside-lupdate.exe")

ps_lconvert = path.join(ps_dir, "lconvert.exe")

git_repo = "https://github.com/mcedit/mcedit2"

if not path.exists("mcedit2"):
  subprocess.check_call(['git', 'clone', '--depth=1', git_repo])
else:
  subprocess.check_call(['git', 'pull'], cwd="mcedit2")

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

files = os.listdir("i18n")
langs = [ts[:-3] for ts in files if ts.endswith(".ts")]
tsfiles = ["i18n/" + ts for ts in files if ts.endswith(".ts")]
tsfiles.append("en.ts")

for f in tsfiles:
    proj.write(f + "\\\n")
    
proj.close()

subprocess.check_call([ps_lupdate, "mcedit2_lupdate.pro"])

os.remove("mcedit2_lupdate.pro")
