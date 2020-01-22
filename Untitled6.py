
# coding: utf-8

# # Sets in python

# In[1]:


set1 = {'a','b','c'}
set1


# In[2]:


type(set1)


# In[3]:


#Set is an unordered collection of unique objects


# In[4]:


set1[0]


# In[6]:


# i.e.  set can't be indexed


# In[7]:


#set contain only uniques objects


# In[8]:


set1 = {1,2,3,4,5,1,2,3}
set1


# In[9]:


set([1,2,3,4,1,2]) #conversion of list into set


# In[11]:


list(set([1,2,3,4,1,2])) #set to list


# In[12]:


set('abcaad')


# In[13]:


''.join(set('abcaad'))


# In[14]:


set([1,2,3,4,1,2])


# In[15]:


if 2 in set1:
    print('present')
else:
    print('absent')

#set supports
 Union
     Intersection
        difference , etc
# In[16]:


set1 = {1,2,3,4}
set2 = {4,5,6}


# In[17]:


set1.union(set2)


# In[18]:


set1.intersection(set2)


# In[19]:


set1.difference(set2)


# In[21]:


#subset and superset


# In[24]:


set1 = {1,2,3,4}
set2 = {1,2}


# In[26]:


set2.issubset(set1)


# In[27]:


set1.issuperset(set2)


# In[28]:


#add/discard elements in set


# In[29]:


set1 = {1,2,3,4}
set1


# In[31]:


set1.add(5)


# In[32]:


set1


# In[33]:


set1.discard(5)


# In[34]:


set1

