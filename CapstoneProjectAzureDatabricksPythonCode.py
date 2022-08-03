#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Creating connection on top of the Azure Datalake Account 

serviceprincpleid="c5de8d16-a00e-4ee1-b50b-d5b8f383fd71"
serviceprincplekey=".E18Q~2d9qZALpRr4zuFwBcvcqf1jig6Dz5Smcsw"
configs = {
  "fs.azure.account.auth.type": "OAuth",
   "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
   "fs.azure.account.oauth2.client.id":serviceprincpleid,
   "fs.azure.account.oauth2.client.secret":serviceprincplekey,
   "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/16446715-0718-4581-af02-52ead6dc05d6/oauth2/token"}


# In[ ]:


#To create mount point on the Azure container , this code should be excecuted only for the first time.
dbutils.fs.mount(
source = "abfss://source@adlsprojectcontainer.dfs.core.windows.net/",
mount_point = "/mnt/mountadlsgen3",
extra_configs = configs)


# In[ ]:


# To know the mounted data path, in order to read the data later
get_ipython().run_line_magic('fs', '')
ls /mnt/mountadlsgen3


# In[ ]:




