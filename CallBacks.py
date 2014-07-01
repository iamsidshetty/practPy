__author__ = 'sid'


def testFunctOne(val, callbackOne, callbackTwo):
    print "Just a Callback by %s" % val
    callbackOne()
    callbackTwo()


def testFunctTwo():
    print "Finished Callback 1"

def testFunctThree():
    print "Finished Callback 2"

if __name__ == "__main__":
    testFunctOne('Sid', testFunctTwo, testFunctThree)
