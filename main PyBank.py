import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

row_count = 0


with open(csvpath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        row_count +=1


# Print the total rows for the column
print ('Total Months:', row_count)

total = 0
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader) 
    for row in reader:
        total += int(row[1])

print("Total: $" + str(total))



row_count = 0
total_change = 0

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    prev = int(next(reader)[1]) # set the prev value to the first row of data
    for row in reader:
        row_count += 1
        total_change += int(row[1]) - prev
        prev = int(row[1])

# Calculate the average of those changes
average_change = total_change / (row_count)

print("Average Change: $" + str(round(average_change,2)))


# Find the greatest increase in profits
greatest_inc = 0
greatest_inc_date = ''
total = 0
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    prev = int(next(reader)[1])
    for row in reader:
        total += int(row[1])
        if int(row[1]) - prev > greatest_inc:
            greatest_inc = int(row[1]) - prev
            greatest_inc_date = row[0]
        prev = int(row[1])

print("Greatest Increase in Profits:", greatest_inc_date, "($" + str(greatest_inc) + ")")

# Find the greatest decrease in profits
greatest_dec = 0
greatest_dec_date = ''
total = 0
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    prev = int(next(reader)[1])
    for row in reader:
        total += int(row[1])
        if int(row[1]) - prev < greatest_dec:
            greatest_dec = int(row[1]) - prev
            greatest_dec_date = row[0]
        prev = int(row[1])

print("Greatest Decrease in Profits:", greatest_dec_date, "($" + str(greatest_dec) + ")")

