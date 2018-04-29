#coding=utf-8

import os

for filename in os.listdir("./"):
    if filename.find(".txt")!=-1:
        print(filename)
        os.system("git add "+filename)
        os.system("git commit -m "+filename)