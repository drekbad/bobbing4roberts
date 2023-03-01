import re

# Create an empty list to store all names from the input file
allNames = []

# Open the input file and read each line
with open('input.txt', 'r') as inputFile:
    for line in inputFile:
        # Strip any whitespace from the line and add the name to allNames
        allNames.append(line.strip())

# Create an empty dictionary to store name pairs from namePairs.txt
namePairs = {}

# Open the namePairs.txt file and read each line
with open('namePairs.txt', 'r') as pairsFile:
    for line in pairsFile:
        # Split the line into two names, separated by a comma
        name1, name2 = line.strip().split(',')
        # Add the name pair to the dictionary, with both names in lowercase
        namePairs[name1.lower()] = name2.lower()
        namePairs[name2.lower()] = name1.lower()

# Create an empty list to store all possible usernames
usernames = []

# Loop through each name in allNames
for name in allNames:
    # Split the name into first and last names
    firstName, lastName = name.split()

    # Create the first possible username (first names only)
    usernames.append(firstName.lower())

    # Create the second possible username (first initial of first name followed by surname)
    usernames.append(firstName[0].lower() + lastName.lower())

    # Create the third possible username (first name followed by a period followed by surname)
    usernames.append(firstName.lower() + '.' + lastName.lower())

    # Create the fourth possible username (first name followed by first initial of surname)
    usernames.append(firstName.lower() + lastName[0].lower())

    # Check if the first name in lowercase is in the namePairs dictionary
    if firstName.lower() in namePairs:
        # If it is, add the opposite name for that record to allNames
        allNames.append(namePairs[firstName.lower()].title())

# Remove any duplicates from the usernames list
usernames = list(set(usernames))

# Print out all possible usernames
for username in usernames:
    # Remove any non-alphanumeric characters from the username
    username = re.sub(r'\W+', '', username)
    print(username)
