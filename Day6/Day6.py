with open('input.txt') as f:
    inp = f.read().strip()

# TASK 1 #
# Convert to set to only get unique values. If there is 4 unique, we have our position.
char_buffer = []
position = 0
for character in inp:
    if(len(char_buffer) < 4):
        char_buffer.append(character)
        position += 1
        continue

    if(len(set(char_buffer)) == 4):
        break

    char_buffer.pop(0)
    char_buffer.append(character)
    position += 1

print(position)

# TASK 2 #
# Same as Task 1, with 14 unique characters.
char_buffer = []
position = 0
for character in inp:
    if(len(char_buffer) < 14):
        char_buffer.append(character)
        position += 1
        continue

    if(len(set(char_buffer)) == 14):
        break

    char_buffer.pop(0)
    char_buffer.append(character)
    position += 1

print(position)