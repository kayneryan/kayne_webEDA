#Kayne Ryan
#unzip multiple files

import os, zipfile, sys


def unzip (folder):
    os.chdir(folder)

    for file in os.listdir(folder):   # get the list of files
        if zipfile.is_zipfile(file): # if it is a zipfile, extract it
            with zipfile.ZipFile(file) as item: # treat the file as a zip
                item.extractall()  # extract it in the working directory


if __name__ == "__main__":
    unzip(sys.argv[1])