import ipaddress

net = ipaddress.ip_network("212.192.32.96/255.255.255.224")

c = 0
for ip in net:
    c += 1

print(c) # 32
