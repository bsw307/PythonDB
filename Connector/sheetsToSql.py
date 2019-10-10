import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name("Quickstart-289b63edd2a2.json", scope)

gc = gspread.authorize(credentials)

spr = gc.open_by_url("https://docs.google.com/spreadsheets/d/1Mfy2LE_C0RRB8WIfvdKm72-aOGSFdV27JE9NAmwePnk/edit#gid=830064553")

engine = create_engine("mysql+pymysql://Baltasar:Pumajaws@Baltasar.mysql.pythonanywhere-services.com/Baltasar$default")
connection = engine.connect()

list_of_lists = spr.get_all_values()
print(list_of_lists)


df = pd.DataFrame(list_of_lists)

df.to_sql("new_test",engine)

connection.close()