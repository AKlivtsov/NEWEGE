# run this to create new folder for the day 

import os
import datetime

def create_new_folder():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    type_of_task = input("Type of task: ")
    folder_name = f"{today}_{type_of_task}"
    os.makedirs(folder_name, exist_ok=True)

    # create a python file in the new folder
    with open(os.path.join(folder_name, f"{folder_name}.py"), 'w') as f:
        pass

    # create a text file in the new folder
    with open(os.path.join(folder_name, "explaining.txt"), 'w') as f:
        pass

    print(f"New folder and python file created: {folder_name}")

create_new_folder()
