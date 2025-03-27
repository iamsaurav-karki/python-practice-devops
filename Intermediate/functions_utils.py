import os
def run_command(command):
    return os.system(command)

def get_disk_space():
    return run_command("df -h")

print(get_disk_space())
# print(run_command("ipconfig"))

def show_date():
    return run_command("date")

print(show_date())