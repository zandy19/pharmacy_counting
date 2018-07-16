
# coding: utf-8

# In[1]:

input='../input/itcont.txt'


# In[2]:

with open(input,'r') as input:
    rawData=input.readlines()





# In[4]:

drug_name=[]
drug_cost=[]
for i in range(1,len(rawData)):
    line=rawData[i].replace('\n','')
    words=line.split(',')
    drug_name.append(words[3])
    drug_cost.append(float(words[4]))


# In[5]:


# In[7]:

drug_summary={}
for i, name in enumerate(drug_name):
    if name in drug_summary.keys():
        drug_summary[name][0]+=1
        drug_summary[name][1]+=drug_cost[i]
    else:
        drug_summary[name]=[0,0]
        drug_summary[name][0]=1
        drug_summary[name][1]=drug_cost[i]
        
    


# In[8]:

drug_summary_sorted=sorted(drug_summary.items(), key=lambda x: x[0])



# In[10]:

drug_summary_sorted=sorted(drug_summary_sorted, key=lambda x: x[1][1],reverse=True)


# In[11]:



# In[12]:

output='../output/top_cost_drug.txt'
title_line='drug_name,num_prescriber,total_cost \n'


# In[13]:

with open (output,'w+') as out:
    out.write(title_line)
    for item in drug_summary_sorted:
        line= item[0]+','+ str(item[1][0])+','+ str(item[1][1])+'\n'
        out.write(line)


# In[ ]:



