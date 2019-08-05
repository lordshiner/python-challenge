#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import csv

d = []
r = 0
var1 = -1

csvpath = os.path.join ("Resources","budget_data.csv")
with open(csvpath, 'r' , newline = '') as csvfile:
    reader = csv.reader (csvfile, delimiter = ',')
    for rows in reader:
        r += 1
        d.append([r-1,rows[0],rows[1]])

row_num = [item[0] for item in d]
the_date = [item[1] for item in d]
the_PL = [item[2] for item in d]

for items in d:
    var1 += 1
    if  var1 >= 2:
        diff1 = int(the_PL[var1])
        diff2 = int(the_PL[var1 - 1])
        diff = diff1 - diff2
        d[var1].append(diff)
        d[var1].append(diff1)
    elif var1 == 1:
        placeholder = 0
        diff1 = int(the_PL[var1])
        d[var1].append(placeholder)
        d[var1].append(diff1)
    else:
        placeholder = 0
        d[var1].append(placeholder)
        d[var1].append(placeholder)
        
rolling_diff = [item[3] for item in d]
PL_int = [item[4] for item in d]

Months = str(len(d)-1)
max_index = rolling_diff.index(max(rolling_diff))
min_index = rolling_diff.index(min(rolling_diff))
Increase_month = the_date[max_index]
Increase_Amt = max(rolling_diff)
Decrease_month = the_date[min_index]
Decrease_Amt = min(rolling_diff)
count = len(rolling_diff)-2
sum_diff = sum(rolling_diff)
avg_diff = round(float(sum_diff/count),2)
Total = str(sum(PL_int))

output_path = os.path.join ("Resources","PyBankResults.csv")

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Months}")
print(f"Total: ${Total}")
print(f"Average  Change: ${str(avg_diff)}")
print(f"Greatest Increase in Profits: {Increase_month} ({str(Increase_Amt)})")
print(f"Greatest Decrease in Profits: {Decrease_month} ({str(Decrease_Amt)})")

with open(output_path,'w', newline = '') as outputfile:
    writer = csv.writer (outputfile, delimiter = ',')
    writer.writerow (["Financial Analysis",""])
    writer.writerow (["----------------------------",""])
    writer.writerow ([f"Total Months: {Months}",""])
    writer.writerow ([f"Total: ${Total}",""])
    writer.writerow ([f"Average  Change: ${str(avg_diff)}",""])
    writer.writerow ([f"Greatest Increase in Profits: {Increase_month} ({str(Increase_Amt)})",""])
    writer.writerow ([f"Greatest Decrease in Profits: {Decrease_month} ({str(Decrease_Amt)})",""])
    

