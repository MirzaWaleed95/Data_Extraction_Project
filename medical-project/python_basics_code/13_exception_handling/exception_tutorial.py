x = input("Enter number 1: ")
y = input("Enter number 2: ")

try:
    z = int(x) / int(y)
    a = 'baby yoda' + 56
except ZeroDivisionError as ze:
    print("Exception occured: ",ze)
    z = 0
except TypeError as te:
    print("Exception occured: ", te)
    z = 0
except Exception as e:
    print("Generic exception occured: ",e`)
    z = 0

print("division is: ",z)
