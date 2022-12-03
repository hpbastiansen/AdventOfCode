import re

with open('input.txt') as f:
    input = f.read().splitlines()

# TASK 1 #
# Find any character from the first rucksack in the second.
# Translate from a-zA-Z to priority and sum up.
result = 0

rucksacks = []
for line in input:
    rucksacks.append([line[:int(len(line)/2)], line[int(len(line)/2):]])

for rucksack in rucksacks:
    pattern = re.compile('[' + rucksack[0] + ']')
    match = re.search(pattern, rucksack[1])[0]
    if(match.isupper()):
        result += ord(match)-38
    else:
        result += ord(match)-96

print(result)

# TASK 2 #
# Use a similar method as in task 1 to find similar characters in first and second rucksack.
# Build a new RegEx to search the final rucksack.
# Translate to priority and sum up.
result = 0
for i in range(0, len(input), 3):
    pattern = re.compile('[' + input[i] + ']')
    matches = re.findall(pattern, input[i+1])
    matches.insert(0, '[')
    matches.append(']')
    newpattern = ''.join(matches)
    match = re.search(newpattern, input[i+2])[0]
    if(match.isupper()):
        result += ord(match)-38
    else:
        result += ord(match)-96

print(result)