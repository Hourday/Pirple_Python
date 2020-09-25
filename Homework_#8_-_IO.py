import os.path
from os import path
import enum

# filename=input("enter filename:" )
#
# try:
#     var= open(str(filename),"r")
# except IOError:
#     #file doesnt exist
#
#     print("enter the text in your file: ")
#     for x in range(5):
#         var.write(x)
#     var.close()
# def read():
#     for x in range(5):
#         y=var.read(x)
#         print(y)
#         var.close()
# def del():
#     var=open(str(filename),"w")
#     var.close()
# def app():
#     final=input("enter the text you want to add: ")
#     var= open(str(filename),"a")
#     var.write(final)
#     var.close()
# def switcher()

class COMMAND(enum.Enum):
   READ = 1
   DELETE = 2
   APPEND = 3

def doesfileexist (filename):
    return path.exists(filename)

def readfilewithname(filename) :
    print("Read file with name ", filename)
    f = open(filename, "r")
    print(f.read())

def deletefilewithname(filename) :
    print("Delete file with name ", filename)
    if doesfileexist(filename):
        os.remove(filename)
        print("The file has been deleted");
    else:
        print("The file does not exist anymore")

def appendtofilewithname(filename):
    print("Append to file with name ", filename)
    content = input("What do you wish to append to the file? ")
    f = open(filename, "a")
    f.write(content)
    f.close()

def createfilewithname (filename):
    try:
        print("Create file with name", filename)
        content = input("What do you wish to write in the file?")
        f = open(filename, "w")
        f.write(content)
    except Exception as e:
        print("Unable to create file with name: ", filename)
    finally:
        f.close()

def throwexception(filename):
    error = "Sorry, wrong command entered for processing file with name " + filename
    raise Exception(error)

def updateFileModificationTime():
    print("this should not have run on wrong input");

def processfilewithcommand(filename, commandnumber):
    commandswitcher = {
        COMMAND.READ.value:readfilewithname,
        COMMAND.DELETE.value:deletefilewithname,
        COMMAND.APPEND.value:appendtofilewithname,
    }
    func = commandswitcher.get(commandnumber, throwexception);
    func(filename)
    # updateFileModificationTime()

def readandprocesscommandforfile(filename):
    try:
        command = input("Enter command number to process the file, READ (1) | DELETE (2) | APPEND (3):")
        processfilewithcommand(filename, int(command))
    except Exception as e:
        print("Unable to process the file: " + str(e))

def main ():
    filename = input("Enter name of file to process:")
    if not doesfileexist(filename):
        createfilewithname(filename)
    else:
        readandprocesscommandforfile(filename)
main()