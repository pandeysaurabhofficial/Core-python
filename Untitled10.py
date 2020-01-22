
# coding: utf-8

# # Loop statements

# In[1]:


#looping statements are those statements which makes an action to repeat for a certain number of times


# In[2]:


#for and while are two main looping statements

while(exp):
    #statements
# In[3]:


import time


# In[6]:


count = 5

while(count>0):
    print(count)
    count-=1
    time.sleep(1)

#for loops: the loop can be used to loop through individual items of an iterable object. The loop terminates when all the items in the iterable object is exhausted. or in other words, the for loop stops when it has finished looping through all the individual items in an iterator
# In[8]:


lst1 = [1,2,3,4]
for i in lst1:
    print(i)
    time.sleep(1)


# In[9]:


str1 = 'HELLO'
for i in str1:
    print(i)
    time.sleep(1)


# In[10]:


# for loops: iterating the indexes and items of a list using for loop


# In[15]:


lst1 = ['a','b','c','d']


# In[17]:


for i in range(len(lst1)): #range is built function
     print(lst1[i],':',i)             


# In[18]:


#enumerate built in function


# In[19]:


lst1 = ['a','b','c','d']


# In[20]:


for i,item in enumerate(lst1):
    print(item,':',i)


# In[21]:


lst1 = ['a','b','c','d']
lst2 = [10,20,30,40]


# In[23]:


for i,j in zip(lst1,lst2):
    print(i,':',j)
    time.sleep(0.5)


# In[24]:


#break condition : it is to terminate the loop and can be use in both for and while looop


# In[28]:


fruits = ['apple','orange','grapes','strawberry','lychee']
for fruit in fruits:
    print('found:',fruit)
    time.sleep(1)
    if(fruit=='grapes'):
        print('stop the search')
        break


# In[29]:


#continue statement


# In[30]:


fruits = ['apple','orange','grapes','strawberry','lychee']
print('intial list:',fruits)

for fruit in fruits.copy():
    if(fruit=='grapes'):
        continue
    fruits.remove(fruit)
    print('removed',fruit,'from the list')
    time.sleep(1)
    
print('final list:',fruits)

