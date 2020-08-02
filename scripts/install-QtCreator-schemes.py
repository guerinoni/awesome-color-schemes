import os
import requests
from sys import platform
from shutil import copyfile
from pathlib import Path


def schemeDir():
    dir = ""
    if platform == "linux" or platform == "linux2":
        dir = str(Path.home()) + "/.config/QtProject/qtcreator/styles/"
    if platform == "darwin":
        dir = str(Path.home()) + "/.config/QtProject/QtCreator/styles/"
    if platform == "win32":
        dir = "C:\Qt\Tools\QtCreator\share\qtcreator\styles\\"

    return dir;


def copy(filename):
    copyfile(filename, schemeDir() + os.path.basename(filename))


def download(filename):
    link = ""
    with open(filename) as f:
        link = f.readline()
    
    file = requests.get(link)
    open(schemeDir() + os.path.basename(filename) + ".xml", 'wb').write(file.content)


def install(filename):
    if filename.endswith(".xml"):
        copy(filename)
    else:
        download(filename)


def checkStylesDir():
    if not os.path.exists(schemeDir()):
        print("styles not exists")
        os.mkdir(schemeDir())


def main():
    print("installing QtCreator color schemes...")
    checkStylesDir()
    QtCreatorPath = "./QtCreator/"
    (_, _, filenames) = next(os.walk(QtCreatorPath))    
    for item in filenames:
        install(QtCreatorPath + item)

    print("install finished")


if __name__ == "__main__":
    main()
