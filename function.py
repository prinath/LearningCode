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