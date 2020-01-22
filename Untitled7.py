
# coding: utf-8

# # Iterators and Generators in Python

# In[1]:


lst1 = [1,2,3,4]

for i in lst1:
    print(i)


# In[3]:


iter1 = iter([1,2,3])


# In[4]:


type(iter1)


# In[5]:


iter1


# In[6]:


for i in iter1:
    print(i)


# In[7]:


iter1 = iter([1,2,3])


# In[8]:


next(iter1)#next is a builtin function in python


# In[10]:


next(iter1)


# In[11]:


next(iter1)


# In[12]:


next(iter1)


# In[13]:


iter1 = iter([1,2,3])


# In[15]:


while True:
    try:
        print(next(iter1)) #this is equivalent to for loop
    except StopIteration:
        break


# # Generators

# In[17]:


#its a type of iterator and its look like a function


# In[18]:


def sum_func(a,b):
    return a+b


# In[19]:


def generator_123():
    yield 1
    yield 2
    yield 3


# In[21]:


print(type(generator_123()))


# In[22]:


gen1 = generator_123()


# In[23]:


gen1


# In[24]:


for i in gen1:
    print(i)


# In[25]:


next(gen1)


# In[27]:


while True:
    try:
        print(next(gen1))
    except StopIteration:
        break

