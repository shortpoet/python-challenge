import os
import csv

voterId = []
county = []
candidate = []

pyPoll_csv = os.path.join("..", "Resources", "election_data.csv", )

def load_file(filepath):
    with open(filepath, "r") as pollFileHandler:
        return pollFileHandler.read()

pollDict

    for row in csvreader:
        header = next(csvreader)
        voterId.append(row[0])
        totalVotes = len(voterId)
        candidate.append(row[2])
        
        #candidateList = set(candidate)
        #candidateList = uniqueFinder(candidate)
        #khanCount = candidate.count("Khan")
        #liCount = candidate.count("Li")
        #correyCount = candidate.count("Correy")
        #oTooleyCount = candidate.count("O'Tooley")
        #khanPercentage = round(int(khanCount) / int(totalVotes), 3)

#candidateList = uniqueFinder(candidate)
candidateDict = {}.fromkeys(candidate, 0)
for word in candidate:    
    candidateDict[row[2]] += 1

returnString = ( 
    f"\r\nElection Results\r\n__________________________"
    f"\r\n\r\nTotal Votes: {totalVotes}"
    f"\r\n__________________________"
    f"\r\nCandidate Results: {candidateDict}"
    #f"\r\nKhan: ({khanCount})"
    #f"\r\nCandidate List: {candidateList}"
    #f"\r\nKhan: {khanPercentage}% ({khanCount})"
    #f"\r\nCandidate List: {candidateList}"
                                            )
print(returnString)

output_file = os.path.join("Election Results.txt")

with open(output_file, "w", newline="") as datafile:
    returnString = ( 
    f"\r\nElection Results\r\n__________________________"
    f"\r\n\r\nTotal Votes: {totalVotes}"
    f"\r\n__________________________"
    f"\r\nCandidate Results: {candidateDict}"
    datafile.write(returnString)
