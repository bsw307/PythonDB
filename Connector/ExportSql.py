import pandas as pd
from sqlalchemy import create_engine
import json

def get_sql():

    current = "Settings.json"

    if input("Current settings file is {}. Do you want to change the file?y/n".format(current) + "\n" ).lower() == "y":
        current = input("New: " + "\n")

    with open("Config_files/{}".format(current),"r") as json_file:

        var = json.load(json_file)

        #Iterates through necessary variables in json file
        for key,value in var["database"].items():
            if input("Current {} is {}. Do you want to change the {}?y/n".format(key,value,key) + "\n" ).lower() == "y":
                var["database"][key] = input("New: " + "\n")


    database = "mysql+pymysql://{}:{}@{}/{}".format(var["database"]["user"],var["database"]["password"],var["database"]["hostname"],var["database"]["database_name"])

    engine = create_engine(database)
    cnxn = engine.connect()

    command = "{}".format(input("Enter sql select command : "))
    while True:
        if "drop" in command:
            command = "{}".format(input("To drop table use sql console instead. New: "))
        else:
            break

    df = pd.read_sql(command, cnxn)
    df.to_csv("{}.csv".format(input("New file name: ")))
    cnxn.close()

get_sql()