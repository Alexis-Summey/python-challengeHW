import csv
import os

with open('budget.csv', newline='') as csvfile:
  
  budget_csv = csv.reader(csvfile, delimiter=',')
  
 # for row in budget_csv:
   
  #  print(', '.join(row))
  
  csvreader = csv.reader(csvfile, delimiter=",")
  next(csvreader)
  
    
  # Looping
  # Naming Variables
  
  months = 0
  total_profit = 0.0
  profit_change_total = 0.0
  final_profit = 0.0
  current_profit = 0.0
  change_profit = 0.0
  greatest_profit = 0.0
  smallest_profit = 0.0
  
  #beginning the loops
  
  for row in csvreader:
    for col in csvreader:
    
      months = months + 1
    
      total_profit = float(row[1],col[2])
    
      current_profit = row[1][0]
      
      change_profit = float(current_profit) - float(final_profit)
      
      profit_change_total = profit_change_total + change_profit
      
      final_profit = row[1]
      
    if change_profit > greatest_profit:
      greatest_profit = change_profit
      greatest_profit_month = row[0]
    
    if change_profit < smallest_profit:
      smallest_profit = change_profit
      smallest_profit_month = row[0]
      
    # Average change in profit
    
  avg_change_profit = profit_change_total/months
  
  
  # Displaying my answers
  
  print("Financial Analysis")
  print("__________________________________")
  print(f"Total Months: {months}")
  print(f"Total Profit: $[round(total_profit,2)]")
  print("Average Change in Profit: $[round(avg_change_profit,2)]")
  print("Greatest Increase in Profits: [greatest_profit_month] $[round(greatest_profit,2)]")
  print("Greatest Decrease in Profits: [smallest_profit_month] $[round(smallest_profit,2)]") 
