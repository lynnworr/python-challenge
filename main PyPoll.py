import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

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
print ('Total Votes:', row_count)

# Create an empty list to store candidate names

candidates = []

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    # Add each row's candidate name to the list
    csv_header = next(csvreader)

    for row in csvreader:
        candidates.append(row[2])

# Create a set to get unique list of candidates
unique_candidates = set(candidates)



# Print the list of candidates
print("List of Candidates: " + str(unique_candidates))


 
# Create empty dictionaries for each candidate's total votes and vote percentage

candidate_votes = {}
candidate_percentage = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip the header row
    csv_header = next(csvreader)

# Loop through each row in the csv
    for row in csvreader:
    # Retrieve the candidate name from each row
        name = row[2]
# If the candidate is not in the dictionary, add them and set the value to 1
        if name not in candidate_votes:
            candidate_votes[name] = 1
    # If the candidate is already in the dictionary, increment their vote count by 1
        else:
            candidate_votes[name] += 1
# Calculate the total number of votes cast
    total_votes = sum(candidate_votes.values())
    # Calculate the percentage of votes for each candidate
    for name in candidate_votes:
        candidate_percentage[name] = round((candidate_votes[name] / total_votes) * 100, 2)  

     # Print out the total number of votes each candidate won and their percentage
    for candidate in candidate_votes:
        print(f"{candidate}: {candidate_votes[candidate]} ({candidate_percentage[candidate]}%)")
    
  
# Find the candidate who won the most votes
most_votes = 0
winner = ""

for candidate in candidate_votes:
    if candidate_votes[candidate] > most_votes:
        most_votes = candidate_votes[candidate]
        winner = candidate

# Print out the winner
print(f"The winner is {winner} with {most_votes} votes!")

