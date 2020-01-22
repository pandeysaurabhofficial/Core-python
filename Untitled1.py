
# coding: utf-8

# # Data Types
Builtins type
1) Boolean
2) Numeric
3) Iterator & Generator 
4) Sequence 
5) text Sequence
6) Binary sequence
7) set 
8) Mapping
9) Context Manager
# # Boolean Types 

# In[1]:


bool


# In[2]:


bool(1)


# In[3]:


bool(100)


# In[4]:


bool(-1)


# In[5]:


bool(0)


# In[6]:


bool([1,2])


# In[7]:


bool([])


# In[8]:


bool([[]])


# In[9]:


bool("")


# In[10]:


bool("ab")


# In[11]:


bool(" ")


# In[12]:


str1 ="1234"


# In[13]:


str1.isdecimal()


# In[15]:


str1="abc123"
str1.isalpha()


# In[17]:


str1.isdecimal()


# In[19]:


bool(None)


# In[21]:


int(True)


# In[22]:


int(False)


# In[23]:


int(1)


# In[24]:


True + 1


# In[25]:


False * 50


# In[26]:


result = 6>5
print(result)


# In[27]:


result = 4>5
print(result)


# In[28]:


result = 3 in [1,2,3,4,5]
print(result)


# In[31]:


if(5<6):
    print("5 is less than 6")
else:
    print("5 IS NOT LESS THAN 6")


# # Numeric Types
1) Integers (1,2,100,-9...)
2) Float (2.32,-2.2....)
3) Complex numbers (2+3j)
# In[32]:


type(3)


# In[33]:


type(.23)


# In[34]:


type(1+3j)


# In[35]:


a = 3
b=5
c= a+b


# In[36]:


c


# In[37]:


c= a*b
c


# In[38]:


c = 2**3


# In[39]:


c


# In[40]:


c = 8**3
c


# # Math module

# In[41]:


import math


# In[43]:


math.ceil(23.3)


# In[44]:


math.floor(23.4)


# In[45]:


math.fabs(-5)


# In[46]:


math.factorial(5)


# In[47]:


math.fsum([1,2.5,3])


# In[50]:


math.gcd(8,12)


# In[51]:


math.exp(2)


# In[52]:


math.exp(1)


# In[53]:


math.log(10,2)


# In[54]:


math.log(5,5)


# In[55]:


math.pow(2,3)


# In[58]:


math.sqrt(16)


# In[59]:


math.sin(0)


# In[60]:


math.sin(1)


# In[61]:


math.sinh(10)


# In[62]:


math.degrees(1.57)


# In[64]:


math.degrees(11013.232)


# In[65]:


math.pi


# In[66]:


math.tau


# # Statistical function module

# In[74]:


import statistics as stat


# In[75]:


statistics.mean([1,2,3,4])


# In[76]:


stat.mean([1,3,4,5,2,68])


# In[78]:


stat.median([1,3,2,4,50])


# In[80]:


stat.median([2,1,50,3,4])


# In[81]:


stat.median([2,4,1,3,50,5])


# In[82]:


stat.median_low([2,4,1,3,50,5])


# In[83]:


stat.median_high([2,4,1,3,50,5])


# In[84]:


stat.mode([1,2,1,3,3,4,4,4,5])


# In[86]:


stat.mode([1,2,1,3,3,4,4,5,5,2])


# In[88]:


stat.harmonic_mean([1,2,3])


# In[89]:


stat.stdev([1,2,3])


# In[90]:


stat.stdev([1,2,5,600])


# In[91]:


stat.variance([1,2,5,500,600])

