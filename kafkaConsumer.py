#!/usr/bin/env python
# coding: utf-8

# In[1]:


from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps,loads
import json


# In[3]:


consumer= KafkaConsumer('stockmarketanalysis',bootstrap_servers=['3.147.127.13:9092'],value_deserializer=lambda x: loads(x.decode('utf-8')))


# In[ ]:


for c in consumer:
    print(c.value)


# In[ ]:





# In[ ]:




