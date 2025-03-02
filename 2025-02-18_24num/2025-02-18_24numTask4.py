with open("2025-02-18_24num/24_4.txt", "r+") as file:
    st = file.readline()
    count_y = 0
    left_frame = 0
    right_frame = 0

    for i in range(len(st)):
        if st[i] == "T":
            count_y += 1
        
        while count_y > 100:
            count_y -= st[left_frame] == "T"
            left_frame += 1

        right_frame = max(right_frame, i - left_frame + 1)

print(right_frame)

