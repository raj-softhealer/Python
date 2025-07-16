'''1. Write a program to declare three variables — a name (str), age (int), and height (float) — and print them using formatted string output.
Example Output:
Name: John, Age: 25, Height: 5.9
'''

name="Raj"
age=22
height=5.9

print(f"Name: {name}, Age: {age}, Height: {height}")



'''2. Create two variables, one integer and one string representing a number (e.g. "10"). Convert the string to int and add both variables. Print the result.
'''

a=5
b="20"

print(f"Answer of sum is {a+int(b)}")


'''3. Create three variables: x = 5, y = 5.0, z = "5". Use isinstance() to check the type of each and print results.
'''

x=5
y=5.0
z="5"

print(isinstance(x,int))
print(isinstance(y,int))
print(isinstance(z,str))


'''4. Assign values to multiple variables in a single line (name, city, age) and print them.
'''

name,city,age="Raj","Rajkot",22

print(f"Name: {name}, City: {city}, Age: {age}")


'''5.Swap Values Without Using a Temporary Variable
 Take two integer inputs and swap their values without using a third variable.
'''

a=5
b=2

a,b=b,a

print("a =",a, ", b=" , b)