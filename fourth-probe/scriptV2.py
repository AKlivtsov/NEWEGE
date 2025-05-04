import os

current_folder = os.path.dirname(os.path.abspath(__file__))

with open(f"{current_folder}/.taskignore", "r") as f:
    ignored = [int(task.split("/n")[0]) for task in f.readlines()]

for i in range(1, 28):
    if i in ignored:
        continue

    path = f"{current_folder}/{i}_task"
    os.makedirs(path, exist_ok=True)
    with open(path + "/ans.txt", "w") as f:
        pass
