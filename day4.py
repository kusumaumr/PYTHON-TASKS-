# assignment operators
x=10
y=3
x+=y
print(x)#x=x+y 13
x-=y
print(x)#x=x-y 10
x*=y
print(x)#x=x*y 30
x/=y
print(x)#x=x/y 10.0
x//=y
print(x)#x=x//y 3.0
x%=y
print(x)#x=x%y 1.0
y**=x
print(y)#y=y**x 3.0^1.0 3.0
#relational operators
a=20
b=30
c=19
print(a==b)# False
print(a!=b)# True
print(a>=b)# False
print(a<=b)# True
print(a>b)# False
print(a<b)# True
print(a<b>c)# False
#logic operatons  ->compareing two or more conditions there are three types of logic operations and they are and,or,not
x=10
y=20
z=5
#and -> if all the conditions are true then only it will return true otherwise it will return false\#or -> if any one of the condtion is true then it will return true otherwise it will return false
#and -> if the condition is true then it will return false full statement will be false
print((x>y) and (y>z) and (z>x)) #True
#true and true and true ->true
print((x<y) and (y<z) and (z<x)) 
print(not(x>y)) #not(true) not(1)->0
#or -> if any one of the condtion is true then it will return true otherwise it will return false
print((x>y) or (y>x)) #true 
#not -> it is used to reverse the result of the condition if the condition is true then it will return false and if the condition is false then it will return true
print(not(x>y)) #not(true) not(1)->0
print(not(x<y)) #not(false) not(0)->1
#practice all bitwise operators
print(2&3)
print(10&5)
print(10|5)
print(7^1)
a=10
print(a<<1)
print(a<<2)
print(a>>1)
print(a>>5)
b=-10
print(~b)
c=5
print(~c)

#day5
#bitwise operators -> it is used to perform bitwise operations on the binary representation of the numbers
#& -> it is used to perform bitwise and operation on the binary representation of the numbers
#| -> it is used to perform bitwise or operation on the binary representation of the numbers
#^ -> it is used to perform bitwise xor operation on the binary representation of the numbers




#~ -> it is used to perform bitwise not operation on the binary representation of the numbers
#<< -> it is used to perform bitwise left shift operation on the binary representation of the numbers
#>> -> it is used to perform bitwise right shift operation on the binary representation of the numbers
