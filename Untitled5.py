
# coding: utf-8

# # Tuple in python

# In[1]:


#tuple are just like list except the fact thats its immutable


# In[2]:


#its a sequence of value differentaited by , 


# In[3]:


tup1 = 1,2,3,4
tup1


# In[4]:


type(tup1)


# In[5]:


#its not necessary but recommended to enclosed the values in parenthesis


# In[6]:


tup1 = (1,2,3,4)
tup1


# In[7]:


tup1[0] = 5


# In[8]:


#its immutable


# In[9]:


#tuple with one item


# In[10]:


tup1 = (1,)
type(tup1)


# In[11]:


tup1 = (1)
type(tup1)


# In[12]:


#empty tuple


# In[13]:


tup1 = ()
type(tup1)


# In[14]:


tup1= tuple()
type(tup1)


# In[15]:


#like list tuple can have items of different data types


# In[16]:


tup1 = (1,'a',2.0,[1,2],('a','b'))
tup1


# In[17]:


#concatenation of two tuples


# In[18]:


('a','b') + ('c','d')


# In[19]:


#use * to replicate the items in tuple


# In[20]:


('a','b','c')*3


# In[21]:


#indexing of tuples is just like list


# In[22]:


tup1 = ('a','b','c','d','e')
tup1


# In[23]:


tup1[0]


# In[24]:


tup1[-1]


# In[25]:


#slicing of tuples


# In[26]:


tup1[0:3]


# In[27]:


tup1[::-1] #for reverse way


# In[28]:


#theres a built in function in python divmod which will return quoteint and reminder and return type is tuple


# In[29]:


divmod(5,2)


# In[31]:


#varaible number of arguments to a function


# In[32]:


def VarNumberFunction(*args):
    print(args,type(args))


# In[33]:


VarNumberFunction(1,2,3,'a','b')


# In[34]:


max(1,2,3,4,5)


# In[36]:


lst1 = [1,2,3]
lst2 = ['a','b','c']


# In[37]:


for i in zip(lst1,lst2):
    print(i)


# In[38]:


#if you want to convert list into tuple


# In[39]:


tuple([1,2,3])


# In[40]:


#tuple have only two function indec and count


# In[44]:


tup1 = ('a','b','c','d','a')
tup1.index('a')


# In[45]:


tup1.count('a')

