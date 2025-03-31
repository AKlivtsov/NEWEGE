text = [x for x in open("2025-03-13_17num/17 (5).txt", "r")]
text = [int(text[i][1:]) if text[i].startswith("-") else int(text[i]) for i in range(len(text))]
# text = [abs(int(x)) for x in open("2025-03-13_17num/17 (5).txt", "r")]


for i in range(0, len(text)):
    for j in:

