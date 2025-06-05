
def alg(n):
    while "00" not in n:
        n = n.replace("01", "103", 1)
        n = n.replace("02", "201", 1)
        n = n.replace("03", "2110", 1)
    return n

for x in range(1, 100):
    print(x)
    for y in range(1, 100):
        for z in range(1, 100):

            res = alg("0"+ "1"*x + "2"*y + "3"*z +"0")

            if res.count("1") == 196 and res.count("2") == 75 and res.count("3") == 0:
                print(len("0"+ "1"*x + "2"*y + "3"*z +"0"))
                break


# 68

