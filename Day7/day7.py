import re

# Directory class. Can get size of all subdirectories recursively.
class Directory:
    def __init__(self, path):
        self.path = path
        self.directories = []
        self.filesize = 0

    def get_total_size(self):
        total = self.filesize
        for directory in self.directories:
            total += directory.get_total_size()

        return total

with open('input.txt') as f:
    inp = f.read().splitlines()

directories = []
current_directory = None

# Create the data structure of the file system.
# If moving up a directory, we change the path and set the current directory to the new one.
# Else, we create a new directory with the new path.
# If the line starts with a number we add that to the directories filesize.
# Otherwise we can ignore the line.
for line in inp:
    if(line.startswith("$ cd")):
        path = line.split(" ")[2]
        if(path == ".."):
            split = current_directory.path[0:-1].rindex("/")
            for directory in directories:
                if(directory.path == current_directory.path[0:split+1]):
                    current_directory = directory
                    break
        else:
            if(current_directory == None):
                new_path = path
            else:
                new_path = current_directory.path + path + "/"
            new_directory = Directory(new_path)
            if(current_directory != None):
                current_directory.directories.append(new_directory)
            directories.append(new_directory)
            current_directory = new_directory
    elif(re.match(r'^[0-9]+', line)):
        current_directory.filesize += int(line.split(" ")[0])

# TASK 1 #
# Get total size of all directories, add to total if under 100000.
total_size = 0
for directory in directories:
    new_size = directory.get_total_size()
    if(new_size <= 100000):
        total_size += new_size

print(total_size)

# TASK 2 #
# Find size needed to remove to install update. 
# Add all directories matching criteria to list and sort in ascending order.
total_system_size = 70000000
system_size_needed = 30000000
used_system_size = directories[0].get_total_size()
remaining_system_size = total_system_size - used_system_size
size_to_remove = system_size_needed - remaining_system_size

size_of_directories = []
for directory in directories:
    if(directory.get_total_size() >= size_to_remove):
        size_of_directories.append(directory.get_total_size())

size_of_directories.sort()
print(size_of_directories[0])