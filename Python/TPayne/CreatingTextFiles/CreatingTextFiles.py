#!/usr/bin/python

import time as t
from os import path

def createFile(dest):
    date = t.localtime(t.time())

    name = '%d_%d_%d'%(date[1], date[2], (date[0] % 100))

    if not(path.isfile(dest + name)):
        f = open(dest + name, 'w')
        f.write("\n"*30)
        f.close
        
if __name__ == "__main__":
    destination = '/home/jatin/Documents/'
    createFile(destination)
    raw_input("Done!!")

