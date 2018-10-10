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

#https://stackoverflow.com/questions/1679384/converting-python-dictionary-to-list
candidateResults = []
candidateResults = list(pollResults.keys())
voteResults = []
voteResults = list(pollResults.values())
electionResults = []
electionResults = list(pollResults.items())

#https://stackoverflow.com/questions/26871866/print-highest-value-in-dict-with-key?lq=1
electionWinner = max(pollResults, key=pollResults.get)



candidateLaterAlphabet = max(electionResults)

candidate1Percentage = round((int(voteResults[0]) / int(totalVotes) * 100), 3)
candidate2Percentage = round((int(voteResults[1]) / int(totalVotes) * 100), 3)
candidate3Percentage = round((int(voteResults[2]) / int(totalVotes) * 100), 3)
candidate4Percentage = round((int(voteResults[3]) / int(totalVotes) * 100), 3)


#totalVotes = len(pollData)

#pollResults = Counter(pollData)

#https://docs.python.org/3.3/library/collections.html?highlight=counter#collections.Counter.fromkeys
#c = Counter(pollData)
#pollResults = sum(c.values())

#https://stackoverflow.com/questions/16406329/python-dictionary-count-of-unique-values
#mergedDict = {}
#for i in pollData:
#    for k,v in i.items():
#        try:
#            c[k].append(v)
#        except KeyError:
#            c[k] = [v]
#
#for k,v in mergedDict.items():
#    print "{0}: {1}".format(k, len(set(v)))

#b =[j[0]] for i in pollData for j in i.items()]

#for k in list(set(b)):
#    print "{0}: {1}".format(k, b.count(k))

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
    f"\r\nTotal Votes: {totalVotes}"
    f"\r\n__________________________\r\n"
    #f"\r\nCandidate Results: {pollResults}"
    f"\r\n{candidateResults[0]}: {candidate1Percentage}% ({voteResults[0]})"
    f"\r\n{candidateResults[1]}: {candidate2Percentage}% ({voteResults[1]})"
    f"\r\n{candidateResults[2]}: {candidate3Percentage}% ({voteResults[2]})"
    f"\r\n{candidateResults[3]}: {candidate4Percentage}% ({voteResults[3]})"
    f"\r\n__________________________\r\n"
    f"\r\nWinner: {electionWinner, pollResults[electionWinner]}"
    f"\r\nCandidate Whose Surname Appears Last in Alphabetical Order: {candidateLaterAlphabet}"

    #f"\r\nCandidate List: {candidateResults[0]}"

#print(f"{pollResults['Correy']}")


                                            )
print(returnString)

output_file = os.path.join("Election Results.txt")

with open(output_file, "w", newline="") as datafile:
    datafile.write(returnString)
