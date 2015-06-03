class BaseClass(object):
    def __init__(self):
        print 'ham'

class InClass(BaseClass):
    def __init__(self):
        super(InClass, self).__init__(self):

a = BaseClass()
b = InClass()
