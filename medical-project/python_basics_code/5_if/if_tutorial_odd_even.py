n = input("Enter a number: ")
n = int(n)

if n % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

print("Now printing the answer using ternary operator")

message = "Number is even" if n % 2 == 0 else "Number is odd"
print(message)