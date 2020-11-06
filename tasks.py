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

    index = ["Logitech G502 Lightspeed Wireless Gaming Mouse","TVS Electronics Gold Keyboard","Seagate Expansion Portable 3TB External Hard Drive HDD","ASUS Prime H310M-CS R2.0 mATX Motherboard","Corsair CV450 Watt Non-Modular Power Supply","Samsung 23.5 inch Curved LED Backlit Computer Monitor LC24F390FHWXXL","AMD Ryzen 7 3700X Desktop Processor 8 Cores up to 4.4GHz 36MB Cache","Gigabyte Nvidia GeForce RTX 2060 OC 6GB GDDR5 Graphic Cards","Ant Esports ICE-120AG Mid Tower Black","WD Blue PCIe NVMe SSD, 2400MB/s R, 1750MB/s W, 5 Y Warranty, 500GB"]
    col = ["Prices"]

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

    except Exception as e:
            print(e)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    ndf1 = pd.DataFrame(df1,index=index,columns=col)
    ndf2 = pd.DataFrame(df2,index=index,columns=col)

    #print("DF1-->", ndf1)
    #print("DF2-->", ndf2)
    return calc_diff(ndf1,ndf2)

def calc_diff(yest, today):
    # Today's price - Yesterday's
    res = today - yest
    #print(res)
    return res.to_json()

if __name__ == "__main__":
    print(clean())
