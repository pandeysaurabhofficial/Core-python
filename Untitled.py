
# coding: utf-8

# <h1> Variables --> reserved memory location to store some values </h1>

# In[6]:


message = " HEllo World"


# In[7]:


print(message)


# In[8]:


type(message)


# In[9]:


message = 5


# In[10]:


type(message)


# In[11]:


del message


# In[12]:


print(message)


# <h2> Casing </h2>

# <h3>Pascal casing</h3>

# In[13]:


NumberOfPeople = 5


# <h4> Camel Casing </h4>

# In[14]:


numberOfPeople = 5


# <h1> Snake Case </h1>

# In[15]:


number_of_people = 5


# Pascal casing for classnames
# Camel casing for Variables and function
# Snake casing for constant

# <h1> Constant </h1>

# In[16]:


CONST_EXAMPLE = 50


# <h1> Rules to be followed while writing Variable name </h1>

# 1) It should start with letter or underscores. It should not start with numbers for ex -

# In[17]:


_name = "saurabh"


# In[18]:


na_me = "Saurabh"


# In[19]:


9name = "sa"


# In[20]:


na123 = "sa"

2) It should contain only alphanumeric characters and underscores
   A-Z
   a-z
   0-9
   _
# In[21]:


name? = "ssssssd"


# In[22]:


name{asd = 14

3) Variable Names are Case Sensitive
# In[23]:


numberone = 1
print(numberone)


# In[25]:


Numberone = 100
print(numberone)
print(Numberone)


# 4) never ever used reserve keywords as variable names
# 

# In[28]:


import keyword
print(keyword.kwlist)


# In[29]:


import builtins


# In[30]:


print(dir(builtins))


# In[31]:


print(builtins)


# In[32]:


zip = "hello"


# In[33]:


print(zip)


# In[34]:


myList = [1,2,3]


# In[37]:


max(myList)


# In[38]:


max = "hello"


# In[39]:


print(max)


# In[40]:


max(myList)


# # Operators

# In[41]:


4 + 4


# In[42]:


4 - 4


# In[43]:


13//4


# In[44]:


13%4


# In[45]:


13/4


# In[46]:


2**3


# 1) assingment operators

# In[47]:


a=4


# In[48]:


b="hello"


# In[54]:


a+=1


# In[55]:


a


# In[56]:


a+=3


# In[57]:


a


# In[58]:


b+="world"


# In[59]:


b


# In[60]:


a-=1


# In[61]:


a


# In[62]:


a*=3


# In[63]:


a


# In[64]:


b*=2


# In[65]:


b

