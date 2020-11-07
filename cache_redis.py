import redis
redis = redis.Redis(decode_responses=True)

def setcache(title, price):
    return redis.setex(title, 3600, price)

def getCache(title):
    title = str(title)
    return redis.get(title)

def checkcache():
    with open('f1.txt') as f: 
        line = f.readline() 
        while line: 
            #print("{}".format(line.strip()))
            line = f.readline()
            print(str(line))
            val = getCache(str(line))
            print(val)
