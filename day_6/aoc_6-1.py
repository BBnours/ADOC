with open("day_6/aoc_6_input.txt", 'r') as f:
    content = f.readlines()

def parse_content(content):
    listOfInt = list(map(int, content[0].split(',')))
    return listOfInt

fish_list = parse_content(content)

#For Test uncoment
fish_list = [3,4,3,1,2]

for i in range(256):
    print(i)
    for idx, item in enumerate(fish_list) :
        fish_list[idx] = item -1
        if fish_list[idx] == -1:
            fish_list[idx] = 6
            fish_list.append(9)
print (len(fish_list))


'''
## Test for 18 dayes
assert content == [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]
assert len(content) == 26
'''
##Test for 80 dayes
#assert len(fish_list) == 26984457539
