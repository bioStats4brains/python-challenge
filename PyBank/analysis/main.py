
# Welcome message to test the output! 
msg = "Enter into the world of coding!"
print(msg)

# Import dependencies.
import os
import csv
import pandas as pd

# Read in data. 
budget_df = pd.read_csv("PyBank/Resources/budget_data.csv")

print(budget_df.head())

#The total number of months included in the dataset.
num_months = len(pd.unique(budget_df["Date"]))

f = open("PyBank/output_pybank_print.txt", "a")
print("The total number of months is :", num_months, file=f)

#The net amount of profit/losses. 
profit = budget_df.loc[budget_df["Profit/Losses"] > 0, 'Profit/Losses'].sum()
losses = budget_df.loc[budget_df["Profit/Losses"] < 0, 'Profit/Losses'].sum()
net_profit = profit + losses 

print("The net profit/losses is $", net_profit, ".", file=f)

#The greatest increase/decrease in profits happened on __ and for __ much. 
max_date = budget_df.loc[budget_df["Profit/Losses"].idxmax(), 'Date']
max_profit = budget_df.loc[budget_df["Profit/Losses"].idxmax(), 'Profit/Losses']
print("The greatest increase in profits happened on: ", max_date, " ($", max_profit, ").", file=f)

min_date = budget_df.loc[budget_df["Profit/Losses"].idxmin(), 'Date']
min_profit = budget_df.loc[budget_df["Profit/Losses"].idxmin(), 'Profit/Losses']
print("The greatest decrease in profits happened on: ", min_date, " ($", min_profit, ").", file=f)

f.close()