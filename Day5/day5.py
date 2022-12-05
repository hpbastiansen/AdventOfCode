import re
import copy

with open('input.txt') as f:
    inp = f.read().splitlines()

class Instruction:
    def __init__(self, amount, at, to):
        self.amount = amount
        self.at = at
        self.to = to

state_pattern = re.compile(r"[A-Z]")
instruction_pattern = re.compile(r"\d+")
state_from_top = []
instructions = []
state_done = False

# Fill in the state in reversed order (top to bottom) first, then store the instructions.
for line in inp:
    # Splitt i state og instruksjoner, for state lagre i temp list
    if(line.startswith(' 1   2 ') or line == ''):
        state_done = True
        continue

    if(not state_done):
        state = [line[i:i+4] for i in range(0, len(line), 4)]
        state_line = []
        for index, item in enumerate(state):
            item = re.search(state_pattern, item)
            if(item != None):
                state_line.append([index, item[0]])

        if(len(state_line) > 0):
                state_from_top.append(state_line)
    else:
        instruction = re.findall(instruction_pattern, line)
        instructions.append(Instruction(int(instruction[0]), int(instruction[1]), int(instruction[2])))

state = [[] for i in range(9)]
for line in reversed(state_from_top):
    for item in line:
        state[item[0]].append(item[1])

# Make a deep copy of state for task 2
state_copy = copy.deepcopy(state)

# TASK 1 #
# Remove and place crates one at a time.
for instruction in instructions:
    for i in range(instruction.amount):
        item = state[instruction.at-1].pop()
        state[instruction.to-1].append(item)

out_string = ''
for line in state:
    out_string += line[len(line)-1]

print(out_string)

# TASK 2 #
# Slice the amount of boxes that should be moved.
for instruction in instructions:
    moved_crates = state_copy[instruction.at-1][-instruction.amount:]
    state_copy[instruction.at-1] = state_copy[instruction.at-1][0:-instruction.amount]
    state_copy[instruction.to-1].extend(moved_crates)

out_string = ''
for line in state_copy:
    out_string += line[len(line)-1]

print(out_string)