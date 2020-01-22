
# coding: utf-8

# In[1]:


def age_program():
    seconds_or_years = input('Give me seconds (s) or years (y) ')
    if seconds_or_years =='s':
        #convert seconds to years
        user_value = input("Enter the number of seconds you've lived for:" )
        print("You've lived for {} years.".format(int(user_value)/60/60/24/365))
    elif seconds_or_years =='y':
        #convert years to seconds
        user_value = input("Enter the number of years you've lived for: ")
        print("You've lived for {} seconds.".format(int(user_value)*365*24*60*60))


# In[2]:


age_program()


# In[3]:


age_program()

