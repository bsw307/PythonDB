import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

import GenerateJson

#Load variables from json file
scope = []
creds = ""
url = ""
database = ""
spreadsheet = ""
table_name = ""

fileName = GenerateJson.create()

with open(fileName, "r") as Json_vars:
    var = json.load(Json_vars)
    scope = [var["scopes"]["scope_1"],var["scopes"]["scope_2"]]
    creds = var["credentials"]
    url = var["url"]
    user = var["database"]["user"]
    password = var["database"]["password"]
    hostname = var["database"]["hostname"]
    database_name = var["database"]["database_name"]
    database = "mysql+pymysql://{}:{}@{}/{}".format(user,password,hostname,database_name)
    spreadsheet = var["spreadsheet_name"]
    table_name = var["table_name"]

print(scope,"\n",creds,"\n",url,"\n",database,"\n",spreadsheet,"\n",table_name,"\n",)

def sheet_to_sql():

    #Get credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name(creds, scope)

    #Connect to sheets
    gc = gspread.authorize(credentials)
    spr = gc.open_by_url(url)

    #Connect to sql
    engine = create_engine(database)
    connection = engine.connect()

    #Get data from spreadsheet and convert to sql
    list_of_lists = spr.worksheet(spreadsheet).get_all_values()
    df = pd.DataFrame(list_of_lists)
    df.to_sql(table_name,engine)

    #Close connection to database
    connection.close()

sheet_to_sql()