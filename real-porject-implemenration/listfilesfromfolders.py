import os
folder = input("Please provide list of folder names with spaces in between:")
folders = folder.split()
for folder in folders:
    
    try:
      files = os.listdir(folder)
    except FileNotFoundError:
        print("Folder not found. Please provide correct folder in your device." + " " + folder)
        break

    print("Files in folder:", folder)

    for file in files:
        print(file)
