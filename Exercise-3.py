'''13. Write a program that takes two numbers as input and divides them. If the denominator is zero, print "Cannot divide by zero!".'''


# inpt1=int(input("Enter first number to divide "))
# inpt2=int(input("Enter second number to divide "))



# try:
#         ans=inpt1/inpt2
#         print("Ans is ",ans)
# except:
#     print("Cannot divide by zero!")



'''14. Take user input and convert it to integer. If the input is not a number, display "Invalid input!". If the number is negative, raise a ValueError.
'''





# try:
#     uinpt1=int(input("Enter first number "))
#     uinpt2=int(input("Enter second number "))
#     print(f"You enter {uinpt1} and {uinpt2}")

# except:
#     print("Invalid input!")


'''15. 
Write a program that prints the current date and time in the format: DD-MM-YYYY HH:MM:SS.
'''

import datetime as dt
# t=dt.datetime().now()
# print(t.date())


# -----------------------------------------------------------------

'''16. Take a date of birth as input in YYYY-MM-DD format and calculate the age in years.
'''

# dob=input('Enter dateof birt in YYYY-MM-DD format ')


# formatt="%Y-%m-%d"
# obj=dt.datetime.strptime(dob,formatt)

# crnt=dt.date.today()
# print(crnt)

# obj=obj.year
# crnt=crnt.year

# print(f"Your age is {crnt-obj}")




'''17. Create a dictionary with name, age, and city. Convert it to JSON format.
'''

# dict={'name':'Raj','age':22,'city':'rajkot'}

# import json

# a=json.dumps(dict)

# print(type(a))


'''18. Load the JSON string below into a Python dictionary and print the value of city.
'''

# dict=json.loads(a)

# print(dict["city"])


'''19. Write a program to read numbers from a text file and calculate their sum. If the file does not exist, create it and ask the user to enter numbers (comma-separated). Handle all exceptions gracefully.'''







try:
        
    a=0
    with open("file.txt",'r') as f:
        a=f.read()
        a=a.split(",")

    ans=0
    for i in a:
        ans = ans+int(i)

    print("Nmber of sum is ",ans)

except:
    txtt=input("Enter numbers and separate with comma ")
    with open("file.txt",'w') as f:
        f.write(txtt)

    a=0
    with open("file.txt",'r') as f:
        a=f.read()
        a=a.split(",")

    ans=0
    for i in a:
        ans = ans+int(i)

    print("Nmber of sum is ",ans)
















      




