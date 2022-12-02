with open('input1.txt') as f:
    lines = f.read().splitlines()

highest_cals = [0, 0, 0]
current_cal = 0

# Check highest cals from highest to lowest.
# If replacing, check again with the replaced value.
def check_cals(new):
    for index, cal in enumerate(highest_cals):
            if(new > cal):
                check = highest_cals[index]
                highest_cals[index] = new
                check_cals(check)
                break

# Add up all cals until empty line
for line in lines:
    if(line == ''):
        check_cals(current_cal)
        current_cal = 0
    else:
        current_cal += int(line)

# Sum all 3 highest calories
sum = 0
for cal in highest_cals:
    sum += cal

print(sum)