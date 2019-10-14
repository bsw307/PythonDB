import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import GenerateJson
import os
from GenerateJson import *
#from Settings import *

scope = []
creds = ""
url = ""
database = ""
spreadsheet = ""
table_name = ""

def send(Csv_file):
    
    #Load variables from settings.json
    current = "Settings.json"

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
    credentials = ServiceAccountCredentials.from_json_keyfile_name(creds, scope)
    gc = gspread.authorize(credentials)

    sh = gc.create(input("New spreadsheet: "))
    sh.share('baltasar.salamonwelwert@gmail.com', perm_type='user', role='writer')
    sh.share('connect-sheets-to-mysql@quickstart-1570036964435.iam.gserviceaccount.com', perm_type='user', role='writer')

    #Loop to share with other people
    while True:
      if input("Do you want to enter another email?" + "\n").lower() == "y":
        sh.share(input("Enter new mail: "), perm_type='user', role='writer')
      else:
        break

    content = open(Csv_file, 'r').read()
    content = content.encode('utf-8')
    gc.import_csv(sh.id, content)

files = [element for element in os.listdir() if element.endswith(".json")]

send(input("Which file do you want to send? Eligble files: {}".format(files)))