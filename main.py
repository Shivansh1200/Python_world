'''# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

'''
#1. sum of 2 variables
from numpy import sort
from numpy.core.defchararray import upper, lower


first=230
second=250
sum=first+second
print('sum of above variable is:',sum)
if sum==460:
    print("sum of first and second is correct")
elif sum<460:
    print(False)
else:
    print('sum is greater than the sum of first and second')


#2 .using user input
number1=int(input('ur first no:'))
number2=int(input('ur second number:'))
sum=number1+number2
print(sum)


#program for SI
p=3000
r=7
t=1
si= int((p*r*t)/100)
print(si)


# pgm for CI.
p=input(input())
r=2
n=1
a=p(1+(r*n)/100)
print(a)
ci=a-p
print(ci)
   #or
def _compound_interest(principal, rate, time):
    ammount=principal*((1+rate/100)**time)
    ci=ammount-principal
    print('compound_interest is: ',ci)
_compound_interest(10000, 10.25,5)


#find the area of the circle
def _area_of_circle(radius):
    pie=3.14
    area=pie*(radius)**2
    print(area)
_area_of_circle(5)


# find area of square
def _area_of_square(side):
    area=side**2
    print('area of the given square:', area)
_area_of_square(5)


# area of rectangle
def _area_of_rectangle(l,b):
    area=l*b
    print(area)
_area_of_rectangle(2,4)


# area of triangle
def _area_of_triangle(base, height):
    area=1/2*(base*height)
    print(area)
_area_of_triangle(10,2)


#type conversion in strings
def strings():
    string='Geeksforgeeks'
    print(upper(string))
    print(lower(string))
strings()


#programs for finding maximum of two numbers
def maximum(num1, num2):
    if num1>num2:
        print('maximum number is:', num1)
    elif num2>num1:
        print('maximum no is:', num2)
    else:
        print('entered numbers are equal')
maximum(60,60)


# greater among 3 numbers
def greater_in3(num1,num2, num3):
    if num1>num2 and num1>num3:
        print('num1 is greatest ')
    elif num2>num3 and num2>num1:
        print('num2 is greatest')
    else:
        print('num3 is grater than num2')
greater_in3(10,82,44)


#string
string='welcome to world of programming'
print(string)


#decimal and integer effect in numbers
print(8/2)
print(8//2)
#for finding reminder in devision of 2 numbers
print(10%3)

name='Shivansh'
print("hi "+name, 'welcome to the world of programming!!')

print("Shivansh's laptop")
print('Shivansh\'s laptop')
print(10*'shivtechviral')


# \n for newline
print('C:\docs\nhivansh')


#rawstring concept (i.e. you want to print the exact text with no effect of any special keyword
print(r'C:\doc\'s altair')


# finding the length of the strings
strings='hellow_buddies'
print(len(strings))
#
import math
list=[10,30,60,90,70,88]
#
list.append(333)
print(list)
sum=list.sum()
print(sum)

# insert()
list.insert(66)
print(list)

# extend()
list.extend([2,66,3])
print(list)
# sum()
list.sum()
print(list)
# pop()
list.pop(2)
print(list)

# sort()
list.sort()
print(list)
#
list.clear()
print(list)

# remove()
list.remove(10)
print(list)
#
user_input=input('enter user\'s choice')
print('user_input', user_input)

# tuple
tuple=(20,60,99,85)
print(tuple.index)
# finding helps
help()

#cheking the id or address of the variable
num=255
num2=25
print(id(num))
print(id(num2))

#"buggs are horrifying"

# complex datatype
a=6+3j
print(type(a))

#program to printing series from 1 to 30
for i in range(1,100,10):
    print(i)

# program to find if entered no. is prime or not?
number=int(input('Enter any number to be verified as prime:'))
if number %2==0:
    print("prime")
else:
    print('not a prime no.')
#program to find out the square root of a entered no
num=int(input('enter no.:'))
num_sqrt=(num**(1/2))
print(int(num_sqrt))


#swapping of 2 nos.
a=20
b=25
temp=a
a=b
b=temp
print(b,a)

#    OR
x=2
y=3
x,y=y,x
print(x, y)


# program for finding the year is leap or not
year=int(input('enter any year in format as ____ :'))
if year %4==0 and year %100==0 and year%400 ==0:
    print('entered year is a leap year')
elif year%4!=0:
    print('entered year isn\'t a leap year' )
else:
    print('entered year isn\'t leap year')

             # OR
year=int(input('enter any year:'))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("entered year is a leap year")
        else:
            print('entered year isn\'t a leap year')
    else:
        print('entered year a leap year')
else:
    print('isn\'t a leap year')

# display a calender

import calendar
yy=int(input('enter any year: '))
mm=int(input('enter month:'))
print(calendar.month(yy,mm))

#solution of a quadratic equation : ax**2+b*x+c=0
a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))
#d=((b**2)-4*(a*c))
#print('d is equals to : ',d)
# OR ( using inbuilt functions()
import cmath
d=(b**2)-(4*a*c)
solution1=(-b+cmath.sqrt(d))/(2*a)
solution2=(-b-cmath.sqrt(d))/(2*a)
print('the solution are {0} and {1}'.format(solution1, solution2))


# sum of natural no. upto no.
num=int(input('enter a number:'))
if num<1:
    print('enter a positive no:')
else:
    sum=0
    while num>0:
        sum+=num
        num-=1
        print('sum of numbers are:',sum)


# factorial of a given no.
um=int(input('enter a no.:'))
factorial=1
if num<0:
    print('factorial of a negative no. isn\'t exists!!')
elif num==0:
    print('factorial of 0 is : 1')
else:
    for i in range(1,num+1):
        factorial=factorial*i
        print('factorial of the given no:',num +'is:', factorial)


# Armstrong  numbers
num=int(input('enter a no>:'))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//10
    if num==sum:
        print('num is a armstrong no.')
    else:
        print('entered no isn\'t an armstrong no')


# check if a no. is +ve or -ve or 0
def num():
    number=int(input('enter any no:'))
    if number>0:
        print('entered no. is +ve')
    elif number==0:
        print('entered no. is = 0')
    else:
     print('entered no. negative')
num()


#Factorial of a no. using recursion
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
f=factorial(5)
print(f)


# palindrome no checking
s=input('enter any string:')
if s==s[len(s)::-1]:
    print('entered string is a palindrome')
else:
    print('entered string isn\'t a palindrome')


# entered chacter is a alphabet or not?
ch=input('enter any character:')
if ((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print('entered chacter is a alphabet')
else:
    print('entered chacter isn\'t an alphabet')


# check entered no. is even or odd ??
num=int(input('enter a no:'))
flag=num%2
if flag==0:
    print('entered no. is even')
elif flag==1:
    print('entered no. is odd')
else:
    print('INVALID NO.')


#check if entered charater is a vovel or consonent ?
ch=input('enter any character:')
if (ch=='a' or ch=='A' or ch=='e' or ch=='E'or ch=='i' or
        ch=='I'or ch=='o' or ch=='O'or ch=='u' or ch=='U'):
    print('entered character is a vovel')
else:
    print('entered character is a CONSONENT')

# converting decimal no. into binary using bin()
no=int(input('enter no:'))
print(bin(no))

#array creation in python ,  The letter d is a type code.
# This determines the type of the array during creation.
import array as arr
a=arr.array('d', [2.2, 3.6, 9.3, 7.1])
print(a)

# Enter number of terms needed                   #0,1,1,2,3,5....
a=int(input("Enter the terms"))
f=0                                         #first element of series
s=1                                         #second element of series
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next

























