import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from GenerateJson import *
#from Settings import *

scope = []
creds = ""
url = ""
database = ""
spreadsheet = ""
table_name = ""

def sheet_to_sql():

    #Json_settings()

    current = create()

    with open("Config_files/{}".format(current), "r") as Json_vars:
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
        table_name = var["table_name"]    #Get credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name("Config_files/{}".format(creds), scope)

    #Connect to sheets
    gc = gspread.authorize(credentials)
    spr = gc.open_by_url(url)

    #Connect to sql
    engine = create_engine(database)
    connection = engine.connect()

    #Get data from spreadsheet and convert to sql
    list_of_lists = spr.worksheet(spreadsheet).get_all_values()
    print(list_of_lists[0])
    df = pd.DataFrame(list_of_lists)
    df.to_sql(table_name,engine)

    #Close connection to database
    connection.close()

sheet_to_sql()