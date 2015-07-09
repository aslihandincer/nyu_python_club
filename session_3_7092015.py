
# coding: utf-8

# #String Exercise

# Type and hit enter:

# In[1]:

sample_name = 'Rep2_4Epositive_HD'


# Now index **sample_name** so that the output is ‘HD’

# In[3]:

sample_name[-2:]


# Type and hit enter:

# In[4]:

sample_type = sample_name.split('_')


# The split method takes as input a string and returns a list
# 
# Type and hit enter:

# In[5]:

sample_type[-1]


# Notice that lists can be indexed like strings

# # Lists
# Lists are positionally ordered collections of arbitrarily typed objects denoted by brackets
# 
# Type and press enter:

# In[6]:

L = [6, 'spam', 1.23] 


# In[7]:

L2 = [1+2+3, 'spam', 1.23]


# Empty lists look like this:
# 
# Type and press enter (Note that we overwrote the previous variable L):

# In[9]:

L = []


#  Sequence operations that we performed on strings like concatenating (+ or *), indexing, and finding the length can also be performed on lists.
#  
#  Sequence operations must be performed on object types that are the same, meaning [‘a’, ‘b’, ‘c’] + ‘d’ doesn’t work
#  
#  However, there are methods that are only associated with lists, just like there are methods that can only be used with strings
# 
# 

# # [List] Methods

# .append()
# 
# max
# 
# .index
# 
# Type and hit enter:

# In[12]:

example_list = []


# In[13]:

example_list.append(4)


# In[14]:

example_list


# In[15]:

example_list.append(5)


# In[16]:

example_list


# In[17]:

max(example_list)


# In[18]:

example_list.index(5)


# There are many many more list methods, these are just the ones that will get you through the homework.  We will cover more in the future

# # Indexing with Lists

# Type and press enter:

# In[19]:

L = [123, 'spam', 1.23]


# In[20]:

len(L)


# In[21]:

L[0]


# How do you index L to retrieve the last element?

# In[22]:

L[-1]


# In[23]:

L[1][0]


# In[24]:

L[0][0]


# Why does L[1][0] work and L[0][0] return an error?

# #Building matrices with lists

# Because lists can contain many different types of objects, lists can contain lists.
# 
# Type and press enter:

# In[25]:

spreadsheet = [[1,2,3],[4,5,6],[7,8,9]]


# How many sublists are there within spreadsheet?
# 
# 3

# #Indexing matrices
# Type and press enter:

# In[26]:

spreadsheet[0]


# Now retrieve the the second element of the first sublist within spreadsheet (hint: go check out the slide on indexing lists for an idea of syntax)
# 
# Your indexing should return 2

# In[27]:

spreadsheet[0][1]


# #Performing operations on each element of a list
# Now just for fun retrieve the first row (or sublist) of spreadsheet and save it as the variable first_row, this is going to be our list we work with:
# 
# Type and press enter:

# In[44]:

first_row = spreadsheet[0] 


# We are going to multiply each element of first_row by 2.  First we are going to try first_row*2

# Type and press enter:

# In[45]:

first_row*2


# This doesn’t give us what we want

# Next we are going to try multipling each element of first_row by 2 using indexing.  Store your answer as a list to a variable called answer. 

# In[46]:

answer = [first_row[0]*2, first_row[1]*2, first_row[2]*2]


# In[47]:

answer


# When you retreive answer it should return:
# [2, 4, 6]

# Check to see if your answer function works with a different list.
# 
# Press and type enter:

# In[60]:

first_row = spreadsheet[1]


# Retype your answer = [your answer here] or use the up arrow to retrieve what you input for answer. When you retrieve your answer variable does it return the correct math still?
# 
# Take home: it’s painful to have to explicitly do an operation on each element of a list, particularly when that list is large.

# #Example For Loop
# Previously, we explicitly multiplied each item of first_row by 2:

# In[61]:

first_row = spreadsheet[0]


# In[62]:

answer = [first_row[0]*2, first_row[1]*2,first_row[2]*2]


# Now we can use a for loop to do the same:
# 
# Type and press enter:

# In[63]:

for item in first_row:
    item * 2


# To store the operation performed on each item as a new list:
# 
# Type and press enter:

# In[64]:

answer = [] 


# In[65]:

for item in first_row:
    answer.append(item*2)


# In[66]:

answer

