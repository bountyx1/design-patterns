from thirdpartylib import Hack

hack = Hack()
hack.test()


# Overriding the  Method test of Hack()
def test(self):
    print("Test done")

Hack.test = test

h = Hack()
h.test() 
