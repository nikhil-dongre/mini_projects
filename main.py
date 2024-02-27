import os

files = os.listdir()
files.remove("main.py")

directories = ['Images', 'Docs', 'Media', 'Js']
imgext = [".png",".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgext]
docext = [".odt",".xls", ".xlsx",".txt"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docext]
# os.makedirs('others')
others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()

    if (ext not in imgext) and (ext not in docext):
        if os.path.isfile(file):
            others.append(file)

def move_folder(folder_name,all_files):
    for file in all_files:
        os.replace(file,f"{folder_name}/{file}")


move_folder("Docs",docs)
move_folder("Images",images)
move_folder("others",others)