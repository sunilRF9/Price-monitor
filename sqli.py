import psycopg2
from psycopg2 import Error
from crawler_args import *
def readfi():
    with open('insert_to_pg.txt', 'r') as f:
        op = f.read().splitlines()
    return op
try:
    connection = psycopg2.connect(user = "coutinho",
                                  password = "d3dx9",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "pcbuild")

    cursor = connection.cursor()
    print(cursor)
    #create_table_query = 'select * from products'
    #prices = [29000, 9000, 19000, 9000]
    op = [scraper(k,link) for k,link in enumerate(links, start=1)]
    print(op)
    for k,v in enumerate(op, start=1): 
        cursor.execute("INSERT INTO prices(pid, prices) VALUES(%s,%s)",(k,v,))
        connection.commit()
except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
