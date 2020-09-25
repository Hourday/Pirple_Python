import os.path
from os import path
import enum

class COMMAND(enum.Enum):
    READ = 1
    DELETE = 2
    APPEND = 3
    REPLACE = 4

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
    while content != "":
        f.write(content)
        f.write("\n")
        content = input()
    f.close()

def readAllFileContentsAndReplaceWithStringAtLine (filename, linenumber):
    filecontent = []
    f = open(filename, "r")
    try:
        filelinenumber = 1
        for line in f:
            filecontent.append(line)
            filelinenumber += 1
        if linenumber > filelinenumber:
            raise Exception("Line number cannot be greater than the number of lines in the file")
    except Exception as e:
        print("Unable to read contents of file with name: ", filename)
        raise e
    finally:
        f.close()
    return filecontent

def replacelineinfilewithname (filename):
    try:
        print("Replace line in file with name", filename)
        linenumber = int(input("What is the line number you wish to replace content on?"))
        if linenumber < 1:
            raise Exception("Line number cannot be less than 1")
        filecontent = readAllFileContentsAndReplaceWithStringAtLine(filename, linenumber)
        content = input("What do you wish to replace with?")
        filecontent[linenumber-1] = content + "\n"
        f = open(filename, "w")
        for line in filecontent:
            f.write(line)
        f.close()
    except Exception as e:
        print("Unable to replace content in file with name: ", filename)
        raise e


def createfilewithname (filename):
    try:
        print("Create file with name", filename)
        content = input("What do you wish to write in the file?")
        f = open(filename, "w")
        while content!="":
            f.write(content)
            f.write("\n")
            content = input()
    except Exception as e:
        print("Unable to create file with name: ", filename)
    finally:
        f.close()

def throwexception(filename):
    raise Exception("Sorry, wrong command entered for processing file with name " + filename)

def processfilewithcommand(filename, commandnumber):
    commandswitcher = {
        COMMAND.READ.value:readfilewithname,
        COMMAND.DELETE.value:deletefilewithname,
        COMMAND.APPEND.value:appendtofilewithname,
        COMMAND.REPLACE.value: replacelineinfilewithname,
    }
    func = commandswitcher.get(commandnumber, throwexception);
    func(filename)

def readandprocesscommandforfile(filename):
    try:
        command = input("Enter command number to process the file, READ (1) | DELETE (2) | APPEND (3) | REPLACE (4):")
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

