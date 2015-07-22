
# coding: utf-8

# #List Review#
# 
# Previously, we wanted to isolate the first row of spreadsheet and multiply each number by 2.  Type and press enter:
# 

# In[3]:

spreadsheet = [[1, 2, 3], [4,5,6],[7,8,9]]
first_row = spreadsheet[0]
answer = [first_row[0]*2, first_row[1]*2,first_row[2]*2]


# In[4]:

answer


# Index spreadsheet in order to create a list containing 2, 5, 8 so that when you return your variable it will look like [2,5,8]

# In[5]:

answer2 = [spreadsheet[0][1], spreadsheet[1][1], spreadsheet[2][1]]


# In[6]:

answer2


# #Example For Loop#

# In[7]:

for item in first_row:
    print(item * 2)


# #Storing the result of a for loop as a list#

# In[8]:

new_answer = [] 
for item in first_row:
    new_answer.append(item*2)


# In[9]:

new_answer


# In[10]:

new_answer2 = []
for item in first_row:
    new_answer2.append(item*2)
    print(item*2)


# In[11]:

new_answer2


# #Your Turn#

# In[12]:

for row in spreadsheet:
    print(row)


# Now using the same loop instead of returning the whole row, return the second item in each row

# In[13]:

for row in spreadsheet:
    print(row[1])


# #Example if statement#

# In[14]:

x = 'killer rabbit'
if x == 'roger': 
    print('how is jessica?')
elif x == 'bugs':
    print('what is up doc?')
else:
    print( 'Run away! Run away!' )


# In[16]:

x = 'killer rabbit'
if x == 'roger':
    print('how is jessica?')


# Notice the difference between the first block of code and the second block of code.  Why does the second block of code yield no output? 

# #Nested Statements: Bringing for and if together#

# In[18]:

example = 'noythp'

if example == 'p':
    print('This is the beginning of python')

if example[-1] == 'p':
    print('This is the beginning of python')
    
for letter in example:
    if letter == 'p':
        print('This is the beginning of the word')


# #Another example of a nested statement#

# Here is an example where I use the for loop to issue a command on each item in example followed by an if loop to also execute a command using logic.

# In[20]:

for letter in example:
    print(letter)
    if letter == 'p':
        print('This is the beginning of the word')
    else:
        print('?')


# #Write a python script using for/if statements#

# 
# Goal: To pull out the gene name that has a p.value less than 0.05.
# 
# Break this down into a series of steps:
# 
# 1. figure out whether you can use an if statement to evaluate true/false correctly.
# 
# i.e. I would index gene_table and store the row where the gene actually has a value less than 0.05 as a variable.  I would then build an if statement to see if I could accurately assess whether I could isolate that value and return true if it is less than 0.05.

# In[21]:

gene_table = [['gene', 'p.value'], ['a1bg', 0.25], ['bbx',0.06], ['creb1', 0.04]]
sample_row = gene_table[3]
if sample_row[-1]<0.05:
    print('yes')
else:
    print('no')


# 2. put your if statement into a for loop that iterates through all of the rows in the table
# 3. change your if statement so that if it evaluates true, than it prints the gene name.  If false, it returns nothing

# In[22]:

for row in gene_table:
    if row[-1] < 0.05:
        print('yes')
        print(row[0])

