class B(object):
    def test(self):
        print "ham"
                
class I(B):
    def test(self):
        print "hammer time"

    
print B.__subclasses__()
