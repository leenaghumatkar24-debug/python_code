#write a function to check whether the number is positive or negative
"""def demo():
    a=int(input("enter value of a"))
    if a>0:
        print("no is positive")
    else:
        print("no is negative")
demo()"""  

#check number is even or odd
def even_odd():
 no=int(input("enter number"))
 if no%2==0:
       print("number is even")
 else:
    print("number is odd")
even_odd() 

#write a function that accepts two numbers and return greater number
def greater_number(a,b):
   if a>b:
      return a
   else:
      return b
greater_number(10,20)

#whether the person is eligible to vote (age>18)
def eligible_to_vote(age ):
   if age>18:
      print("eligible to vote:",age)
   else:
      print("not eligible to vote:",age)
eligible_to_vote(20)

#check whether a number is divisible by 5
def number(no):
   if no%5==0:
      print("no is divisible by 5")
   else:
      print("no is not divisible by 5")
a=int(input("enter number"))
number(a)

#write a function to check whether the given number is a leap year or not
def leap_year(year):
   if year%400==0:
      print("it is leap year")
   else:
      print("it is leap year")
leap_year(2000)

#check whether a character is vowel or consonant
def vowel_consonant(ch):
   if ch=='A'or ch=='E' or ch=='I' or ch=='O' or ch=='U':
      print("it is vowel")
   else:
      print("it is consonant")
c=input("enter character")
vowel_consonant(c)

#find largest among three
def largest_number(a,b,c):
   if a>b and a>c:
      print("a is greater")
   elif b>a and b>c:
      print("b is greater")
   else:
      print("c is greater")
    
#calculate the sum of numbers from 1 to 100
def sum():
   s=0
   for i in range(1,101):
    s=s+i
   print("sum of numbers=",s)  
sum()   

#multiplication of given number
def multiplication(no):
   for i in range(1,11):
      print(no*i)
multiplication(5)

#calculate and return the square of number
def Square(num):
   res=num*num
   print(res)
Square(2)

#calculate factorial of given number

def factorial():
   fact=1
   i=1
   for i in range(1,11):
    fact=fact*i
    print("factorial number:",fact)
factorial()

#check whether given number is prime or not
def prime(no):
   if no>1:
      for i in range(2,no):
         if no%1==0:
            print("it is not prime number")
            break;
         else:
           print("it is prime number",no)
   else:
      print("it is not prime number",no)
a=int(input("enter no"))
prime(a)

#calculate sum of digit of a number
def sum_of_digit(no):
   

      
          
   

