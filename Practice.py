# 1. remove duplicates from list without using set()


# a=["parle","amul","mahi","parle",'amul']

# final=[]

# for i in a:
#     if i not in final:
#         final.append(i)

# print(final)


#2. find the intersection of two list

# a=["parle","amul","mahi","parle",'amul']
# b=['amul','britania',"mahi",'gopal']

# ans=[]
# for i in a:
#     if (i in b) and (i not in ans):
#         ans.append(i)

# print(ans)



#3. find the pairs in list whose sum is equal to a given number

# a=[1,2,3,4,5,6,7,8,9]

# num=int(input("Enter a number"))

# for i in a:
#     for j in a:
#         if (i+j) == num:
#             print(f"{i} + {j} = {num}")



#4. remove duplicate from the list 

# a=[6,6,5,3,2,7,8,9,6,3,7]

# for i in range(len(a)):
#     for j in range(i,len(a)):
#         # print(a[j],end=" ")
#         if a[i] == a[j]:
#             # del a[j]
#             a.pop(j)
#             # break

# print(a)



#5. sort a list without using sort() 

# l=[5,4,3,6,4,7,5,4,2,1,7,9,1,4,6,7]

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i] > l[j]:
#             print(l[i],l[j])
#             l[i],l[j] = l[j],l[i]
#             print(l[i],l[j])
            
# print(l)



#6. sort the list of tuple based on second element of tuple

# lst=[(4,1),(5,5),(4,2),(8,4),(9,3)]

# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i][1] > lst[j][1]:
#             lst[i],lst[j] = lst[j],lst[i]

# print(lst)



# reverse the words in a sentence(without using split() and reverse() )
# input: "python is super fun"
#output: "fun super is python"


# strr = "python is super fun"

# for i in strr:
#     if strr == " ":




#input aabbbccccddddd
# output: a2b3c4d5

a="aabbbccccdddddd"
ans=""
for i in a:
    b=str(a.count(i))
    if (i+b) not in ans:
        ans= ans + (i+b)

print(ans)


    


        

    












        
        


















            
