import json
import os

def CrearData (*args : tuple):
    if CheckData(args[0]) == False:
        with open('data/'+args[0],'w') as writeFile:
            json.dump(args[1], writeFile, indent = 4)
            writeFile.close()
    else:
        with open('data/'+args[0],'r+') as file:
            fileData = json.load(file)
            fileData["data"].append(args[1])
            file.seek(0)
            json.dump(fileData, file, indent = 4)
            file.close()

def EditarData (*args):
    with open('data/'+args[0],'w') as writeFile:
        json.dump(args[1], writeFile, indent = 4)
        writeFile.close() 

def LoadData(FileName):
    if (CheckData(FileName) == True):
        with open('data/'+FileName, 'r') as readFile:
            dicc = json.load(readFile)
        return dicc

def CheckData (Filename):
    try:
        with open('data/'+Filename, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
    