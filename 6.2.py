print("Expression: y > a + b or c. Determine values for a, b, c, and y to make the expression true.")

a= input("Enter value for a: ")
a = int(a)
b = input("Enter value for b: ")
b = int(b)
c = input("Enter value for c: ")
c = int(c)
y = input("Enter value for y: ")
y = int(y)

if y > (a + b) or c == True:
    print("Correct")
else:
    print("Incorrect")