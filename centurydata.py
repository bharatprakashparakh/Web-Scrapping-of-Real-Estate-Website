
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import ssl
import pandas as pd


# In[2]:


r = requests.get("https://www.makaan.com/chennai-residential-property/buy-property-in-chennai-city?budget=,")
print(type(r))
code = r.content
#print(code)


# In[14]:


soup = BeautifulSoup(code,"html.parser")
#print(soup.prettify())


# In[15]:


all = soup.find_all("div",{"class":"title-line"})
print(len(all))


# In[16]:


for item in all:
    print(item)
    print("")


# In[17]:


l=all[0].find('a',{"data-type":"listing-link"})
#print(l.get("href"))


# In[18]:


links = []
for item in all:
    l=item.find('a',{"class":"typelink"})
    links.append(l.get("href"))
    
    #print(links)


# In[19]:


list2=[]
name=[]
size = []
place=[]
location=[]
city=[]
i=0

for link in links:
    
    r1 = requests.get(link)
    code1 = r1.content
    soup1 = BeautifulSoup(code1,"html.parser")
    all1 = soup1.find_all("h1",{"class":"type-wrap"})
    
    #name.append(all1[0].find(('span',{"class":"type"})).text)
    
    s = all1[0].find_all(("span",{"class":"size"}))
    if(len(s)>5):
        name.append(s[0].text)
        size.append(s[1].text)
        place.append(s[2].text)
        location.append(s[4].text)
        city.append(s[5].text)
        
    else:
        name.append(s[0].text)
        size.append(s[1].text)
        place.append(s[2].text)
        location.append(s[2].text)
        city.append(s[3].text)
        
    list1= [name[i],size[i],place[i],location[i],city[i]]
    list2.append(list1)
    i=i+1
#print(name)
#print(size)
#print(place)
#print(location)
#print((city))
#print(list2)


# In[20]:


df=pd.DataFrame(list2)
df.columns=['Name','Size','Place','Locality','City']
#df.set_index('Name')
print(df)
df.to_csv('makaan.csv')

