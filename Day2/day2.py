with open('input.txt') as f:
    lines = f.read().splitlines()

# Translate line to score.
dic = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

total_score = 0

# Add up score of all lines
for line in lines:
    total_score += dic[line]

print(total_score)