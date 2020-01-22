
# coding: utf-8

# # Regular expression in python

# In[1]:


#it can use to match certain patterns


# In[2]:


#for ex- chaecking of email address is in correct format or not, finding out pincodes in address


# In[3]:


import re


# In[4]:


#check if string contains only numbers using regex:


# In[5]:


data = '515'
if re.match(r'^[0-9]*$',data):
    print('match')
else:
    print('no match')


# In[6]:


data = '515 abc'
if re.match(r'^[0-9]*$',data):
    print('match')
else:
    print('no match')


# In[7]:


# extracting all the numbers from a string


# In[11]:


str1 = 'hgv 1 h 123hhgh 253'
lst1 = re.findall('[0-9]+',str1)
print(lst1)


# In[12]:


str1 = 'hgv 1 h 123hhgh 253'
lst1 = re.findall('[a-z]+',str1)
print(lst1)


# In[13]:


str1 = 'hgv 1 h 123HJHhhgh 253'
lst1 = re.findall('[A-Z]+',str1)
print(lst1)


# In[14]:


str1 = 'hgv 1 h 123HJHhhgh 253'
lst1 = re.findall('[a-zA-Z]+',str1)
print(lst1)


# In[15]:


str1 = 'hgv 1 h 123HJHhhgh 253 *////####'
lst1 = re.findall('[a-zA-Z0-9]+',str1)
print(lst1)


# In[18]:


str1 = 'hgv 1 h 123HJHhhgh 253 *////####'
lst1 = re.findall('/w+',str1) #backslash
print(lst1)


# In[19]:


#email id validation using regex


# In[22]:


data = 'akajsbkja@gamil.com'
if re.match(r'[a-zA-Z0-9_]+@[a-zA-Z0-9_]',data): #a-zA-Z0-9_ instead of this backslash w+@ bckslh w+ can be written as well
    print('match')
else:
    print('no match')


# In[23]:


#check if file name is an image


# In[24]:


data = 'abc.jpg'
if re.match(r'^\w+\.(gif|png|jpg|jpeg)$',data):
    print('match')
else:
    print('no match')

