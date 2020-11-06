import psycopg2
from celery import Celery
import numpy as np
import pandas as pd
from psycopg2 import Error
from datetime import date 
from datetime import timedelta 

today = date.today()
yest = today - timedelta(days=1)

app = Celery('tasks', backend='rpc://', broker='pyamqp://')

@app.task
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
        for v in range(1,11):

            ##Previous day
            cursor.execute(f'''
            select distinct prices from prices where pid = {v} AND timestamp >= '{str(yest)} 00:00:00' AND timestamp < '{str(yest)} 23:59:59'
            ''')
            row = cursor.fetchall()
            #print("Yest",row)
            # if a row as multiple price changes in a day, choose the lowest one
            raow = min([i[0] for i in row])
            d1.append(str(raow).replace('[', '').replace(']','').replace('(','').replace(')','').replace(',',''))
            #print(d1)

            ##Current day
            cursor.execute(f'''
            select distinct prices from prices where pid = {v} AND timestamp >= '{str(today)} 00:00:00' AND timestamp < '{str(today)} 23:59:59'
            ''')
            row = cursor.fetchall()
            #print("Today", row)
            # if a row as multiple price changes in a day, choose the lowest one
            rmin = min([i[0] for i in row])
            d2.append(str(rmin).replace('[', '').replace(']','').replace('(','').replace(')','').replace(',',''))
            #print(d2)

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
    return calc_diff(ndf1,ndf2)

def calc_diff(ndf1, ndf2):
    # Today's price - Yesterday's
    res = ndf2 - ndf1
    return res.to_json(orient='records')[1:-1].replace('},{', '} {')

if __name__ == "__main__":
    print(clean())
