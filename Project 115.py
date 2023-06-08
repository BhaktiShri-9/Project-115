import os

source= "C:/Users/Nag/Downloads"              
destination = "C:/Users/Nag/Desktop/Downloaded_Files"
os.rename(source, destination)
print('Source path renamed to destination path sucessfully!')