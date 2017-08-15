# Let's check the first if and else condition

x = 10
y = 20
z = 30

if x > y:
    print(x + " is greater than " +y)
    # this line is not executing that why it is not giving error.
    # Otherwise it gives this error TypeError: unsupported operand type(s) for +: 'int' and 'str'
else: pass   # this will pass without any thing print

# another example

if x > y:
    print(str(x)+ " is greater than " + str(y))  # Here we need to type cast int to string.
else:
    print(str(y) + " is greater than " + str(x))


# another example

if x > y & x > z:
    print(str(x) + " is the greatest number")
elif y > x & y > z:
    print(str(y) + " is the greatest number")
else:
    print(str(z) + " is the greatest number")


# Let's check the loop condition

print("********While loop test**********")
x = 1
while x < 5:
    print(x)
    x += 1

print("********For loop test**********")
list = [1, 2, 3, 4, 5]
for x in list:
    print(x)


print("********For loop range test**********")
for x in range(1,5):
    print(x)