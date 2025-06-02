from math import dist

def get_medoid(cluster):
    return min(cluster, key=lambda p: sum(dist(p, q) for q in cluster))


with open("2025-06-02_27cluster/task1/2702_A.txt", "r") as file:
    next(file)
    # cahnge here , to . if presented 
    cluster_1 = []
    cluster_2 = []

    for line in file:
        x, y = map(float, line.split())
        if x < 1:
            cluster_1.append((x,y))
        else:
            cluster_2.append((x,y))

medoid_1 = get_medoid(cluster_1)
medoid_2 = get_medoid(cluster_2)

px = (medoid_1[0] + medoid_2[0]) / 2
py = (medoid_1[1] + medoid_2[1]) / 2
print(abs(int(px*10000)), abs(int(py*10000)))