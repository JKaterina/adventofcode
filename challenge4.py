### PART 1 ###

# load the file as dataframe
import pandas as pd
data = pd.read_csv('inputs/input_ch4.txt', sep = ',', names = ['range_1', 'range_2'])
data[['start_1', 'end_1']] = data['range_1'].str.split('-', expand = True).astype('int')
data[['start_2', 'end_2']] = data['range_2'].str.split('-', expand = True).astype('int')

# check if ranges overlap
data['overlap_1'] = data.apply(lambda x: set((range(x.start_1, x.end_1))).issubset(range(x.start_2, x.end_2)), axis = 1)
data['overlap_2'] = data.apply(lambda x: set((range(x.start_2, x.end_2))).issubset(range(x.start_1, x.end_1)), axis = 1)
data['overlap_final'] = (data['overlap_1'] + data['overlap_2']).astype('int')

print(data['overlap_1'].sum() + data['overlap_2'].sum())

### PART 2: Find all overlaps ###
data['intersection_1'] = data.apply(lambda x: len(set((range(x.start_1, x.end_1))).intersection(range(x.start_2, x.end_2))), axis = 1)
data['intersection_2'] = data.apply(lambda x: len(set((range(x.start_2, x.end_2))).intersection(range(x.start_1, x.end_1))), axis = 1)
data['intersection'] = data['intersection_1'] + data['intersection_2']
print(data.head())

print(sum(data['intersection'] > 0))

### other solution

with open("inputs/input_ch4.txt") as f:
    data_list = list(f)
r = 0
for line in data_list:
    s1, s2 = map(lambda section: tuple(map(int, section.split("-"))), line.split(","))
    if (s1[0] - s2[0]) * (s1[1] - s2[1]) <= 0:
        r += 1

print(r)

r2 = 0
for line in data_list:
    s1, s2 = map(lambda section: tuple(map(int, section.split("-"))), line.split(","))
    if s2[0] <= s1[0] <= s2[1] or s1[0] <= s2[0] <= s1[1]:
        r2 += 1
print(r2)