import subprocess
import os

os.system('ls -l')
list_files = subprocess.run(["ls", "-l"])
print("The exit code was: %d" % list_files.returncode)