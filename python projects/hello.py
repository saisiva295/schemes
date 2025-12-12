'''
python
data types
variables
operators
type casting
coditional statements
arrays
functions
file handling 
exception handling

python is a interpreted high level programing language which is used to develop the applications
features
1.simple syntax
2. easy to understand
3.interpreted
4. high level language
5. more libraries
6.oops
#DATA TYPES
NUMERIC---int float complex
SEQUENCE--- list tuple string range
SET------- set frozen set
MAP--- dictionary
BOOLEAN--- bool--(true/false)

#numeric
#int-- only numbers
#example
a=10
b=20
c=3.89
print(a,b,c)
d=int(input("enter a number:"))
print(d)
print(a,b,c,d)
print(type(a))
print(type(b))
print(type(c))

a=2+5j
print(a)
print(type(a))
a=True
print(a)
print(type(a))
#list
a=[1,2,3,4,4,4,'sai',3,56,'True','siva']
print(a)
print(type(a))
print(a.append(20))
print(a)
list functions
list methods

#list functions

len
append
insert
count
index
sort
reverese
pop
a=[10,20,30,40,50,60,70,80,90,100,100,100]
print(a)
print(len(a))
print(type(a))
print(a.append('siva'))
print(a.pop())
print(a.pop())
print(a)
print(a.append('siva'))
print(a)
print(a.insert(2,1000))
print(a)
print(a.count(100))
print(a)'''
'''
a=[10,4,5,7,89,4,5,77,2,1]
print(a.sort())
print(a)
for a in range(5):
    print("sivayya")
    '''
#operators
'''
airtmetic operator
relational
assignment
logical operator
bitwise
membership
identity 
'''
#arithemetic operator
#Write a program to add two numbers using the + operator.
'''
num1=20
num2=30
num3=num1+num2
print(num3)'''
#Take two integers from the user and print which one is greater using comparison operators (>, <, ==)
'''
a=int(input("Enter first number:"))
b=int(input("Enter your second number:"))
if(a>b):
    print("a is greater number than b")
elif(a<b):
    print("b is greater than a")
else:
    print("both are equal")
'''
#Check if a number is even using the modulus operator %.
'''
n=35
if n%2==0:
    print("even")
else:
    print("not even")
    '''
#Write a program to swap two numbers using assignment operators.
'''
a=10
b=22
print("before swapping:",a ,b)
print("After swapping:",a,b)
print(a,b=b,a)
print()
'''

'''
import array
array.typecodes
print(array.typecode..

arr=array('i',[1,2,3,4,5])
print(arr)'''
'''
#Print all elements of an array
import array
arr=array.array('i',[10,20,30,40,50])
print(arr)
print(arr.tolist())
print(arr)'''
'''
#Find the sum of all elements
import array
arr=array.array('i',[10,20,30,40])
print(sum(arr))
print(arr)
#Find the largest element in an array
import array
arr=array.array('i',[20,30,57,50,38])
print(max(arr))
print(min(arr))
#print(add(max)+add(min))
print(max(arr)+min(arr))'''


'''
✅ Level 1: Very Easy (Start Here)

Print all elements of an array

Find the sum of all elements

Find the largest element in an array

Find the smallest element in an array

Count how many even and odd numbers are in the array

Search for a given number in the array (Linear Search)

✅ Level 2: Easy

Reverse an array without using built-in functions

Find the second largest element

Find the second smallest element

Copy elements from one array to another

Count frequency of each element

Check if an array is sorted or not

✅ Level 3: Medium

Move all zeroes to the end

Remove duplicates from the array

Find the first repeating element

Find the first non-repeating element

Pair sum problem: Find pairs whose sum equals a target

Rotate array by k positions

Find missing number in an array of 1 to n

Find the element with the highest frequency
'''
#Count how many even and odd numbers are in the array

'''
import array
arr=array.array('i',[1,2,3,4,5,6,7,8,9,10])
for num in arr:
    if num%2==0:
        print("The even numbers are:",num)
    else:
        print("The odd numbers are:",num)
'''
'''
#Count how many vowels are in a string.     #vowels===a,e,i,o,u
a="saisiva"
vowels="A,E,I,O,U"
count=0
if(vowels==a):
    print("vowels are:")
    count+1
    print()'''

'''
✅ Indexing – Small Logical Questions

Print the second and second last character of a string.

Check if the first character and last character are the same.

Given a string, print characters at even index positions only.

Given a string, print characters at odd index positions only.

Print the character at index 3, but only if it exists.

Given a string, form a new string using first, middle, and last characters.

Swap the first 2 characters with the last 2 characters.

Extract the character exactly in the middle of the string (if length is odd).

✅ Slicing – Small Logical Questions

Print the string without its first and last character.

Print the first 3 characters and the last 3 characters.

Reverse the string using slicing.

Print the string in steps of 2 (every alternate character).

Use slicing to remove the last 5 characters.

Slice the string from index 2 to index -2.

Given a string, extract the first half of it.

Extract the second half of the string.

✅ String Methods – Small Logical Questions

Count how many times "a" appears using a method.

Check if the string starts with "py" (any case).

Convert the string to uppercase and check if contains "ABC".

Remove extra spaces at start and end, then print length.

Replace all vowels with "*".

Split the sentence into words and print the longest word.

Check if all characters are alphabets.

Make the string title case ("hello world" → "Hello World")
'''
#Print the second and second last character of a string.
'''
a='hello my name is sai siva'
print(a[1::2])
print(a[-1:-24:])'''
#Check if the first character and last character are the same.
'''
a='helloiamsiva'
print(a.startswith(a[0]))
print(a.endswith(a[-1]))
if(a[0],a[-1]):
    print("same")
else:
    print("not same")'''
#Given a string, print characters at even index positions and odd index positions only.
'''
a='saisivagoodboy'
print(len(a))
print("even places are:",a[0:15:2])
print("odd places are:",a[1:15:2])'''
#Print the character at index 3, but only if it exists.
'''
text = "Hello"

if len(text) > 3:   # ensures index 3 exists
    print(text[3])  # prints 'l'
else:
    print("No character at index 3")'''
#Given a string, form a new string using first, middle, and last characters.
s='hello sai siva'
print(s[1])
print(s[-1])
print(s//2)
print('has')



