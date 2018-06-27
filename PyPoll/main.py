#!/usr/bin/env python
import sys
import os
import csv

# import csv data
infilename = os.path.join("Resources", "election_data.csv")

with open(infilename,'r',encoding='utf-8-sig') as infile:
    reader = csv.DictReader(infile)
    poll_data = list(reader)

# make sure nobody voted more than once
voteids = [ x['Voter ID'] for x in poll_data ]
unique_voteids = list(set(voteids))
if len(unique_voteids) < len(voteids):
    raise Exception("Voter Fraud!!!")
    
# total # of votes cast
n_votes = len(poll_data)

# list of candidates
cands = [ x['Candidate'] for x in poll_data ]
cands = list(set(cands))

# make a dict with entries for each candidate for vote tally and
# initialize to zero
md = {}
for cand in cands:
    md[cand] = 0

# count votes for each candidate
for vote in poll_data:
    md[vote['Candidate']] += 1

# make a list, then sort it
result_list = []
for key,value in md.items():
    result_list.append([key,value])

result_list.sort(key=lambda x:x[1], reverse=True)
    
# set up results list
results = []
results.append("")
results.append("Election Results")
results.append("-"*30)
results.append(f"Total Votes: {n_votes}")
for cand in result_list:
    results.append(f"{cand[0]}: {cand[1]/n_votes*100:.3f}% ({cand[1]})")
results.append("-"*30)
results.append(f"Winner: {result_list[0][0]}")
results.append("-"*30)

# print to stdout
for line in results:
    print(line)

# print to file
with open('election_results.txt','w') as outfile:
    for line in results:
        outfile.write(line+'\n')


                    
