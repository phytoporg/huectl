from phue import Bridge

b = Bridge('192.168.1.119')

b.connect()
b.get_api()

groups = b.get_group()
for k in groups:
    print(groups[k])
