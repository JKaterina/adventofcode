# load the file as list
with open("inputs/input_ch1.txt") as f:
    input1 = list(f)

### DATA CLEANING ###

# remove '\n' --> empty string is a batch separator
a = [s.strip('\n') for s in input1]

# transform string to digits
b = [int(s) if s.isdigit() else '' for s in a]

# split the list into sublists based on empty string separator
from itertools import groupby
res = [list(sub) for ele, sub in groupby(b, key = bool) if ele]

### PART 1: FIND THE HIGHEST SUM ###

# sum all elements in each sublist and find the highest value
all_sums = [sum(a_list) for a_list in res]
print(max(all_sums))

### PART 2: FIND THE TOP THREE AND CALCULATE THEIR SUM ###

# sort the list of all sums and take the top 3
top_sums = sorted(all_sums, reverse = True)

# find the sum of the top three
print(sum(top_sums[:3]))