import shutil

basepath = 'D:\\Polito\\Magistrale\\Machine learning and Artificial intelligence\\MLAI_DomainToText\\PACS\\kfold\\'
destinationpath = 'C:\\Users\\Gaetano\\Desktop\\images'

file = open("photo.txt", "r")

lines = file.readlines()

for line in lines:
    line = line.replace("\n", "")
    line = line.replace("/", "\\")
    fields = line.split(" ")
    path = basepath + fields[0]

    shutil.copy(path, destinationpath)