#!/usr/bin/env python
# coding: utf-8

# In[37]:


import os
import csv

d = []

csvpath = os.path.join ("Resources","election_data.csv")
with open(csvpath, 'r' , newline = '') as csvfile:
    reader = csv.reader (csvfile, delimiter = ',')
    for rows in reader:
         d.append(rows[2])
votes = len(d)-1       
Khan_votes = d.count('Khan')
Correy_votes = d.count('Correy')
Li_votes = d.count('Li')
Tooley_votes = d.count("O'Tooley")
K_r = float(Khan_votes/votes)
C_r = float(Correy_votes/votes)
L_r = float(Li_votes/votes)
T_r = float(Tooley_votes/votes)

Khan_results = "{:.3%}".format(K_r)
Correy_results = "{:.3%}".format(C_r)
Li_results = "{:.3%}".format(L_r)
Tooley_results = "{:.3%}".format(T_r)

results = {'Khan':K_r,'Correy':C_r,'Li':L_r,"O'Tooley":T_r}
winner = max(results, key=results.get)

output_path = os.path.join ("Resources","PyPollResults.csv")

print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes}")
print("-------------------------")
print(f"Khan: {Khan_results} ({str(Khan_votes)})")
print(f"Correy: {Correy_results} ({str(Correy_votes)})")
print(f"Li: {Li_results} ({str(Li_votes)})")
print(f"O'Tooley: {Tooley_results} ({str(Tooley_votes)})")    
print("-------------------------")
print(f"Winner: {winner}")
    
with open(output_path,'w', newline = '') as outputfile:
    writer = csv.writer (outputfile, delimiter = ',')
    writer.writerow (["Election Results",""])
    writer.writerow (["-------------------------",""])
    writer.writerow ([f"Total Votes: {votes}",""])
    writer.writerow (["-------------------------",""])
    writer.writerow ([f"Khan: {str(Khan_results)} ({str(Khan_votes)})",""])
    writer.writerow ([f"Correy: {str(Correy_results)} ({str(Correy_votes)})",""])
    writer.writerow ([f"Li: {str(Li_results)} ({str(Li_votes)})",""])
    writer.writerow ([f"O'Tooley: {str(Tooley_results)} ({str(Tooley_votes)})",""])    
    writer.writerow (["-------------------------",""])
    writer.writerow ([f"Winner: {winner}",""])


# In[ ]:




