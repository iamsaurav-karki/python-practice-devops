import shutil
import datetime
import os

def backup_file(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name.replace('.tar.gz',''), 'gztar',source)
    print("Backup successful")
source = "D:/python-for-devops/real-project-implementation"
destination = "D:/python-for-devops/real-project-implementation/backups"
backup_file(source, destination)