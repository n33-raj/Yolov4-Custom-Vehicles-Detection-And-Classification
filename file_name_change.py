import os

os.getcwd()

# path = "Images/test/"
path = "C:/Users/lenovo/Downloads/car/"
file_type = "txt"

for i, filename in enumerate(os.listdir(path)):

    i = str(i)

    if len(i)==1:
        i = "car"+i
    elif len(i)==2:
        i = "car"+i
    elif len(i)==3:
        i = "car"+i
    else:
        i = str(i)

    os.rename(path + filename, path + str(i) + "." + file_type)