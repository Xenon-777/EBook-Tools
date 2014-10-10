#

from rarfile    import is_rarfile, RarFile
from os         import listdir
from os.path    import isdir
from subprocess import call

filelist = listdir(".")
filelist.sort()

for filename in filelist:
    if isdir(filename):
        continue
    print filename
    if filename.endswith(".rar"):
        try:
            call("unrar e -o- %s" % filename, shell=True)
        except:
            continue