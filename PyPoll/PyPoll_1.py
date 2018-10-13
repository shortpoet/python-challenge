import os
import csv
from collections import Counter
from collections import defaultdict

pollData = []

pyPoll_csv = os.path.join("..", "Resources", "election_data.csv", )

with open(pyPoll_csv, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #voterId = row["Voter ID"]
        #county = row["County"]
        candidate = row["Candidate"]
        pollData.append(
            {
                #"Voter ID": row["Voter ID"],
                #"County": row["County"],
                "Candidate": row["Candidate"],
            }
        )

pollResults = defaultdict(int)
for name in candidate:
    pollResults[name] += 1

totalVotes = len(pollData)

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
    f"\r\nCandidate Results: {pollResults}"
    #f"\r\nKhan: ({khanCount})"
    #f"\r\nCandidate List: {candidateList}"
    #f"\r\nKhan: {khanPercentage}% ({khanCount})"
    #f"\r\nLi: {liPercentage}% ({liCount})"
    #f"\r\nCorrey: {correyPercentage}% ({correyCount})"
    #f"\r\nO'Tooley: {oTooleyPercentage}% ({oTooleyCount})"
    f"\r\n__________________________\r\n"
    #f"\r\nWinner: {result}"

    #f"\r\nCandidate List: {pollData[1]}"
                                            )
print(returnString)

output_file = os.path.join("Election Results.txt")

with open(output_file, "w", newline="") as datafile:
    datafile.write(returnString)
