with open("inputs/input_ch6.txt") as f:
    a = list(f)[0]

a_list = [*a]

# check every 4 characters set
# if set < 4 -> continue
# else: stop and print set start
set_start = 0
for subset in a_list:
    
    subset = set(a_list[set_start: set_start + 14])
    if len(subset) < 14:
        set_start += 1

    else:
        print(set_start+14)
        break

for i in range(14, len(a_list)):
    s = set(a_list[(i-14):i])
    if len(s) == 14:
        print(i)
        break


    