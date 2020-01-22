
# coding: utf-8

# # Context Management and WITH keyword

# In[1]:


myfile = open('abc.txt','r')


# In[2]:


myfile


# In[3]:


for line in myfile:
    print(line)


# In[4]:


#it is important to close the file


# In[5]:


myfile.close()


# In[8]:


try:
    myfile = open('abc.txt','r')
    for line in myfile:
        print(line)
    myfile.close()
except:
    myfile.close()


# In[9]:


#i.e even if there is exception the file will be closed


# In[11]:


try:
    myfile = open('abc.txt','r')
    for line in myfile:
        print(line)
    myfile.close()
except:
    print('some error')
finally:
    print('executed')
    myfile.close()


# In[12]:


#to do above with WITH keyword


# In[13]:


#It make it easier to work with contextMGmt


# In[14]:


with open('abc.txt','r') as myfile:
    for line in myfile:
        print(line)

