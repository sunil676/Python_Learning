#How to define variables in python

my_var1 = "This is my first variable"  # string assign into variable name my_var1
print(my_var1)

my_var2 = 20;   # this is integer assign into variable name my_var2
print(my_var2)

my_var3 = 30.4   # this is double assign into variable name my_var3
print(my_var3)

my_var4 = 10/3
print(my_var4)

my_var5 = 4
my_var6 = 6
print(my_var5 + my_var6)

my_var7 = True  # this is boolean assign into variable name my_var7
print(my_var7)

# Local and Global Variable

my_global_var1 = "This is global variable."
print(my_global_var1)


def example():
    # Here I am define local variable
    my_local_var1 = "This is my local variable"
    print(my_local_var1)
    print(my_global_var1)

# Here I am calling this method or function
example()

x = 6

def example2():
    # what we do here is defined x as a global variable now we can tell
    # that x is global other wise UnboundLocalError: local variable 'x' referenced before assignment:.
    global x
    print(x)
    x+=5
    print(x)
    x = 13    # Here x is treating as a local variable
    x+=5
    print(x)

example2()