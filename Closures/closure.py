def outer():
    x = 'python'

    def inner():
        #x = "java"
        print("{0} rocks!".format(x)) #here x is in closure

    inner()

outer()


def outer1():

    x = 'golang'

    def inner1():
        print("{0} also rocks!".format(x)) #here x is in closue

    return inner1()

outer1()

print("Python points to same cell using intermediary object cell")

print("Closure is a function + extended scope that contains free variables")
print("Whenever a free variable is called it looks up for that value")
