# coding=utf-8
file = open("a.txt")
print (file.read())
print (file.name)
file.close()

import os
os.rename("a.txt", "b.txt")

filename = input("Enter your file name  ")
file = open(str(filename))
print (file.read())
file.close()

os.rename("b.txt","a.txt")

file = open("a.txt")
newfile = open("copy.txt","w+")
newfile.write(file.read())
print (newfile.read())
newfile.close()
file.close()
