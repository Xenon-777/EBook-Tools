#

from os         import listdir, remove
from zipfile    import is_zipfile, ZipFile
from rarfile    import is_rarfile, RarFile
from Image      import open as iopen
from shutil     import rmtree, move
from os.path    import isdir

filelist = listdir(".")
filelist.sort()

print filelist

for filename in filelist:
    if isdir(filename):
        continue
    print filename
    if is_zipfile(filename):
        cbfilein = ZipFile(filename, "r")
    elif is_rarfile(filename):
        cbfilein = RarFile(filename, "r")
    else:
        print "File nicht erkannt"
        continue
    cbfileout = ZipFile(filename[0:-4] + ".cbz", "a")
    
    for picfile in cbfilein.namelist():
        cbfilein.extract(picfile)
        if picfile.rfind("\\") > -1:
            picfile = picfile.replace("\\","/")
        if isdir(picfile):
            rmtree(picfile)
            continue
        if picfile.rfind("/") > -1:
            if isdir(picfile):
                rmtree(picfile[:picfile.find("/")])
                continue
            else:
                move(picfile,picfile[picfile.rfind("/")+1:])
                rmtree(picfile[:picfile.find("/")])
                picfile = picfile[picfile.rfind("/")+1:]
        try:
            pic = iopen(picfile)
        except:
            remove(picfile)
            continue
        if pic.size[0] > pic.size[1]:
            pic = pic.rotate(270)
        try:
            pic.save(picfile)
            cbfileout.write(picfile)
        except:
            pass
        remove(picfile)
    cbfilein.close()
    cbfileout.close()