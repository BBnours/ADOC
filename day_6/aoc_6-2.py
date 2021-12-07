import collections

def parse_content(content):
    listOfInt = list(map(int, content[0].split(',')))
    return listOfInt

def make_dic(fish_dict,liste):
    for fish in liste :
        if fish in fish_dict:
            fish_dict[fish] = fish_dict[fish]+1
    return fish_dict

def reproduce_fish(fish_dict):
    for el in fish_dict:
        if el > -1:
            buffer = fish_dict[el] 
            fish_dict[el] = 0
            fish_dict[el-1] = fish_dict[el-1] + buffer
        if el == -1:
            fish_dict[6] = fish_dict[6] + fish_dict[-1]
            fish_dict[8] = fish_dict[-1]
            fish_dict[-1] = 0
    return fish_dict
    
with open("day_6/aoc_6_input.txt", 'r') as f:
    content = f.readlines()

fish_list = parse_content(content)

#For Test uncoment
#fish_list = [3,4,3,1,2]

fish_dict = {-1: 0,0: 0,1:0,2: 0,3: 0,4: 0,5: 0,6: 0,7: 0,8: 0}

fish_dict = make_dic(fish_dict,fish_list)

#fish_dict = dict(reversed(sorted(fish_dict.items())))

for i in range(256):
    fish_dict = reproduce_fish(fish_dict)
print(fish_dict)

print(sum(fish_dict.values())+fish_dict[-1])
#352195 low



##Test for 356 dayes
assert len(fish_list) == 26984457539
