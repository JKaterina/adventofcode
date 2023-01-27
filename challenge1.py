# load the file as list
with open("inputs/input_ch1.txt") as f:
    input1 = list(f)

# remove '\n' --> empty string is a batch separator
a = [s.strip('\n') for s in input1]

# transform string to digits
b = [int(s) if s.isdigit() else '' for s in a]

# roll over the list until the next separator and sum digits in each batch
from itertools import groupby
res = [list(sub) for ele, sub in groupby(b, key = bool) if ele]
        
all_sums = [sum(a_list) for a_list in res]
print(max(all_sums))