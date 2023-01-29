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
print(data.head())

print(sum(data['overlap_final'] == 1))