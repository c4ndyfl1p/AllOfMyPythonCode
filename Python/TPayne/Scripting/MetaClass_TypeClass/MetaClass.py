#!/usr/bin/env python2

class Singleton(type):
        _instances = {}
        def __call__(cls, *args, **kwargs):
                if cls not in cls._instances:
                        cls._instances[cls] = super(Singleton, cls).__class__(*args, **kwargs)
                        cls.x = 1
                return cls._instances[cls]

class MyClass(object):
        __metaclass__ = Singleton

m = MyClass()
v = MyClass()
print m.x
m.x = 2
print v.x
