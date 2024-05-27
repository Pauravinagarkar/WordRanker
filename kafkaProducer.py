#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install kafka-python')


# In[4]:


pip install kafka-python


# In[ ]:


import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps
import json


# In[ ]:


producer=KafkaProducer(bootstrap_servers=['3.147.127.13:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))


# In[ ]:


producer = KafkaProducer(
    bootstrap_servers=['3.147.127.13:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)


# In[15]:


producer.send('stockmarketanalysis',value="{'name':'Sachin'}")


# In[ ]:


df =pd.read_csv("C:/Users/paura/Downloads/indexProcessed.csv")


# In[19]:


print(df)


# In[ ]:


while True:
    dict_stock=df.sample(1).to_dict(orient="records")[0]
    producer.send('stockmarketanalysis',value=dict_stock)
    


# In[ ]:




