
# coding: utf-8

# # Functions in python

# In[1]:


#functions are re-usable blocks of code
#builtin function


# In[2]:


sum([1,2,3,4])


# In[3]:


#but we are going to excute some user defined functions 
#syntax for user-define function

def function_name(arguments):
    #function defination/set of statements
# In[8]:


def multiplication_function(a,b):
    c = a*b
    return c 


# In[5]:


#functions will return 'None by default if no return statement is written


# In[9]:


multiplication_function(1,2)


# In[10]:


def multiplication_function(a,b):
    c = a*b


# In[16]:


x = multiplication_function(1,2)
print(x)


# In[19]:


def multiplication_function(a,b):
    """ 
This function accepts two nos and returns the multiplication of those two
    """
    c = a*b
    return c 


# In[20]:


multiplication_function(1,2)


# In[21]:


#default/optional arguments of functions


# In[23]:


def multiply(a,b=2):
    return a*b
    


# In[24]:


multiply(3,3)


# In[25]:


multiply(3)


# In[26]:


#Variable number of arguments


# In[28]:


def sample_function(*args): #* accept varaible args
    for i in args:
        print(i)


# In[30]:


sample_function(2,4)


# In[31]:


#Local and Global Varaibles


# #The Varaible which is written inside the function is called as local varaible since it is written inside the function.
# The one which is written outside the function is called as the global variable

# In[32]:


a = 50 #global


# In[34]:


def function123():
    a = 12 #local
    return a


# In[35]:


print(a)


# In[36]:


function123()


# In[38]:


print(a) #values doesn't change


# In[39]:


def function123():
    global a
    a = 12 
    return a


# In[40]:


print(a)


# In[42]:


function123()


# In[44]:


print(a) #value is changes


# In[45]:


#Nested Functions


# In[46]:


#These are those functions in which one function is written inside another function


# In[47]:


import time


# In[48]:


def timer(n):
    def display(a):
        print(a)
        time.sleep(0.5)
    
    while(n>0):
        display(n)
        n-=1


# In[49]:


timer(6)


# In[50]:


#Recursive function


# In[51]:


#these are those function in which the function calls itself for certain number of times


# In[52]:


#find the factorial using recursive function


# In[58]:


def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)


# In[59]:


factorial(6)


# In[60]:


#Decorators


# In[61]:


#it is used to add new functionalities to an existing functions without even modifying the existing function definitions.


# In[65]:


def divide(a,b):
    print(a/b)


# In[67]:


divide(5,2)


# In[68]:


divide(5,0)


# In[69]:


#if can't change anything inside function we use decorators


# In[70]:


def validate(divide):
    def final(a,b):
        if(b==0):
            print('cannot divide by zero')
        else:
            return divide(a,b)
    return final


# In[71]:


@validate
def divide(a,b):
    print(a/b)


# In[72]:


divide(5,0)

