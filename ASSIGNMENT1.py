#check whether number is positive or negative
num=7
if num>0:
    print("number is positive")
else:
    print("number is negative")
#even or odd
    no=int(input("enter number"))
    if no%2==0:
        print("number is even")
    else:
        print("number is odd")

#find greater number between two numbers
a=int(input("enter value of a"))
b=int(input("enter value of b"))
if a>b:
    print("a is greater")
else:
    print("b is greater")
#person is eligible to vote
age=int(input("enter your age"))
if age>18:
    print("eligible to vote")
else:
    print("not eligible to vote")

#number is divisible by 5
n=int(input("enter number"))
if n%5==0:
    print("divisible by 5") #basic division
else:
    print("not divisible by 5")

#check whether given year is leap year or not
year=int(input("enter year"))
if year%400==0 or year%100!=0:
    print("it is leap year")
else:
    print("it si not leap year")

#check whether it is vowel or consonant
ch=input("enter character")
if ch=='a'or ch=='e' or ch=='i'or ch=='o'or ch=='u':
    print("it is vowel")
else:
    print("it is consonant")

#largest among three numbers
d=10
e=9
f=89
if d>e and d>f:
    print("d is greater ",d)
elif e>d and e>f:
    print("e is greater ",e)
else:
    print("f is greater",f)

#assign grades based on marks
marks=int(input("enter your marks"))
if marks>90:
    print("A grade")
elif marks>=75 and marks<=85:
    print(" B grade")
elif marks>=50 and marks <=74:
    print("C grade")
elif marks<50:
    print("fail")

#number is within range of 1 to 100
number=int(input("enter the number"))
if(number>=1 and number<=100):
    print("number is within range")
else:
    print("number is not within range")

#for loop programs

#print number from 1 to 10
for i in range(1,11):

    print(i)

#reverse order
for i in range(11,0,-1):
    print(i)

    #print even number between 1 to 2o
for i in range(1,21):
    if i%2==0:
        print(i)

#print odd numbers between 1 and 20
for i in range(1,21):
    if i%2==1:
        print("odd no=",i)

 #find the sum of numbers from 1 to 100
sum=0
for i in range(1,101):
    sum=sum+i
print("sum=",sum)


#print multiplication of given number
no=int(input("enter number"))
for i in range (1,11):
    print("mul=",no*i)

#nested loop to print pattern
for i in range(1,6):
    for j in range(i):
      print("*",end=" ")
    print()

#print each character of string
song="sonia"
for i in song:
    print(i)

 #print factorial of given number
fact=1
for i in range(1,10):
    fact=fact*i
    print("fact=",fact)

#print the following pattern
    for i in range(6,0,-1):
     for j in range(i):
        print("*",end=" ")
    print()
    
#while loop programs

#print number from 1 to 10
i=1
while i in range(1,11):
    print("value of i:",i)
    i=i+1

#reverse order from 10 to 1
i=10
while i>=1:
    print("i=",i)
    i=i-1

#print even number between 1 and 20
i=1
while i in range(1,21):
    if i%2==0:
        print("even no=",i)
    i=i+1

#print odd numbers between 1 and 20
i=1
while i in range(1,21):
    if i%2!=0:
        print("odd no:",i)
    i=i+1

#sum of numbers from 1 to 100
i=1
sum=0
while i in range(1,101):
  sum=sum+i
print("sum=",sum)

#multiplication of given number
i=1
no=6
while i<=100:
    print("mul=",no*i)
    i=i+1

#count the number of digits in a given number
num=int(input("enter a number:"))
count=0
while num>0:
    num=num//10
    count=count+1
print("number of digits is:",count)

#reverse a number
no=int(input("enter a no"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("reversed number=",rev)

#find factorial of number
b=int(input("enter value of a"))
fact=1
i=1
while i<=b:
    fact=fact*i
    i=i+1
print("factorial of given number:",fact)

#ask for password until correct
correct_password="abc"

while True:
    password=input("enter password")
    
    if password==correct_password:
        print("login successful")
        break
    else:
        print("unsuccesful")