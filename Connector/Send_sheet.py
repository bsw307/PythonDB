import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import GenerateJson
import os
from Settings import *

def send(Csv_file):
    
    #Load variables from settings.json
    Json_settings()

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