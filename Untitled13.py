
# coding: utf-8

# # Exception Handling in Python

# In[1]:


#certain errors python identify itself like syntax errors


# In[2]:


print('HEllo'


# In[3]:


#certain errors can't be identify in compilation time but in runtime


# In[12]:


a = 5
b = 0


# In[6]:


c = a+b
print('addiction=',c)


# In[7]:


c = a/b
print('division',c)


# In[8]:


#try and except blocks


# In[11]:


try:
    a=5
    b=0
    c=a/b
    print(c)
except:
    print('error occured')


# In[13]:


#Child class exception


# In[18]:


try:
    a=5
    b='abc'
    c=a/b
    print(c)
except ZeroDivisionError: #child exception (it should be return first then parent exception)
    print('Zero division error occured')
except:
    print('some error occured')


# In[19]:


#Raising Exception Manually


# In[20]:


try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print('Zero division error occured')
except:
    print('some error occured')


# In[21]:


#try,Except & Finally...


# In[22]:


file = open('abc.txt','r')

for line in file:
    print(line)
    
file.close()


# In[23]:


#lets assume some error occur without closing file


# In[24]:


try:
    file = open('abc.txt','r')

    for line in file:
        print(line)
    
    file.close()
except:
    file.close()


# In[25]:


try:
    file = open('abc.txt','r')

    for line in file:
        print(line)
    
except:
    print('some error occureed')
finally:
    file.close()

