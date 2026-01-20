print(type(10))
print(type(1+3j))
print(type('Priyanka'))
print(type (3.14))
print(type({'name':"Priyanka",'age':42}))
print(type([1,3,3]))
print(type(True))
print(type((0,1,2,3))) # immutable
#We can change tuples to lists and lists to tuples. 
# Tuple is immutable if we want to modify a tuple we should change it to a list.

# Syntax
tpl = ('item1', 'item2', 'item3','item4')
tpl2 =('apple','banna','mango')
#lst = list(tpl)
#checking an Item in a Tuple
print('item' in tpl) # False 
print('item2' in tpl) # True
print(tpl+tpl2)


a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
print("first value ",a)
print("second value ",b)
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b 
 #rounds the result down to the nearest whole integer (towards negative infinity)
floor_division1=-7//2
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function -
#  try to avoid overriding built-in functions


print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b  & -7//2 = ', floor_division,' ',floor_division1)
print('a ** b = ', exponential)


# Comparison Operators**
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango'))
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

"""In addition to the above comparison operator Python uses:

- _is_: Returns true if both variables are the same object(x is y)
- _is not_: Returns true if both variables are not the same object(x is not y)
- _in_: Returns True if the queried list contains a certain item(x in y)
- _not in_: Returns True if the queried list doesn't have a certain item(x not in y)"""

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B not in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True



print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

#And function
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)

#or function
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)

#not function
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# String 
#Multiline string is created by using triple single (''') or triple double quotes ("""). See the example below.


multiline_string1 = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string1)


# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)


print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash


#### New Style String Formatting (str.format)

#This format was introduced in Python version 3.



first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}.\nI teach {}.\n'.format(first_name, last_name, language)
print(formated_string)


a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))


print ("""XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        START of LOOP 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        START of CONCEPT of LOOP
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        """)

#print("Udemy")
output =[]
input='udemy'
for i in input :
    output.append(i)
print(output)


# by using list comprehension
print(".................")
input="udemy"
output=[i for i in input]
print (output)

# add to numbe in list
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#x=list(input())
x=[1,2,3,4,5]
#print(x)
y=[i+100 for i in x]
print(y)
#[expression loop condition]

#print even number
 # to generate even numbers list in range 0 to 21clear
even_numbers = [i for i in range(21) if i % 2 == 0] 
print(even_numbers) 


# odd number
odd_number = [i for i in range(50) if i % 2 != 0]
print(odd_number)

#5 [1,2,3,4,5]
x = range(6)
for i in x:
    print(i)

#add in one line
total=[i+i for i in range(6)]
print(total)

for i in range(10):
   print(i)

print("XXXXXX1XXXXX")
#just on parameter
total=0
for i in range(10):
  total=i+i
print(total)  

print("XXXXXX2XXXXX")
#just on parameter
total=0
for i in range(10):
  total=total+i
print(total)  


print ("""XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        START of FUNCTIOn
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        START of CONCEPT of LOOPFunction
       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        """)


#function without parameter
print("function parameter")


# function without parameter 
def function_name():
    print("code") 
 #calling function
function_name()

# adding number
def add_two_number():
    x=2
    y=3
    add=x+y
    print(add)
add_two_number() 

### Function with Parameters

#In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as parameters.

def name(surname):
    name="priyanka"
    fullname = name + "  " + surname
    return fullname
print(name("nathawat"))

# squre of number
def sqaure_number(number):
    result= number*number
    return result
print (sqaure_number(3))

# area of circle 

def circle_area(radius):
    area=2*3.14*radius
    return area
print(circle_area(4))

#addition of series 

#just on parameter
total=0
for i in range(11):
  total=i+i
print(total)

#n is first 10 numner not incliding ZERO
def addition_Series(n):
    total=0
    for i in range(n+1):
        total=total+i
    return total
print(addition_Series(10))


def even_odd_number(num):
    if num % 2 ==0:
        return 'even number'
    else:
        return "odd"
    
result =even_odd_number(22)
print(result)

#Two Parameter: A function may or may not have a parameter or parameters.
#A function may also have two or more parameters.
#  If our function takes parameters we should call it with arguments. Let us check a function with two parameters:
from datetime import date
def person_age(birth_year,curent_year):
    curent_age= curent_year-birth_year
    return curent_age
print(person_age(1984,curent_year=date.today().year)) 
#datetime.now().year

def generate_full_name (first_name, last_name='Nathawat'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name('Asabeneh'))

"""
SyntaxError: parameter without a default follows parameter with a default
1st value default then all rest has to be default
def generate_full_name (first_name="Priyanka", last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name('NAthawat'))
"""



