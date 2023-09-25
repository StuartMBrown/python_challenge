#Import modules
import os
import csv
#Prime data and rundown
results_data_csv=os.path.join("Resources", "election_data.csv")
results_txt=os.path.join("certifiedanalysis", "certifiedanalysis.txt")
#Define candidates and their tallies
allvotes=0
gopvotes=0
gopperc=0
demvotes=0
demperc=0
libvotes=0
libperc=0
cand1="Charles Casper Stockham"
cand2="Diana DeGette"
cand3="Raymon Anthony Doane"
#Retrieve the results
with open(results_data_csv) as results:
    csvreader=csv.reader(results)
    header= next(csvreader)
#Count all votes and candidate-specific votes
    for row in csvreader:
        allvotes += 1
        if row[2] == cand1:
            gopvotes +=1
        if row[2] == cand2:
            demvotes +=1
        if row[2] == cand3:
            libvotes +=1
#Convert to percentages
gopperc=100*(gopvotes/allvotes)
demperc=100*(demvotes/allvotes)
libperc=100*(libvotes/allvotes)
#Define a fickle winner based on, say, a possible outcome-altering recount
victor= max(gopperc,demperc,libperc)
if victor == gopperc:
    victor=cand1
if victor == demperc:
    victor=cand2
if victor == libperc:
    victor = cand3
#Prepare rundown for txt
outcome = f"""
Election Results
-------------------------
Total Votes: {allvotes}
-------------------------
Charles Casper Stockham: {gopperc:.3f}% ({gopvotes})
Diana DeGette: {demperc:.3f}% ({demvotes})
Raymon Anthony Doane: {libperc:.3f}% ({libvotes})
-------------------------
Winner: {victor}
-------------------------
"""
#Export rundown to txt
print(outcome)
with open(results_txt, "w") as certified:
    certified.write(outcome)