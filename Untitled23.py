
# coding: utf-8

# In[8]:


import requests


# In[9]:


request = requests.get('http://www.google.com')


# In[10]:


print(request.content)

