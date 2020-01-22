
# coding: utf-8

# # Object oriented programming language

# In[1]:


#object are instance of class, vehicle is class then car is object


# In[2]:


#attributes are nothing but data; attributes of car are wheel,engine,doors,etc


# In[3]:


#methods are nothing but the behaviours,ex- car can start,accelerate ,stop,etc


# In[5]:


class vehicle:
    pass


# In[6]:


car1 = vehicle()


# In[7]:


car1


# In[8]:


type(car1)


# In[12]:


class vehicle:
    def __init__(self,number_of_wheels,type_of_engine,seating_capacity):
        self.number_of_wheels = number_of_wheels
        self.type_of_engine = type_of_engine
        self.seating_capacity = seating_capacity
    def get_number_of_wheels(self):
        return self.number_of_wheels
    def set_number_of_wheels(self,number):
        self.number_of_wheels = number


# In[13]:


#getters and setters to access attributes


# In[16]:


Audi = vehicle(4,'petrol',5)


# In[17]:


Audi.get_number_of_wheels()


# In[18]:


#creating a class which has attributes and method


# In[19]:


class vehicle:
    def __init__(self,number_of_wheels,type_of_engine,seating_capacity):
        self.number_of_wheels = number_of_wheels
        self.type_of_engine = type_of_engine
        self.seating_capacity = seating_capacity
    def get_number_of_wheels(self):
        return self.number_of_wheels
    def set_number_of_wheels(self,number):
        self.number_of_wheels = number
    def Move(self):
        print('vehicle is moving')


# In[20]:


Audi = vehicle(4,'petrol',5)


# In[21]:


Audi.Move()


# In[22]:


#Abstraction- hiding unnecessary detail and Encapsulation-actual implementation of abstraction


# In[23]:


#by appending _ we can make attribute protected


# In[24]:


class Myclass():
    def __init__(self):
        self.a = 123 #public
        
        self._b = 456 #protected
        
        self.__c = 789 #private


# In[25]:


obj = Myclass()


# In[26]:


print(obj.a)


# In[27]:


print(obj._b)


# In[28]:


print(obj.__c)


# In[30]:


print(obj._Myclass__c)


# In[31]:


#Inheritance- to avoid repetitive coding and encourage the code reusability


# In[33]:


class vehicle():
    def __init__(self,number_of_wheels,seats,max_speed):
        self.number_of_wheels = number_of_wheels
        self.seats = seats
        self.max_speed = max_speed


# In[34]:


class car(vehicle):
    def __init__(self,number_of_wheels,seats,max_speed):
        vehicle.__init__(self,number_of_wheels,seats,max_speed)


# In[35]:


car1 = car(4,5,100)


# In[37]:


car1.number_of_wheels


# In[38]:


#Polymorphism - when different classes have same method but implemented in a different way, we can call it as polymorphism.


# In[39]:


class animal():
    def __init__(self,name):
        self.name = name
    def talk(self):
        pass


# In[40]:


class cat(animal):
    def talk(self):
        print('meow')


# In[41]:


class dog(animal):
    def talk(self):
        print('woof')


# In[43]:


cat1 = cat('cat1')
cat1.talk()

