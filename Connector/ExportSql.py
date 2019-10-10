import pandas as pd
from sqlalchemy import create_engine

def get_sql():

    engine = create_engine("mysql+pymysql://Baltasar:Pumajaws@Baltasar.mysql.pythonanywhere-services.com/Baltasar$default")
    cnxn = engine.connect()

    df = pd.read_sql("{}".format(input("sql command, please don't drop all my tables: ")), cnxn)
    csvFile = df.to_csv()
    with open("newFile.csv","w+") as new_file:
        new_file = csvFile
    cnxn.close()
    
get_sql()