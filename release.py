
import PySide
import os
from os import path
import subprocess

ps_dir = path.dirname(PySide.__file__)

ps_lupdate = path.join(ps_dir, "pyside-lupdate.exe")

ps_lconvert = path.join(ps_dir, "lconvert.exe")
ps_lrelease = path.join(ps_dir, "lrelease.exe")

files = os.listdir("i18n")
langs = [ts[:-3] for ts in files if ts.endswith(".ts")]

if not path.exists("build"):
    os.mkdir("build")

for lang in langs:
    subprocess.check_call([ps_lrelease, "i18n/%s.ts" % lang, "-qm",
                           "build/%s.qm" % lang])
