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
print(data.head())

print(data['priority'].sum())