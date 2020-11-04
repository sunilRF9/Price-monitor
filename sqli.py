import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user = "coutinho",
                                  password = "d3dx9",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "pcbuild")

    cursor = connection.cursor()
    print(cursor)
    prods = ['ryzen7', 'corsair16gb']
    #create_table_query = 'select * from products'
    prices = [29000, 9000, 19000, 9000]
    for k,p in enumerate(prices, start=1):
        cursor.execute("INSERT INTO prices(pid, prices) VALUES(%s, %s)",(k,p,))
    #create_table_query = '''create table test (nid serial primary key, name varchar(255));'''
        #cur_obj = cursor.execute("INSERT INTO products(pname) VALUES(%s)",p)
        connection.commit()

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
