#1.print given values is positive or negative only if else condition use
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

            #or

x= float(input("Enter a number: "))
if x > 0:
    print(x,"is positive.")
else:
    print(x,"is negative.")
# 2.given char(A) is upper case or lower case(without using bulidin function)
char = input("Enter a character: ")
if 'A' <= char <= 'Z':
    print( char," is uppercase.")
else:
    print(char," is lowercase.")

# #pass or fail(have 6 subjects) and condition use
telugu=int(input("enter the marks of telugu:"))
english=int(input("enter the marks of english:"))
m1=int(input("enter the marks of m1:"))
m2=int(input("enter the marks of m2:"))
physics=int(input("enter the marks of physics:"))
chemistry=int(input("enter the marks of chemistry:"))
if (telugu>=35 and english>=35 and m1>=28 and m2>=28 and physics>=28 and chemistry>=28):
    print("pass")
else:    
    print("fail")


