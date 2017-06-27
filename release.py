
import PySide
import os
from os import path
import subprocess

ps_dir = path.dirname(PySide.__file__)

def get_pstool(name):
    pth = subprocess.check_output(["which", name])
    if pth: return pth

    pth = path.join(ps_dir, name)
    if os.name == "nt":
        pth += ".exe"

    return pth

ps_lupdate = get_pstool("pyside-lupdate")
ps_lconvert = get_pstool("lconvert")
ps_lrelease = get_pstool("lrelease")

langdir = path.dirname(__file__)
i18n = path.join(langdir, "i18n")
build = path.join(langdir, "build")

files = os.listdir(i18n)
langs = [ts[:-3] for ts in files if ts.endswith(".ts")]

if not path.exists(build):
    os.mkdir(build)

for lang in langs:
    subprocess.check_call([ps_lrelease, i18n + "/%s.ts" % lang, "-qm",
                           build + "/%s.qm" % lang])

subprocess.check_call([ps_lrelease, langdir + "/en.ts", "-qm",
                       build + "/en.qm"])
