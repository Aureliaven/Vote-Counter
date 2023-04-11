import random
import csv

national_1 = "Alice"
national_2 = "Bob"
national_3 = "Chris"
local_2 = ["Devon","NJ"]
local_3 = ["Ethan", "NJ"]
local_4 = ["Fran", "PA"]
local_5 = ["Greg", "PA"]
local_6 = ["Heather", "CT"]
local_1 = ["Iain","CT"]
votes = [["voter_number","state", "national_choice", "local_choice", 
"reserve_national_choice"]]

for i in range(1,101):
 national = random.sample([national_1, national_2, national_3],2)
 local_choice = random.choice([[local_1, local_2], [local_3, local_4], [local_5, 
local_6]])
 local = random.choice(local_choice)
 vote = [i, local[1],national[0], local[0],national[1]]
 votes.append(vote)
with open("votes.csv", "w") as file:
 writer = csv.writer(file)
 writer.writerows(votes)