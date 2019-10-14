import json
import GenerateJson

#Load variables from json file
scope = []
creds = ""
url = ""
database = ""
spreadsheet = ""
table_name = ""


def Json_settings():
    
    current = GenerateJson.create()

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

print("Test", creds)