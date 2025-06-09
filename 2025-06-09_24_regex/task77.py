maxi = 0

with open("2025-06-09_24_regex/24_77.txt", "r+") as file:
    l = file.read()
    l = l.replace("-*", "!")
    l = l.replace("*-", "!")
    l = l.replace("**", "!")
    l = l.replace("--", "!")
    l = l.replace("0-", "!")
    l = l.replace("-0", "!")
    l = l.replace("0*", "!")
    l = l.replace("*0", "!")
    l = l.replace("-!", "!")
    l = l.replace("!-", "!")
    l = l.replace("*!", "!")
    l = l.replace("!*", "!")
    l = l.replace("!!", "!")
    l = l.split("!")
    for line in l:
        print(line)
        maxi = max(maxi, len(line))

    print(maxi)
