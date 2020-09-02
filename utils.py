links = [
        "https://www.amazon.in/Logitech-Wireless-Cross-Computer-Control-Sharing/dp/B071YZJ1G1/ref=sr_1_1?crid=2SDAUCOU39HU4&dchild=1&keywords=mx+master+3&qid=1598853736&sprefix=mx+mas%2Caps%2C401&sr=8-1",
        "https://www.amazon.in/HyperX-Tenkeyless-Mechanical-HX-KB4RD1-US-R1/dp/B074F5L8GQ/ref=sr_1_1?crid=20RJWL0W25FA4&dchild=1&keywords=mechanical+keyboard+cherry+mx&qid=1598853872&sprefix=mechanical+keyboard+cherry%2Caps%2C406&sr=8-1",
"https://www.amazon.in/TechKnox-PlayStation-Dual-Shock-Controller/dp/B08GHDWKPG/ref=sr_1_15?crid=17EA1K9AY8A6L&dchild=1&keywords=playstation+4&qid=1598851384&sprefix=Plays%2Caps%2C291&sr=8-15",
        "https://www.amazon.in/Seagate-Expansion-Portable-External-Playstation/dp/B00ZTRXTPW/ref=sr_1_11?crid=17EA1K9AY8A6L&dchild=1&keywords=playstation+4&qid=1598851384&sprefix=Plays%2Caps%2C291&sr=8-11",
        "https://www.amazon.in/Prime-H310M-CS-Motherboard-Socket-2666MHz/dp/B07YMGXG42/ref=sr_1_2?crid=3LTN5JWLT7U7Y&dchild=1&keywords=asus+motherboard+gaming&qid=1598852196&sprefix=asus+mothre%2Caps%2C296&sr=8-2",
        "https://www.amazon.in/Corsair-Bronze-Certified-Non-Modular-Supply/dp/B07YVVXYFN/ref=sr_1_1?crid=2BN3C0J7L46OZ&dchild=1&keywords=corsair+power+supply&qid=1598852240&sprefix=corsair+%2Caps%2C445&sr=8-1",
        "https://www.amazon.in/Samsung-23-5-inch-Curved-Monitor/dp/B01GFPGHSM/ref=sr_1_2?crid=3QCAFQSYNILVL&dchild=1&keywords=samsung+curved+monitor&qid=1598852284&sprefix=Samsung+curv%2Caps%2C295&sr=8-2",
        "https://www.amazon.in/AMD-Ryzen-3600X-Processor-100000022BOX/dp/B07SQBFN2D/ref=sr_1_1_sspa?crid=DL8J259L05D0&dchild=1&keywords=ryzen+5+3600&qid=1598852312&sprefix=ryzen%2Caps%2C445&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE5Q1NCWVFGSjlIWjUmZW5jcnlwdGVkSWQ9QTA0MjA0NjUyOFYySDlZN05aMkdYJmVuY3J5cHRlZEFkSWQ9QTAyMjgyMTkxTzZCOVpCOVRaNEhUJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
        "https://www.amazon.in/Zotac-Gaming-GeForce-GDDR6-Graphics/dp/B07QC8RSZB/ref=sr_1_1?crid=N3QKIA2CHUGJ&dchild=1&keywords=rtx+2060&qid=1598852349&sprefix=rtx+%2Caps%2C291&sr=8-1",
        "https://www.amazon.in/CHIPTRONEX-X310B-GAMING-CABINET-WITHOUT/dp/B078Z88HT9/ref=sr_1_1?crid=32S5MI0PIY7KE&dchild=1&keywords=cabinet+for+pc&qid=1598852383&sprefix=cabin%2Caps%2C402&sr=8-1",
        "https://www.amazon.in/Western-Digital-SN550-Internal-WDS500G2B0C/dp/B07YFF3JCN/ref=sr_1_1_sspa?crid=1VYL5Y3AFUH24&dchild=1&keywords=ssd+512gb+internal+for+desktop&qid=1598852423&sprefix=ssd+512%2Caps%2C434&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzR1VDTjY1TjlSWVlBJmVuY3J5cHRlZElkPUEwMDgxMjY4MVNPUzdNNjJHQk9KRCZlbmNyeXB0ZWRBZElkPUEwNDUyNjI0MzgxMTYyWEo4NjY3SCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        ]
def getUserAgent():
    import random
    with open('user.txt', 'r') as f:
        lines = f.readlines()
    user_agent = random.choice(lines).strip()
    return user_agent

def getProxy():
    from proxyscraper import proxyScrap
    return proxyScrap()

def compute(data):
    total = []
    for v in data.values():
        v =  v.lstrip("₹ ")
        v = v.replace(",","")
        total.append(int(float(v)))
    return sum(total)

if __name__ == "__main__":
    val = getUserAgent()
    print(val)
    prox = getProxy()
    print(prox)
