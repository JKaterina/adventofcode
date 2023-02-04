with open("inputs/input_ch7.txt") as f:
    data = [s.strip('\n') for s in list(f)]

# import re
# digit_pattern = '\d+'
# word_pattern = '\w+'


dir_dict = {"/main" : 0}
current_path = "/main"

for line in data:

    # case 1: line is a command (starts with $)
    if line[0] == "$":
        if "ls" in line: # do nothing when directories are listed
            pass
        elif "cd" in line:
            # case 1.1: directory is main
            if "/" in line:
                current_path = "/main"
            # case 1.2: go up to the previous diretcory ($ cd ..)
            elif ".." in line:
                # path name before the last "/"
                current_path = current_path[0:current_path.rfind("/")]
            # case 1.3: add new directory name to dir dictionary
            else:
                dir_name = line[5:]
                current_path = current_path + "/" + dir_name
                dir_dict[current_path] = 0  # add path to dict

    # case 2: line starts with dir
    elif "dir" in line:
        pass

    # case 3: line is a file
    else:
        # digits stored before the space character
        size = int(line[:line.rfind(" ")])

        dir_temp = current_path
        for i in range(current_path.count("/")):
            # update the size of the current path
            dir_dict[dir_temp] += size
            # update the size of all paths containing current path
            dir_temp = dir_temp[:dir_temp.rfind("/")]  # find the index of the last "/"

#print(dir_dict)

### PART 1 ###

# only leave directories with at most 100,000
dir_dict_sorted = {}

for k, v in dir_dict.items():
    if v <= 100000:
        dir_dict_sorted[k] = v

print(f"The total size of all directories below 100,000 is {sum(dir_dict_sorted.values())}")

### PART 2 ###

# space missing for the upgrade
missing_space = 30000000 - (70000000 - dir_dict["/main"])


big_values = []

# for k, v in dir_dict.items():
#     if missing_space <= v:
#         big_values.append(dir_dict[k])

for dir in dir_dict:
    if missing_space <= dir_dict[dir]:
        big_values.append(dir_dict[dir])

print(min(big_values))