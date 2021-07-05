#!/usr/bin/env python
# coding: utf-8

# In[1]:


def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(20, 35, 19))


# In[3]:


def calculation(a, b):
    return a+b, a-b

res = calculation(40, 10)
print(res)


# In[5]:


items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))


# In[6]:


# Python program to multiply all values in the
# list using traversal

def multiplyList(myList) :
	
	# Multiply elements one by one
	result = 1
	for x in myList:
		result = result * x
	return result
	
# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))


# In[7]:


import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)


# In[ ]:




