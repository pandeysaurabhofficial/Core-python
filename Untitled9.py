
# coding: utf-8

# # Decision/Conditional statements

# In[1]:


#this statement can control the flow of program,  i.e. it decide wheather code will be executed or not


# In[4]:


a = 6

if (a%2==0):
    print(a,'is an even number')


# In[5]:


(a%2==0)


# In[6]:


if (a%2==0):print(a,'is an even number')


# In[7]:


a = 6

if (a%2==0) and (a<10):
    print(a,'is an even number and less then 10')


# In[8]:


(a%2==0) and (a<10)


# In[9]:


#if...else statements


# In[10]:


a = 5

if (a%2==0):
    print(a,'is an even number')
else:
    print(a,'is an odd number')


# In[11]:


#nested if.....else statements


# In[14]:


a = 51

if(a%2==0):
    if(a<10):
        print(a,'= even number less than 10')
    else:
        print(a,'= even number greater then 10')
else:
    if(a<10):
        print(a,'= odd number less than 10')
    else:
        print(a,'= odd number greater then 10')
    


# In[15]:


#if....elif...else statements

#syntax
if exp1:
    #statements exp1
elif exp2:
    #stat exp2
......
...
elif expN
     #statt expN
else:
    #state else
# In[19]:


a = 6
if(a==0):
    print(a,'is neither even nor odd')
elif(a%2 == 0):
    print(a,'is an even number')
else:
    print(a,'is an odd number')


# In[22]:


a = 12
if(a==0):
    print(a,'is neither even nor odd')
elif(a%2 == 0) and (a<10):
    print(a,'is an even number less than 10')
elif(a%2 == 0) and (a>10):
    print(a,'is an even number greater then 10')
else:
    print(a,'is an odd number')


# In[ ]:


#it is not mandatory to write else condition

