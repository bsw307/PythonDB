import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("Quickstart-8209fc4d5cad.json", scope)

gc = gspread.authorize(credentials)

wks = gc.open("Global networks - COPY")

engine = create_engine("mysql+pymysql://{Baltasar}:{Pumajaws}@{Baltasar.mysql.pythonanywhere-services.com}/{Baltasar$PythonDatabase}")

connection = engine.connect()

list_of_lists = wks.get_all_values()



df = pd.DataFrame(list_of_lists)

df.to_sql("new_test",engine)

connection.close()