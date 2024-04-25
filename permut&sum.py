# i1=int(input("enter any number:"))
# sum2=0
# while i1>0:
#     sum = i1%10 
#     sum2+=sum   
    
#     i1//=10
# print(sum2)

"""
# find permutaion

elements = [1, 2, 3]
permutations = [[]]
for element in elements:
 new_permutations = []
 for permutation in permutations:
 for i in range(len(permutation) + 1):
 new_permutation = permutation[:i] + [element] + permutation[i:]
 new_permutations.append(new_permutation)
 permutations = new_permutations
for permutation in permutations:
 print(permutation)
 """
# sorting
# list =[12,21,5,19,23]
# list.sort()
# print(list[-2])

# find second number in your list

# list =[12,21,5,19,23,45,42]
# n1=0
# n2=[]
# for i in list:
#     if i>n1:
#         n1=i
#     else:
#         continue
# list.remove(n1)
# n2=0
# for i in list:
#     if i>n2:
#         n2=i
#     else:
#         continue    
# print(n2)

str1=input("enter 1st:")
str2=input("enter 2nd:")
flag=False
for i in str1:
    if i in str2:
        flag = True
    else:
        flag = False
        break
if flag == True:
    print("anagram of each other") 
else:
    print("not anagram")        
        
