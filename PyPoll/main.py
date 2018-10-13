import os
import csv
from collections import Counter
from collections import defaultdict

pollData = []
candidate = []

pyPoll_csv = os.path.join("..", "Resources", "election_data.csv", )

with open(pyPoll_csv, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader, None)
    for row in csvreader:               
        candidate.append(row[2])

totalVotes = len(candidate)

#https://www.youtube.com/watch?v=dt4JCYtc1dE
pollResults = defaultdict(int)
for name in candidate:
    pollResults[name] += 1

#https://stackoverflow.com/questions/26871866/print-highest-value-in-dict-with-key?lq=1
electionWinner = max(pollResults, key=pollResults.get)

print( 
    f"\r\nElection Results\r\n__________________________\r\n"
    f"\r\nTotal Votes: {totalVotes}"
    f"\r\n__________________________\r\n\r\n")

#can you place for loop into return string variable for printing ?
for k,v in pollResults.items():
    percentage = (v / totalVotes) * 100
    print(f"{str(k)}: {str(v)} ({round(percentage, 3)})")    


print(
    f"\r\n__________________________\r\n"
    f"\r\nWinner: {electionWinner, pollResults[electionWinner]}")

output_file = os.path.join("Election Results.txt")

with open(output_file, "w", newline="") as datafile:
    datafile.write(
    f"\r\nElection Results\r\n__________________________\r\n"
    f"\r\nTotal Votes: {totalVotes}"
    f"\r\n__________________________\r\n\r\n")
    for k,v in pollResults.items():
        percentage = (v / totalVotes) * 100
        datafile.writelines(f"{str(k)}: {str(v)} ({round(percentage, 3)})\r\n")
    datafile.write(
    f"\r\n__________________________\r\n"
    f"\r\nWinner: {electionWinner, pollResults[electionWinner]}")   

    

