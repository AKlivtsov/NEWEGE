from math import dist

def get_medoid(cluster):
    return min(cluster, key=lambda p: sum(dist(p ,q) for q in cluster))

def starsA():
    with open("2025-06-02_27cluster/task3/A.txt", "r+") as file:
        next(file)

        cluster1 = []
        cluster2 = []
        for line in file:
            x, y = map(float, line.replace(",", ".").split())
            if y < 15:
                cluster1.append((x,y))
            else:
                cluster2.append((x,y))

        medoid1 = get_medoid(cluster1)
        medoid2 = get_medoid(cluster2)

        px = (medoid1[0] + medoid2[0]) / 2
        py = (medoid1[1] + medoid2[1]) / 2

        return abs(int(px*10000)), abs(int(py*10000))
    
def starsB():
    with open("2025-06-02_27cluster/task3/B.txt", "r+") as file:
        next(file)

        cluster1 = []
        cluster2 = []
        cluster3 = []

        for line in file:
            x, y = map(float, line.replace(",", ".").split())
            if y < -2:
                cluster1.append((x,y))
            elif -2 < y < 5:
                cluster2.append((x,y))
            else:
                cluster3.append((x,y))

        medoid1 = get_medoid(cluster1)
        medoid2 = get_medoid(cluster2)
        medoid3 = get_medoid(cluster3)

        px = (medoid1[0] + medoid2[0] + medoid3[0]) / 3
        py = (medoid1[1] + medoid2[1] + medoid3[1]) / 3

        return abs(int(px*10000)), abs(int(py*10000))
    
print(starsA(), starsB())