links = ["https://www.amazon.in/Logitech-Lightspeed-Wireless-Adjustable-Programmable/dp/B07S4JRHNJ/ref=sr_1_11_sspa?dchild=1&keywords=gaming+mouse&qid=1599541750&sr=8-11-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUldTWlBNWklFVkJPJmVuY3J5cHRlZElkPUEwNjMwMDA2MTlWTTkxVVhYOEtPSCZlbmNyeXB0ZWRBZElkPUEwMzU1NDAxRFYwQU9CQThVVzhXJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
        "https://www.amazon.in/TVS-Bharal-Gold-Keyboard-Black/dp/B07B75DVZS/ref=sr_1_2?crid=37R3YYYKEERHR&dchild=1&keywords=tvs+gold+keyboard&qid=1599199721&s=computers&sprefix=tvs+%2Ccomputers%2C296&sr=1-2",
        "https://www.amazon.in/Seagate-Expansion-Portable-External-Playstation/dp/B00ZTRXTPW/ref=sr_1_11?crid=17EA1K9AY8A6L&dchild=1&keywords=playstation+4&qid=1598851384&sprefix=Plays%2Caps%2C291&sr=8-11",
        "https://www.amazon.in/Prime-H310M-CS-Motherboard-Socket-2666MHz/dp/B07YMGXG42/ref=sr_1_2?crid=3LTN5JWLT7U7Y&dchild=1&keywords=asus+motherboard+gaming&qid=1598852196&sprefix=asus+mothre%2Caps%2C296&sr=8-2",
        "https://www.amazon.in/Corsair-Bronze-Certified-Non-Modular-Supply/dp/B07YVVXYFN/ref=sr_1_1?crid=2BN3C0J7L46OZ&dchild=1&keywords=corsair+power+supply&qid=1598852240&sprefix=corsair+%2Caps%2C445&sr=8-1",
        "https://www.amazon.in/Samsung-23-5-inch-Curved-Monitor/dp/B01GFPGHSM/ref=sr_1_2?crid=3QCAFQSYNILVL&dchild=1&keywords=samsung+curved+monitor&qid=1598852284&sprefix=Samsung+curv%2Caps%2C295&sr=8-2",
        "https://www.amazon.in/dp/B07SXMZLPK/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B07SXMZLPK&pd_rd_w=4Z0eJ&pf_rd_p=1801b34c-8af9-42b5-8961-11f124edc99b&pd_rd_wg=ifZ26&pf_rd_r=7E3Z97P2FTYF9RXR7KYT&pd_rd_r=abb57d6a-8e02-418a-a324-ee5d0904784e&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExU0hWWVpOMjdUNDA1JmVuY3J5cHRlZElkPUEwOTgzMzQ5N1FVM0lEMzI5UjdBJmVuY3J5cHRlZEFkSWQ9QTA5OTQyNjdGWDhIRkE0S0taWE0md2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl",
        "https://www.amazon.in/Gigabyte-GeForce-Graphic-Cards-GV-N2060OC-6GD/dp/B07MPM8HK1/ref=sr_1_2?crid=1ANQRHLRCRIT0&dchild=1&keywords=nvidia+rtx+2060&qid=1604468604&s=computers&sprefix=nvidia+rtx%2Ccomputers%2C296&sr=1-2",
        "https://www.amazon.in/Ant-Esports-ICE-120AG-Motherboard-Preinstalled/dp/B08CGCRNMS/ref=sr_1_3?crid=2PKDBPR9UYVPE&dchild=1&keywords=pc+cabinets&qid=1604468639&s=computers&sprefix=pc+ca%2Ccomputers%2C299&sr=1-3",
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
