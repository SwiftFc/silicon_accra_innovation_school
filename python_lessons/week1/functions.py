print(1,2,3, sep=' < ')

def meet(who="Henry"):
    print("Hello,", who)

meet()
meet(who="Asiedu")
meet("world")
meet(who="Dade")
meet("Kwesi")

def mult_by_six(i):
    return 6 * i

def call(fn, arg):
    #call fn on arg
    return fn(arg)

def tripled_call(fn, arg):
    #call fn on the result of calling fn on arg
    return fn(fn(fn(arg)))

print(
        call(mult_by_six, 1),
        tripled_call(mult_by_six, 1))
