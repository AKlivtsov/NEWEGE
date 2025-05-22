import os
import datetime


def create_new_folder():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    type_of_task = input("Type of task: ")
    folder_name = f"{today}_{type_of_task}"
    os.makedirs(folder_name, exist_ok=True)

    with open(folder_name + "/task1-3.py", "w") as f:
        pass

    with open(folder_name + "/linkToTasks.txt", "w") as f:
        pass

    print(f"New folder and python file created: {folder_name}")


create_new_folder()
