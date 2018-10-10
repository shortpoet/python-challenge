import os
import csv

pollData = []

pyPoll_csv = os.path.join("..", "Resources", "election_data.csv", )

with open(pyPoll_csv, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        voterId = row["Voter ID"]
        county = row["County"]
        candidate = row["Candidate"]
        pollData.append(
            {
                "Voter ID": row["Voter ID"],
                "County": row["County"],
                "Candidate": row["Candidate"],
            }
        )
       
       
#khanPercentage = round((int(khanCount) / int(totalVotes) * 100), 3)
#liPercentage = round((int(liCount) / int(totalVotes) * 100), 3)
#correyPercentage = round((int(correyCount) / int(totalVotes) * 100), 3)
#oTooleyPercentage = round((int(oTooleyCount) / int(totalVotes) * 100), 3)


#candidateDict = {}.fromkeys(candidate, 0)
#for word in candidate:    
#    candidateDict[row[2]] += 1

#resultsDict = {
#    "Khan" : khanCount,
#    "Li" : liCount,
#    "Correy" : correyCount,
#    "O'Tooley" : oTooleyCount}
#result = max(resultsDict.values())
#result = max(resultsDict, key=resultsDict.get)
#result = max(resultsDict.items(), key=lambda x: x[1])

returnString = ( 
    f"\r\nElection Results\r\n__________________________\r\n"
    #f"\r\nTotal Votes: {totalVotes}"
    f"\r\n__________________________\r\n"
    #f"\r\nCandidate Results: {candidateDict}"
    #f"\r\nKhan: ({khanCount})"
    #f"\r\nCandidate List: {candidateList}"
    #f"\r\nKhan: {khanPercentage}% ({khanCount})"
    #f"\r\nLi: {liPercentage}% ({liCount})"
    #f"\r\nCorrey: {correyPercentage}% ({correyCount})"
    #f"\r\nO'Tooley: {oTooleyPercentage}% ({oTooleyCount})"
    f"\r\n__________________________\r\n"
    #f"\r\nWinner: {result}"

    f"\r\nCandidate List: {pollData}"
                                            )
print(returnString)

output_file = os.path.join("Election Results.txt")

with open(output_file, "w", newline="") as datafile:
    datafile.write(returnString)
