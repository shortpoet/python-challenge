import os
import csv

pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

def pl_total(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total 

def pl_maximum(numbers):
    maximum = 0.0
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

def pl_minimum(numbers):
    minimum = 0.0
    for number in numbers:
        if number > minimum:
            minimum = number
    return minimum


month_entries = []
profit_loss = []

with open(pybank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:   
        month_entries.append(row[0])
        profit_loss.append(int(row[1]))
        months = len(month_entries)
        total = pl_total(profit_loss)
        total = sum(profit_loss)
        average = total / months
        maximum = max(profit_loss)
        maximum = pl_maximum(profit_loss)
        minimum = min(profit_loss)
        minimum = pl_minimum(profit_loss)

       

print(f"Financial Analysis\n__________________________\n")
print(f"Total Months: {months}")
print(f"Total: {total}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profits: {maximum}")
print(f"Greatest Decrease in Profits: {minimum}")

output_file = os.path.join("")