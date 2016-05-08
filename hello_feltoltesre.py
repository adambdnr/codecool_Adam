import sys

def sayhello(name):
    print('Hello ',name)

if len(sys.argv) == 2:
    name = sys.argv[1]
    sayhello(name)

else:
    print ('Hello World!')
