
# sum of digits

n=1234
sum=0
while n>0:
    temp=n%10
    sum+=temp
    n//=10
print(sum)
# output:10
# reverse numbers

n=1234
reverse=0
while n>0:
    temp=n%10
    reverse=reverse*10+temp
    n//=10
print(reverse)
# output:4321
# count digits in a number

n=12345
count=0
while n!=0:
    n//=10
    count+=1
print(count)
#output:5
# check even or odd

n=17
if n%2==0:
    print("Even")
else:
    print("Odd")
#output:Odd
# check prime number

n=13
if n>1:
 for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        print("prime")
else:
    print("not prime")
#output
# prime
# prime
# prime
# prime
# prime
# prime
# prime
# prime
# prime
# prime
# prime
# find factorial of a number

n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
# output:120
# find factors of a number

n=12
for i in range(1,n+1):
    if n%i==0:
        print(i)
#output:
# 1
# 2
# 3
# 4
# 6
# 12
# check palindrome number

n=121
rem,rev=0,0
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
if rev==temp:
    print("palindrome")
else:
    print("not palindrome")
# output:palindrome
# check armstrong number

n=153
temp=n
sum=0
while n>0:
    rem=n%10
    sum+=rem**3
    n//=10
if sum==temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# output:Armstrong number
# find GCD(HCF) of two numbers

a=12
b=18
while b!=0:
    a,b=b,a%b
print("GCD is",a)
# output:GCD is 6