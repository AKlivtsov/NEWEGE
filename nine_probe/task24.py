with open("nine_probe/24.txt", "r+") as file:
    maxi = 0
    l = file.read()
    l = l.replace("+", "!")
    l = l.replace("**", "!")
    l = l.replace("*!", "!")
    l = l.replace("!*", "!")
    l = l.replace("!0", "!")
    l = l.replace("!!", "!")
    l = l.split("!")

    for item in l:
        if "*" not in item:
            continue

        h = [num for num in item.split("*")]
        if "0" not in h:
            continue

        if "" in h:
            h.remove("")

        bad = False
        for num in h:
            if (int(num) % 2 != 0) or (str(num)[-1] == "0"):
                bad = True

        if bad:
            continue

        h.append("*" * (len(h) - 1))

        comb = ""
        for sub in h:
            comb += str(sub)

        maxi = max(maxi, len(comb))

print(maxi)
