import pandas as pd
from sqlalchemy import create_engine

def get_sql():

    engine = create_engine("mysql+pymysql://Baltasar:Pumajaws@Baltasar.mysql.pythonanywhere-services.com/Baltasar$default")
    cnxn = engine.connect()

    df = pd.read_sql("{}".format(input("sql command, please don't drop all my tables: ")), cnxn)
    df.to_csv("newFile.csv")
    cnxn.close()

get_sql()