from math import dist

def get_medoid(cluster):
    return min(cluster, key=lambda p: sum(dist(p,q) for q in cluster))

with open("2025-06-02_27cluster/task2/1_27_A/1_27_A.txt", "r+") as file:
    next(file)
    cluster1 = []
    cluster2 = []

    for line in file:
        x, y = map(float, line.replace(",", ".").split())
        if y > 2:
            cluster1.append((x,y))
        else:
            cluster2.append((x,y))

with open("2025-06-02_27cluster/task2/1_27_B/1_27_B.txt", "r+") as file:
    next(file)
    cluster3 = []
    cluster4 = []
    cluster5 = []

    for line in file:
        x, y = map(float, line.replace(",", ".").split())
        if x < 10:
            cluster3.append((x,y))
        elif 10 < x < 20:
            cluster4.append((x,y))
        else: 
            cluster5.append((x,y))

medoid1 = get_medoid(cluster1)
medoid2 = get_medoid(cluster2)
medoid3 = get_medoid(cluster3)
medoid4 = get_medoid(cluster4)
medoid5 = get_medoid(cluster5)

pxA = (medoid1[0] + medoid2[0]) / 2
pyA = (medoid1[1] + medoid2[1]) / 2
pxB = (medoid3[0] + medoid4[0] + medoid5[0]) / 3
pyB = (medoid3[1] + medoid4[1] + medoid5[1]) / 3

print(abs(int(pxA*10000)), abs(int(pyA*10000)))
print(abs(int(pxB*10000)), abs(int(pyB*10000)))
