for x in range(397, 10**5):
    r = str(bin(x)[2:])
    if (r.count("1") % 2 == 0) and r[-2:] == "00":
        print(x)
        break


print(bin(402)[2:])