# load the file as pandas dataframe

import pandas as pd
data = pd.read_csv("inputs/input_ch2.txt", sep = ' ', names = ['Player 1', 'Player 2'])

### PART 1

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

# identify the winner & assign score per round
data['p2 score per round'] = data['p2 score'] - data['p1 score']

# assign the score per round
winner_dict = {0: 3, -1: 0, 1: 6, -2: 6, 2: 0}
data['score translation'] = data['p2 score per round'].map(winner_dict)

# calculate Player 2 sum per round
data['p2 final score'] = data['p2 score'] + data['score translation']

# calculate the final score
print(data['p2 final score'].sum())

### PART 2
### NEW DECISION RULE FOR THE WINNING PARTY ###
new_rule_dict = {'X': 0, 'Y': 3, 'Z': 6}
# X -> loss -> the response should be A-3 B-1 C-2
# Y -> draw -> the response should be A-1 B-2 C-3
# Z -> win -> the response should be A-2 B-3 C-1

# based on p1 scores...
# X -> loss -> the response should be 1-3 2-1 3-2
# Y -> draw -> the response should be 1-1 2-2 3-3
# Z -> win -> the response should be 1-2 2-3 3-1

# determine the new choice of response
# check p2 (z) -> check p2 (c) -> response
# new_dict = {'X': [3, 1, 2], 'Y': [1, 2, 3], 'Z': [2, 3, 1]}

def new_element_choice(p1, p2):
    if p2 == 'X':
        if p1 == 'A':
            return 3
        elif p1 == 'B':
            return 1
        else:
            return 2

    elif p2 == 'Y':
        if p1 == 'A':
            return 1
        elif p1 == 'B':
            return 2
        else:
            return 3

    else:
        if p1 == 'A':
            return 2
        elif p1 == 'B':
            return 3
        else:
            return 1

data['p2 new element choice'] = data.apply(lambda x: new_element_choice(x['Player 1'], x['Player 2']), axis=1)

print(data.head())

# map the new rule
data['p2 score new rule'] = data['Player 2'].map(new_rule_dict)

# calculate the new player 2 score
data['p2 new total score'] = data['p2 new element choice'] + data['p2 score new rule']

print(data.head())

# total score
print(data['p2 new total score'].sum())