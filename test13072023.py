list_= [84, 92.13, 'apples']
mylist=list() # passing an empty list

#creating a list from iterables
 
char_list=list('hello') #break the list to its char to count, search, check for vowels, capitals,etc

my_list=list(range(1,6))

A_matrix=[[0,1,0], [1,1,0],[0,0,1]] #matrix is a 2D list

#create a list based on the expression

#list comprehension is optimal way to create a list

squares_num=[x**2 for x in range(5)]

odd_num=print([x for x in range(10) if x%2!=0])
#print(odd_num)

#replicate the list
list1=[0]*2

list2=['a',54]*2
print(list2)

bool_list=print([True]*2)

import random
print([random.randint(1,100) for _ in range(5)]) # list comprehension

x=random.sample(range(1,100),5) # calling a random function
print(x)

[random.random() for _ in range(2)]
mylist2=[1,2,3,4,5]

#dir(mylist2)
# print the elements of a list
#method1
for num in mylist2:
 print(num)

#method2

for i in range(0,len(mylist2)):
 print(mylist2[i])

#delete an element
del mylist2[3] #[3] refers to the index
print(mylist2)

# negative indexing: starts from -1 o -n for n items in a list
print(mylist2[-1])
print(mylist2[-3])

originallist=[1,2,3,4,5]
new_list=originallist[1:4:2]
print(new_list)

new_list.append(56)# 56 is the value to be added to the list "at the end"
print(new_list)


#copy() shallow copy of the list
my_list3=[1,2,3]
new_list3=mylist2.copy()


#extend(iterable) appends elements from ietrable to end of list
my_list=[1,2,3]


#index


#insert
my_list4=[12,3,4]
my_list4.insert(1,4)
print(my_list4)

#pop(index)
element=my_list4.pop(-2)
print(element)
print(my_list4)


#remove(element)

#reverse()
my_list4.reverse()

#sort() sorting in the ascending order
my_list5=[367,44,51,16,89]
my_list5.sort()
print(my_list5)


#dictionary: mapping of keys to value

#curly braces are delimiters that intialise empty dict

#my_dict=dict()
#my_dict[1]=('Python')

#Acess the value with a key
#print(my_dict[1])

#comprehension of a dictionary

squares_num={x:x**2 for x in range(1,6)}
print(squares_num)

#keys=['a','b','=['a','b'],'c'']
#my_dict={k:v for k,v in enumerate(keys)}

#Access a value by key
my_dict={'name':'John','age':'30'}
print(my_dict['name']) #returns 'error' if no key as 'name' 
print(my_dict.get('name'))  #returns 'none' if no key as 'name' . Handled in error

dir(my_dict)



