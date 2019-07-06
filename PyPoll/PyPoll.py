import csv

with open('PyPoll.csv', newline='') as csvfile:
  
  csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  csv_header = next(csvreader)
   
  # Creating variables and lists
  
  totalcandidates = []
  votecount = []
  totalvotes = 0
  votecountofwinner = 0
  
  # Loops needed
  for row in csvreader:
    totalvotes += 1
    
    if(row[2] not in candidates):
      candidates.append(row[2])
      votecount.append(0)
    
    candidateindex = candidates.index(row[2])
    votecount [candidateindex] += 1
    
  
  print("Election Results")
  print("____________________________")
  print(f"Total Votes: [totalvotes]")
  print("____________________________")
  
  for x in range(len(candidates)):
    percentvote = round((votecount[x]/totalvotes)*100,3)
    print(f"{candidates[x]}: {percentvote}% ({votecount[x]})")
    
    if (votecountofwinner<votecount[x]):
      votecountofwinner = votecount[x]
      winner = candidates[x]
      
  print("____________________________")
  print(f"Winner:{winner}")
  print("____________________________")

