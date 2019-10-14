import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import GenerateJson
import os
import csv
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
    credentials = ServiceAccountCredentials.from_json_keyfile_name("Config_files/{}".format(creds), scope)
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

    #Test bulk update
    worksheet = sh.add_worksheet(title="A worksheet", rows="100", cols="20")
    reader = csv.reader(content, delimiter=',')
    cell_list = worksheet.range('A1:A2')
    tmpcell = []
    for i, row in reader:
      print("Row: ", row)
      for x, column in row:
        print("column: ", column)
        tmpcell.append(content[i][x])
    for i,val in enumerate(tmpcell):
      cell_list[i].value = val
    worksheet.update_cells(cell_list)
        

    #Regular
    """
    content = content.encode('utf-8')
    gc.import_csv(sh.id, content)
    """

files = [element for element in os.listdir() if element.endswith(".csv")]

send(input("Which file do you want to send? Eligble files: {}".format(files)))