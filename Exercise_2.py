'''6. Write a program to take two numbers from the user and perform all arithmetic operations (addition, subtraction, multiplication, division, modulus, floor division, exponentiation) on them.
'''

# num1=int(input("Enter Number : "))
# num2=int(input("Enter Number : "))



# print(f"Addition of {num1} and {num2} is {num1+num2}")

# print(f"Subtraction of {num1} and {num2} is {num1-num2}")

# print(f"Multiplication of {num1} and {num2} is {num1*num2}")

# print(f"Division of {num1} and {num2} is {num1/num2}")

# print(f"Modulus of {num1} and {num2} is {num1%num2}")

# print(f"Floor Division of {num1} and {num2} is {num1//num2}")

# print(f"Exponentiation of {num1} and {num2} is {num1**num2} \n\n\n")



'''7. Write a program to check:
Whether a given element is in the list or not (membership)
Whether two variables are referring to the same object (identity)
'''

# lst=[2,4,6,32,5,66,3,21,34,56,23,72]
# num=int(input("Enter number to find in list "))

# ans="Number is present in list" if num in lst else "Number is not in list\n\n\n"
# print(ans)

# obj1="Hello My name is Raj"
# obj2="Hello My name is Raj"

# print(obj1 == obj2)
# print(obj1 is obj2)


'''8. Given a list: numbers = [10, 20, 30, 40, 50]
Print:
First three elements
Reverse the list
Replace 2nd element with 25
'''

# numbers = [10, 20, 30, 40, 50]

# print(numbers[:3])

# numbers[1]=25
# print(numbers)

# numbers.reverse()
# print(numbers)


'''9.Count Frequency of Elements in a List
Input: [1, 2, 2, 3, 3, 3, 4]
	Output: {1:1, 2:2, 3:3, 4:1}
'''
inpt_lst=[1,3,4,5,4,2,6,4,2]


dic={x:inpt_lst.count(x) for x in inpt_lst}
print(dic)


'''10. Write a program to take two sets and:
Find common elements
Find elements only in the first set
Combine both sets (union)
'''

set1={2,5,3,6,8,54,12}
set2={2,53,43,65,8,54,12}

print("Common elements are ",set1.intersection(set2))

print("Elements are only in first set are", set1.difference(set2))

print("Union is ",set1.union(set2))




'''Find Unique Words from a Sentence
Input: "python is fun and python is powerful"
Output: {'fun', 'powerful', 'and'}
(Hint: Use sets and string methods)
'''

str="python is fun and python is powerful"

str=str.split()



# ans=[]

# for i in str:
#     if not str.count(i) > 1:
#         ans.append(i)

print({i for i in str if not str.count(i) > 1})



'''12. Dictionary Merge with Value Sum Given:
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 100, 'd': 400}
Output: {'a': 400, 'b': 300, 'c': 300, 'd': 400}
'''

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 100, 'd': 400}








