# Modules
import csv


#The total number of votes cast-rows
totalvotes = 0

with open("election_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader: 
        totalvotes = totalvotes + 1

print (totalvotes)


#A complete list of candidates who received votes

with open("election_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    Candidate = []
    for row in csvreader:
        if row[2] not in Candidate:
            Candidate.append(row[2]) 
        
print (Candidate)   

#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote 

#Creates dictionary to be used for candidate name and vote count.
candidate_votes = {}

#Sets variable, total votes, to zero for count.
total_votes = 0

with open("election_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
#creates dictionary from file using column 3 as keys, using each name only once.
#counts votes for each candidate as entries
#keeps a total vote count by counting up 1 for each loop (# of rows w/o header)
    for row in csvreader:
        #total_votes += 1
        total_votes = total_votes + 1
        if row[2] in candidate_votes.keys():
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1
        else:
            candidate_votes[row[2]] = 1
 
 #create empty list for candidates and his/her vote count
candidates = []
num_votes = []

#takes dictionary keys and values and, respectively, dumps them into the lists, 
# candidates and num_votes
for key, value in candidate_votes.items():
        candidates.append(key)
        num_votes.append(value)

#creates vote percent list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

#zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
         winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]
        
print (candidate_votes)
print (vote_percent)
print (winner_list)
