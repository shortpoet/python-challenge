import os
import csv
#import operator

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

#def uniqueFinder(items):
#    uniqueList = []
#    uniqueList = [item for item in items if item not in uniqueList]
#    return uniqueList



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
        
       

candidateList = uniqueFinder(candidate)
khanCount = candidate.count("Khan")
liCount = candidate.count("Li")
correyCount = candidate.count("Correy")
oTooleyCount = candidate.count("O'Tooley")
khanPercentage = round((int(khanCount) / int(totalVotes) * 100), 3)
liPercentage = round((int(liCount) / int(totalVotes) * 100), 3)
correyPercentage = round((int(correyCount) / int(totalVotes) * 100), 3)
oTooleyPercentage = round((int(oTooleyCount) / int(totalVotes) * 100), 3)

#resultsList = [khanCount, liCount, correyCount, oTooleyCount]
#result = max(resultsList)

#candidateDict = {}.fromkeys(candidate, 0)
#for word in candidate:    
#    candidateDict[row[2]] += 1

resultsDict = {
    "Khan" : khanCount,
    "Li" : liCount,
    "Correy" : correyCount,
    "O'Tooley" : oTooleyCount}
#result = max(resultsDict.values())
result = max(resultsDict, key=resultsDict.get)
#result = max(resultsDict.items(), key=lambda x: x[1])
#result = max(resultsDict.iteritems(), key=operator.itemgetter(1))[0]

returnString = ( 
    f"\r\nElection Results\r\n__________________________\r\n"
    f"\r\nTotal Votes: {totalVotes}"
    f"\r\n__________________________\r\n"
    #f"\r\nCandidate Results: {candidateDict}"
    #f"\r\nKhan: ({khanCount})"
    #f"\r\nCandidate List: {candidateList}"
    f"\r\nKhan: {khanPercentage}% ({khanCount})"
    f"\r\nLi: {liPercentage}% ({liCount})"
    f"\r\nCorrey: {correyPercentage}% ({correyCount})"
    f"\r\nO'Tooley: {oTooleyPercentage}% ({oTooleyCount})"
    f"\r\n__________________________\r\n"
    f"\r\nWinner: {result}"

    #f"\r\nCandidate List: {candidateList}"
                                            )
print(returnString)

output_file = os.path.join("Election Results.txt")

with open(output_file, "w", newline="") as datafile:
    datafile.write( 
    f"\r\nElection Results\r\n__________________________\r\n"
    f"\r\nTotal Votes: {totalVotes}"
    f"\r\n__________________________\r\n")

for k,v in pollResults.items():
    percentage = (v / totalVotes) * 100
    datafile.writelines(f"{str(k)}: {str(v)} ({round(percentage, 3)})")    
    
    #datafile.write(
    #f"\r\n__________________________\r\n"
    #f"\r\nWinner: {electionWinner, pollResults[electionWinner]}")
