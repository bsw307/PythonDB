import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import GenerateJson

scope = []
credentials = ""
url = ""
database = ""
spreadsheet = ""


fileName = GenerateJson.create()

with open(fileName, "r") as Json_vars:
    var = json.load(Json_vars)
    scope = [var["scopes"]["scope_1"],var["scopes"]["scope_2"]]
    credentials = var["credentials"]
    url = var["url"]
    user = var["database"]["user"]
    password = var["database"]["password"]
    hostname = var["database"]["hostname"]
    database_name = var["database"]["database_name"]
    database = "mysql+pymysql://{}:{}@{}/{}".format(user,password,hostname,database_name)
    spreadsheet = var["spreadsheet_name"]

def send(Csv_file):
    
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)
    gc = gspread.authorize(creds)
    sh = gc.create(input("New spreadsheet: "))
    sh.share('baltasar.salamonwelwert@gmail.com', perm_type='user', role='writer')
    sh.share('connect-sheets-to-mysql@quickstart-1570036964435.iam.gserviceaccount.com', perm_type='user', role='writer')


    content = open(Csv_file, 'r').read()
    content = content.encode('utf-8')
    gc.import_csv(sh, content)

send(input("Which file do you want to send?"))