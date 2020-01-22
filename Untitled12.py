
# coding: utf-8

# # Anonymous/Lambda Function

# In[1]:


#we can declare anonymous function by lambda and it don't look like normal function


# In[2]:


#syntax

lambda parameter : expression
# In[4]:


#sum of two numbers using lambda


# In[5]:


lambdasum = lambda a,b : a+b


# In[6]:


lambdasum(2,3)

#we use it beacause it comes in handy whenever we want to  quickly write an inline function.they look very simple and doesnot need too much of coding like normal function
# In[7]:


#largest no in given two no


# In[8]:


largest = lambda a,b : a if a>b else b


# In[9]:


largest(4,5)


# In[10]:


#you can use it inside filter function


# In[11]:


#finding even numbers using both functions


# In[12]:


lst1 = [1,2,3,4,5,6,7,8,9,10]


# In[14]:


list(filter(lambda x:x%2==0,lst1))


# In[15]:


#reduce function


# In[16]:


#sum of all element using reduce and lambda function


# In[17]:


from functools import reduce


# In[18]:


lst1 = [1,2,3,4,5,6,7,8,9,10]


# In[19]:


reduce(lambda a,b : a+b,lst1)


# In[20]:


#map function


# In[21]:


#multiply each item in list with 2


# In[22]:


lst1 = [1,2,3,4,5,6,7,8,9,10]


# In[23]:


list(map(lambda a: a*2,lst1))

