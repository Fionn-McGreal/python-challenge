import csv
import os
File = os.path.join('Resources','election_data.csv')
candidate_dict={}
total_votes = 0
percentage_votes = {}
winning_votes = 0
winner = ''
with open (File) as data:
    reader = csv.reader(data)
    header = next(reader)
    for row in reader:
        total_votes += 1
        if row [2] in candidate_dict:
            candidate_dict [row[2]] += 1
        else: 
            candidate_dict [row[2]] = 1 
print (candidate_dict)
for k,v in candidate_dict.items():
    percentage_votes [k] = v/total_votes *100
    if v > winning_votes: 
        winning_votes = v 
        winner = k
print (percentage_votes)
print (winner)
print (winning_votes)
with open ('output.txt', 'w') as txt_file: 
    print (candidate_dict, percentage_votes,winner,winning_votes,file=txt_file)






