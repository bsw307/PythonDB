import pandas as pd
from sqlalchemy import create_engine
import json

import GenerateJson

def get_sql():

    GenerateJson.create()

    with open("Settings.json","r") as json_file:
        var = json.load(json_file)
        
    hostname = "mysql+pymysql://{}:{}@{}/{}".format(var["database"]["user"],var["database"]["password"],var["database"]["hostname"],var["database"]["database_name"])
    if input("Current hostname is {}. Do you want to change the hostname?y/n".format(hostname) + "\n" ).lower() == "y":
            var = input("New: " + "\n")

    engine = create_engine(hostname)
    cnxn = engine.connect()

    df = pd.read_sql("{}".format(input("sql command, please don't drop all my tables: ")), cnxn)
    df.to_csv("{}.csv".format(input("New file name: ")))
    cnxn.close()

get_sql()