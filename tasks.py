import psycopg2
import numpy as np
import pandas as pd
from psycopg2 import Error
from datetime import date 
from datetime import timedelta 
today = date.today()
yest = today - timedelta(days=1)
def clean():
    d1 = []
    d2 = []
    try:
        connection = psycopg2.connect(user = "coutinho",
                                      password = "d3dx9",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "pcbuild")

        cursor = connection.cursor()
        ##Previous day
        for v in range(1,11):
            cursor.execute(f'''
            select distinct prices from prices where pid = {v} AND timestamp >= '{str(yest)} 00:00:00' AND timestamp < '{str(yest)} 23:59:59'
            ''')
            row = cursor.fetchall()
            d1.append(str(row).replace('[', '').replace(']','').replace('(','').replace(')','').replace(',',''))
        ##Current day
        for v in range(1,11):
            cursor.execute(f'''
            select distinct prices from prices where pid = {v} AND timestamp >= '{str(today)} 00:00:00' AND timestamp < '{str(today)} 23:59:59'
            ''')
            row = cursor.fetchall()
            d2.append(str(row).replace('[', '').replace(']','').replace('(','').replace(')','').replace(',',''))
            df1 = list(np.array(d1).astype(float))
            df2 = list(np.array(d2).astype(float))
            ndf1 = pd.DataFrame(df1)
            ndf1.index = ndf1.index + 1
            ndf1.columns = ["Prices"]
            ndf2 = pd.DataFrame(df2)
            ndf2.index = ndf2.index + 1
            ndf2.columns = ["Prices"]
    except Exception as e:
            print(e)
    #print(ndf1)
    #print(ndf2)
    return ndf1, ndf2

def calc_diff(ndf1, ndf2):
    # Today's price - Yesterday's
    return ndf2 - ndf1

if __name__ == "__main__":
    ndf1, ndf2 = clean()
    print(calc_diff(ndf1, ndf2))
