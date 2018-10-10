import os
import csv

voterId = []
county = []
candidate = []

def uniqueFinder(items):
    uniqueList = []
    for item in items:
        #uniqueList.append(item)
        if item not in uniqueList:
            uniqueList.append(item)
    return uniqueList

pyPoll_csv = os.path.join("..", "Resources", "election_data.csv", )

with open(pyPoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        header = next(csvreader)
        voterId.append(row[0])
        totalVotes = len(voterId)
        candidate.append(row[2])
        #candidateList = set(candidate)
        #candidateList = uniqueFinder(candidate)
        khanCount = candidate.count("Khan")
        liCount = candidate.count("Li")
        correyCount = candidate.count("Correy")
        oTooleyCount = candidate.count("O'Tooley")
        khanPercentage = round(int(khanCount) / int(totalVotes), 3)



returnString = ( 
    f"\r\nElection Results\r\n__________________________"
    f"\r\n\r\nTotal Votes: {totalVotes}"
    f"\r\n__________________________"
    f"\r\nKhan: ({khanCount})"
    f"\r\nKhan: {khanPercentage}% ({khanCount})"
    #f"\r\nCandidate List: {candidateList}"
                                            )
print(returnString)

