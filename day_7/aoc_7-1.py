def parse_content(content):
    listOfInt = list(map(int, content[0].split(',')))
    return listOfInt
    
    
with open("day_7/aoc_7_input.txt", 'r') as f:
    content = f.readlines()

crabs_list  =parse_content(content)
#For Test uncoment
#crabs_list = [16,1,2,0,4,2,7,1,2,14]

print('list of crabs', crabs_list)
max_dist = max(crabs_list)
fuel = 0
fuel_list =[]
position = []
crabs_number = 0
gap = 0
for i in range(max_dist):
    for crabs in crabs_list:
        gap=0
        for itt in range(abs(crabs - i)+1):
            gap = gap + itt
        fuel = fuel + gap
    fuel_list.append(fuel)
    position.append(i)
    fuel = 0

print(fuel_list)

for i in range(len(fuel_list)):
    if fuel_list[i] == min(fuel_list):
        print('total fuel',fuel_list[i])
        print('position',position[i])

