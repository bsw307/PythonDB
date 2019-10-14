import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

from Settings import *


def sheet_to_sql():

    Json_settings()
    print("test",creds,scope)
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