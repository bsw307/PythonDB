import json
import os.path

def changeVal(key,val,file):

    #Recursively goes through sub dictionaries
    if isinstance(val,dict) == True:
        tmpdict = {}
        for i in val:
            tmpdict[i] = changeVal(i,val[i],file)
        return tmpdict

    #Ask for new value
    else:
        if input("Current {} is {}. Do you want to change {}?y/n".format(key,val,key) + "\n" ).lower() == "y":
            newval = input("New value: " + "\n")
            return newval
        else:
            return val



def create():   
    current = "Settings.json"
    #Iterative loop goes through all json settings to change them
    if input("Do you want to use the same settings as last time?y/n" + "\n" ).lower() == "y":
        return current

    else:
        with open("/Config_files/{}".format(current),"r") as json_file:
            data = json.load(json_file)
            tmp = data
            
            #Calls changeVal for each value in json file
            for i in data:
                data[i] = changeVal(i,data[i],tmp)


        with open("/Config_files/{}".format(current),"w") as newFile:
            json.dump(tmp,newFile)
        return "Settings.json"

    json_file.close()