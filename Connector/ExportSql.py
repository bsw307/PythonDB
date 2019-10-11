import pandas as pd
from sqlalchemy import create_engine
import json
#from itertools import iteritems
import GenerateJson

def get_sql():

    current = "Settings.json"

    if input("Current settings file is {}. Do you want to change the file?y/n".format(current) + "\n" ).lower() == "y":
        current = input("New: " + "\n")

    with open(current,"r") as json_file:

        var = json.load(json_file)

        #Iterates through necessary variables in json file
        for key,value in var["database"].iteritems():
            if input("Current {} is {}. Do you want to change the {}?y/n".format(key,value,key) + "\n" ).lower() == "y":
                var["database"][key] = input("New: " + "\n")


    database = "mysql+pymysql://{}:{}@{}/{}".format(var["database"]["user"],var["database"]["password"],var["database"]["hostname"],var["database"]["database_name"])

    engine = create_engine(database)
    cnxn = engine.connect()

    df = pd.read_sql("{}".format(input("sql command, please don't drop all my tables: ")), cnxn)
    df.to_csv("{}.csv".format(input("New file name: ")))
    cnxn.close()

get_sql()