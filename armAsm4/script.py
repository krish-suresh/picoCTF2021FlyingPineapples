sp28 = 3459413018
def func1(x):
    if x <= 100:
        #L2
        #func3 sp28
        #func7 sp28
        if x <=100:
            #L18
            print(x)
        else:
            print(7)
        #L3
    else:
        x += 100
        #go to func2
        if x > 499:
            x = x+13
            #func 8 with that^
            x += 2
            print(x)
        else:
            x = x-86
            #func 4
            func1(17)
            # func1 call -> store in sp44
            #L6
        #L3
    sp28 = x

func1(sp28)

def func7(x):
    if x <= 100:
        return 7
    return x

def func8(x):
    return x+2