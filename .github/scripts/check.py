
import os
import sys

if __name__ == '__main__':
    print(os.listdir("./"))
    for i in os.listdir("./"):
        print(os.path.abspath(i))
    print(__file__)
    print(sys.path)
    import mypackage
    print(mypackage.hello.hello())