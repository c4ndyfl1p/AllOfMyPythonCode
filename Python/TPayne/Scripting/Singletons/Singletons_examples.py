#!/usr/bin/env python2

class AutoIncr(object):
       _instance = None
       def __new__(self, *args, **kwargs):
                if not self._instance:
                       self._instance = super(AutoIncr, self).__new__(self)
                       self.value = 0
                self.value += 1
                return self.value

if __name__ == "__main__":
        print AutoIncr()
