### PART 1 ###

# load the file as dataframe
import pandas as pd
data = pd.read_csv('inputs/input_ch3.txt', names = ['Initial String'])

# split each string into two parts
data['part_1'] = data['Initial String'].apply(lambda s: s[:len(s)//2])
data['part_2'] = data['Initial String'].apply(lambda s: s[len(s)//2:])

# find a matching element
def find_match(str_a, str_b):
    for a in str_a:
        for b in str_b:
            if a==b:
                return b

data['matching_element'] = data.apply(lambda x: find_match(x.part_1, x.part_2), axis=1)

# assign priorities

# create a dictionary of priorities
import string
priority_dict_lower = {string.ascii_lowercase[i]: range(1, 27)[i] for i in range(len(string.ascii_lowercase))}
priority_dict_upper = {string.ascii_uppercase[i]: range(27, 53)[i] for i in range(len(string.ascii_uppercase))}
priority_dict = {**priority_dict_lower, **priority_dict_upper}

# assign priority
data['priority'] = data['matching_element'].map(priority_dict)
# print(data.head())

print(data['priority'].sum())

### PART 2 ###

# load data as list
with open("inputs/input_ch3.txt") as f:
    data_list = list(f)

data_list = [s.strip('\n') for s in data_list]

# split list into sublists with three sequential elements
n = 3
sublists = [data_list[i:i + n] for i in range(0, len(data_list), n)]
print(sublists[:3])

# find a match in each sublist
all_matches = [set(sublist[0]).intersection(sublist[1], sublist[2]) for sublist in sublists]

# assign priorities
df_matches = pd.DataFrame(all_matches)
df_matches['priority'] = df_matches[0].map(priority_dict)

# sum priorities
print(df_matches['priority'].sum())