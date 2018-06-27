#!/usr/bin/env python

# import modules
import sys
import os
import csv


# import csv data
infilename = os.path.join("Resources", "budget_data.csv")

with open(infilename,'r',encoding='utf-8-sig') as infile:
    reader = csv.DictReader(infile)
    fin_data = list(reader)

# debug: take a quick look at the data    
#for row in fin_data:
#    print(row)    
    
n_months = len(fin_data)

prof_sum = 0
for i in range(n_months):
    prof_sum += int(fin_data[i]['Revenue'])

changes = []
for i in range(1,n_months):
    tmp_change = int(fin_data[i]['Revenue']) - \
                 int(fin_data[i-1]['Revenue'])
    changes.append( ( fin_data[i]['Date'], tmp_change ) )

# average change:
av_change = 0.0

# average change magnitude:
av_change_mag = 0.0

# greatest increase:
max_change = ['',-100000000]

# greatest decrease:
min_change = ['',100000000]

for i in range(len(changes)):
    print(changes[i][1])
    av_change += changes[i][1]
    av_change_mag += abs(changes[i][1])
    if changes[i][1] > max_change[1]:
        max_change[1] = changes[i][1]
        max_change[0] = changes[i][0]

    if changes[i][1] < min_change[1]:
        min_change[1] = changes[i][1]
        min_change[0] = changes[i][0]

    
av_change /= len(changes)
av_change_mag /= len(changes)

print("")
print("Financial Analysis")
print("-"*30)
print(f"Total Months: {n_months}")
print(f"Total: ${prof_sum}")
print(f"Average Change: ${av_change:.2f}")
print(f"Average Change Magnitude: ${av_change_mag:.2f}")      
print(f"Greatest Increase in Profits: {max_change[0]} (${max_change[1]})")
print(f"Greatest Decrease in Profits: {min_change[0]} (${min_change[1]})")
print("")
print("Note: The large change magnitude together with the small \n"\
      "average change suggests that the business profits are fluctuating\n"\
      "wildly from month to month. This indicates trouble.")
print("")
