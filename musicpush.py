import re
import os
import subprocess as sp

adb = "/android-sdk/platform-tools/adb"
src = "/Multimedia/My music/"
dest = "/sdcard/Music"

# doesn't explore recursively for now
for f in os.listdir(src):
    full = src + "/" + f
    if os.path.isfile(full) and len(re.findall("\.mp3|\.wma", f)) > 0:
        cmd = adb + " push '" + full + "' '" + dest + "'"
        print "Pushing " + cmd
        sp.check_output(cmd, shell=True)
