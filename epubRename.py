#

from sys        import argv
from os         import listdir
from epub       import open_epub

filelist = listdir(".")

if len(argv) > 1:
    for filename in filelist:
        if filename.endswith(".epub"):
            book = open_epub(filename, "r")
            print filename[:-5], ":", book.opf.metadata.titles[0][0]
            book.close()
else:
    for filename in filelist:
        if filename.endswith(".epub"):
            book = open_epub(filename, "a")
            book.opf.metadata.titles = [(filename[:-5].decode('utf8'), u"")]
            book.close()