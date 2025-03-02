with open("2025-02-18_24num/24_3.txt", "r+") as file:
    st = file.readline()
    ans = []
    line = ""
    left_frame = 0
    right_frame = 0
    alph = "qwertyuiopasdfghjklzxcvbnm".capitalize()

    for i in range(len(st)):
        line += st[i]
        
        while line.count(alph) > 1:
            if line.count(st[left_frame]) > 1:
                line -= st[left_frame] 

            left_frame += 1

        ans.append(right_frame - (i - left_frame + 1))

print(ans)


