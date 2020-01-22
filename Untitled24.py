
# coding: utf-8

# In[11]:


import requests


# In[12]:


from bs4 import BeautifulSoup


# In[14]:


request = requests.get('https://www.amazon.com/PlayStation-Slim-1TB-Console-Bundle-4/dp/B07YLDNTKB/ref=sr_1_1?fst=as%3Aoff&pf_rd_i=16225016011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=03b28c2c-71e9-4947-aa06-f8b5dc8bf880&pf_rd_r=8QQ1JWJ2EWSVA8R1WTVG&pf_rd_s=merchandised-search-3&pf_rd_t=101&qid=1579605739&refinements=p_89%3APlaystation&rnid=2528832011&s=videogames-intl-ship&sr=1-1')
content = request.content
soup = BeautifulSoup(content, 'html.parser')
element = soup.find('span', {'itemprop': 'price', 'class': 'a-size-medium a-color-price priceBlockBuyingPriceString'})
print(element.text)

