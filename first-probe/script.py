import os

for i in range(1, 28):
    path = f"first-probe/{i}_task"
    os.makedirs(path, exist_ok=True)
    with open(path + "/ans.txt", "w") as f:
        pass
