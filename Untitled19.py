
# coding: utf-8

# # Age of seconds

# In[1]:


input('Enter your age: ')


# In[2]:


user_age = input('Enter your age: ')


# In[3]:


user_age


# In[4]:


int(user_age)


# In[5]:


int(user_age) * 365 * 24 * 60 * 60


# In[6]:


seconds = int(user_age) * 365 * 24 * 60 * 60


# In[7]:


seconds


# In[8]:


print('You have lived for {} seconds.'.format(seconds))

