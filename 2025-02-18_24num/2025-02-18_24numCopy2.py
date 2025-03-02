with open("2025-02-18_24num/24_4.txt", "r+") as file:
    st = file.readline()
    answers = []
    count_hex = 0
    alph = "0123456789ABCDEF"

    for i in range(len(st)):
        if st[i] in alph:
            count_hex += 1
        else:
            answers.append(count_hex)
            count_hex = 0

print(max(answers))

