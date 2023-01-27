# load the file as pandas dataframe

import pandas as pd
data = pd.read_csv("inputs/input_ch2.txt", sep = ' ', names = ['Player 1', 'Player 2'])

print(data.head())

# data['Player 2'] = data['Player 1'].apply(lambda x: x[1:]).astype('str')
# data['Player 1'] = data['Player 1'].apply(lambda x: x[:1])

### DECISION RULE FOR THE WINNING PARTY ###

# A OR X == Rock 1-1 = 0 draw 1-2 = -1 loss 1-3 = -2 win 
# B OR Y == Paper 2-2 = 0 draw 2-3 = -1 loss 2-1 = 1 win 
# C OR Z == Scissors 3-3 = 0 draw 3-1 = 2 loss 3-2 = 1 win 

# decision rule:
# 0 always draw
# -1 always loss
# 1 always win
# -2 win
# 2 loss

# score allocation: 0 (loss), 3 (draw), 6 (win)

# replace letters with digits
a_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

data['p1 score'] = data['Player 1'].map(a_dict)
data['p2 score'] = data['Player 2'].map(a_dict)

print(data.head())

# identify the winner & assign score per round
winner_dict = {0: 3, -1: 0, 1: 6, -2: 6, 2: 0}

data['p2 score per round'] = data['p2 score'] - data['p1 score']

print(data.head())

# assign the score per round
data['score translation'] = data['p2 score per round'].map(winner_dict)
# calculate Player 2 sum per round
data['p2 final score'] = data['p2 score'] + data['score translation']
# calculate the final score
print(data['p2 final score'].sum())