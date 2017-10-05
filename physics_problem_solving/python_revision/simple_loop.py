list = range(10,21)

def loop():
    for i in range(len(list)):
        print list[i]
        print list[i] ** 2

def f(x,y):
    function = (x * y) ** (0.5)
    print function

if __name__ == '__main__':
    f(2.,1.)
    #loop()
