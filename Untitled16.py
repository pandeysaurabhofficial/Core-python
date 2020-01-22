
# coding: utf-8

# # Data Analysis and Visualization with Python

# In[2]:


# Numpy ~ Linear Algebra
# Pandas ~ Data Analysis
# Matplotlib ~ Data Visualization


# In[3]:


#Numpy


# In[4]:


#stands for 'Numerical Python'
#it is a linear library
#it is used to work with multidimensional array objects.
#Most data science libraries in python are built on top of numpy.
#Numpy objects are homogeneous multidimensional arrays.


# In[5]:


import numpy as np


# In[6]:


a = np.array([1,2,3,4])
a


# In[7]:


a = np.array([[1,2,3],[4,5,6]])
a


# In[8]:


a.shape


# In[9]:


a.ndim


# In[10]:


a = np.array(10)
a


# In[11]:


a.size


# In[12]:


np.zeros(5)


# In[13]:


np.zeros((2,3))


# In[14]:


np.ones((2,3))


# In[15]:


a = np.array([10,20,30,40])
b = np.array([2,4,6,8])


# In[16]:


a+b


# In[17]:


a-b


# In[18]:


a*b


# In[19]:


a/b


# In[20]:


b*2


# In[21]:


a = np.array([[1,2],[3,4]])
b = np.array([[1,1],[1,1]])


# In[22]:


a*b


# In[24]:


a@b #size should match


# In[25]:


a = np.array([[1,2],[3,4]])
a


# In[26]:


a.sum()


# In[27]:


a.max()


# In[28]:


a.min()


# In[31]:


#STACKING of arrays


# In[32]:


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[9,8,7],[6,4,5]])


# In[34]:


np.vstack((a,b))

