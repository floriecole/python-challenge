# Modules
import csv

#The total number of months included in the dataset-rows
#The net total amount of "Profit/Losses" over the entire period-total revenue
total=0
totalmonths=0

with open("budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
            totalmonths = totalmonths + 1
#           Don't we have to reference a row for the totalmonths counter like we do for the total counter below?
#           totalmonths = totalmonths + int(row[0])
            total = total + int(row[1])
    print (totalmonths)
    print(total)
   
#The average of the changes in "Profit/Losses" over the entire period 
#The greatest increase in profits (date and amount) over the entire period 
#The greatest decrease in losses (date and amount) over the entire period
#total of difference between all rows of column "Profit/Losses" to get total revenue change. Also max revenue change and min revenue change

with open("budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    date = []
    differences_list = []
    previous_value = 0
    for row in csvreader: 
        current_value = int(row[1])
        difference = current_value - previous_value
        previous_value = current_value

        date.append(row[0])
        differences_list.append(difference)
#print (differences_list)

avg_change = sum(differences_list)/len(differences_list)

max_change = max(differences_list)

min_change = min(differences_list)

max_change_date = str(date[differences_list.index(max_change)])
min_change_date = str(date[differences_list.index(min_change)])

print("Average Change: $", round(avg_change))
print("Greatest Increase in Profits:", max_change_date,"($", max_change,")")
print("Greatest Decrease in Losses:", min_change_date,"($", min_change,")")
