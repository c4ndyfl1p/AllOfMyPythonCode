#!/usr/bin/env python2
from os import path
def createFileLoop(dest):
    for i in range(5):
        f = open('FileNo.%d'%i, 'w')
        f.write("something")
        f.close
    
if __name__ == "__main__":
    destination = '/home/jatin/Documents/Python/TPayne/CreatingTextFiles/'
    createFileLoop(destination)
    print 'done!'

