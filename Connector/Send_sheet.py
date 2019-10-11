import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import GenerateJson

scope = []
creds = ""
url = ""
database = ""
spreadsheet = ""


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

def send(Csv_file):
            
    gc = gspread.authorize(creds)
    sh = gc.create(input("New spreadsheet: "))
    sh.share('baltasar.salamonwelwert@gmail.com', perm_type='user', role='writer')

    content = open(Csv_file, 'r').read()
    gc.import_csv(sh, content)

