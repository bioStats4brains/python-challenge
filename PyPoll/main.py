# Welcome message to test the output! 
msg = "Start on the second challenge: PyPoll!"
print(msg)

# Import dependencies.
import os
import csv
import pandas as pd

# Read in data. 
election_df = pd.read_csv("PyPoll/Resources/election_data.csv")
print(election_df.head())

# Output the total number of votes cast.
num_votes = len(pd.unique(election_df["Ballot ID"]))

#f = open("output_pypoll_print.txt", "a")
print("The total number of votes cast is :", num_votes) #, file=f)

#Determine the percentage and number of votes for Charles. 
num_Charles = election_df[election_df["Candidate"] == 'Charles Casper Stockham'].shape[0]
per_Charles = round(num_Charles/num_votes*100, 3)
print("Charles Casper Stockham: ", per_Charles, "% (", num_Charles, ")")#, file=f)

#Determine the percentage and number of votes for Diana. 
num_Diana = election_df[election_df["Candidate"] == 'Diana DeGette'].shape[0]
per_Diana = round(num_Diana/num_votes*100, 3)
print("Diana DeGette: %", per_Diana, "% (", num_Diana, ")")#, file=f)

#Determine the percentage and number of votes for Diana. 
num_Raymon = election_df[election_df["Candidate"] == 'Raymon Anthony Doane'].shape[0]
per_Raymon = round(num_Raymon/num_votes*100, 3)
print("Raymon Anthony Doane: %", per_Raymon, "% (", num_Raymon, ")")#, file=f)

#Determine the winner based on max num.
#list_winnings = election_df["Candidate"].value_counts()
#print(list_winnings)

#print(list_winnings[max(list_winnings)])
#f.close()