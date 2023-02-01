# load the file as list
with open("inputs/input_ch5.txt") as f:
    # split at empty line
    stacks, commands = (i.splitlines() for i in f.read().strip('\n').split('\n\n'))

# transform stacks input to dict {column index: [crate label values]}
stacks_dict = {int(digit):[] for digit in stacks[-1].replace(" ", "")}
indexes = [index for index, char in enumerate(stacks[-1]) if char != " "]

# display stacks
def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks_dict:
        print(stack, stacks_dict[stack])
    print("\n")

# load stacks
def loadStacks():
    for s in stacks[:-1]:
        stack_num = 1
        for i in indexes:
            if s[i] != " ":
                stacks_dict[stack_num].insert(0, s[i])
            stack_num += 1

# display answer
def getStackEnds():
    answer = ""
    for stack in stacks_dict:
        answer += stacks_dict[stack]
    return answer

print(stacks_dict[4])

# clean commands
for command in commands:
    command = command.replace("move ", "").replace("from ", "").replace("to ", "").strip().split(" ")
    command = [int(e) for e in command]
    
    # commands structure: move {number_of_rows} from {old_index} to {new_index}
    crates_to_move = command[0]
    move_from = command[1]
    move_to = command[2]

    print(crates_to_move, move_from, move_to)

    for crate in range(crates_to_move):
        print(stacks_dict[move_from])
        # crate_removed = stacks_dict[move_from].pop()
        # stacks_dict[move_to].append(crate_removed)

loadStacks()
displayStacks()
getStackEnds()



