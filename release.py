
import PySide
import os
from os import path
import subprocess

ps_dir = path.dirname(PySide.__file__)

ps_lupdate = path.join(ps_dir, "pyside-lupdate.exe")

ps_lconvert = path.join(ps_dir, "lconvert.exe")
ps_lrelease = path.join(ps_dir, "lrelease.exe")

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
