def readFile(fileName):
    fileHandle = open(fileName, mode='rt')
    print(fileHandle.read())
    fileHandle.close()


f = open("test.txt", mode='a')
f.write("this line is at end of file")
f.close()

# read file
readFile("test.txt")
# overwrite the content

f = open("test.txt", mode='w')
f.write("New Content")
f.close()

readFile("test.txt")

import os


def createFile(fileName):
    # check if file exits.
    if os.path.exists(fileName):
        os.remove(fileName)

    f = open(fileName, mode='x')  # will error if file exits.
    f.close()


# Create a file called "myfile.txt":
createFile("myfile.txt")


def createFileIfNotExits(fileName):
    f = open(fileName, "w")
    f.close()


createFileIfNotExits("myfile1.txt")
createFileIfNotExits("myfile2.txt")


def createFolder(folderName):
    os.mkdir(folderName)


# remove folder
createFolder("myfolder")
os.removedirs("myfolder")
createFolder("myfolder")
os.rmdir("myfolder")
createFolder("myfolder1")
createFileIfNotExits('myfolder1//kaka.txt')
os.rmdir("myfolder1")
