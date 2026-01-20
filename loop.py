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
