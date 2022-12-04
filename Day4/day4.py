class Area:
    def __init__(self, start, end):
        self.start = start
        self.end = end

with open('input.txt') as f:
    inp = f.read().splitlines()

# Split all sections into pairs, recording their start and end points.
pairs = []
for line in inp:
    areas = line.split(',')
    new_pair = []
    for area in areas:
        area_range = area.split('-')
        new_pair.append(Area(int(area_range[0]), int(area_range[1])))
    pairs.append(new_pair)

# TASK 1 #
# Compare all pairs of areas. If they start with the same section, one is guaranteed to contain the other.
result = 0
for pair in pairs:
    if(pair[0].start == pair[1].start):
        result += 1
    elif(pair[0].start <= pair[1].start):
        if(pair[0].end >= pair[1].end):
            result += 1
    else:
        if(pair[1].end >= pair[0].end):
            result += 1

print(result)

# TASK 2 #
result = 0
for pair in pairs:
    for i in range(pair[0].start, pair[0].end+1):
        if i in range(pair[1].start, pair[1].end+1):
            result += 1
            break

print(result)