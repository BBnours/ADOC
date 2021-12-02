with open("day_2/aoc_2_input.txt", 'r') as f:
    lines = [line.rstrip() for line in f]

horizontal = 0
depth = 0

for item in lines:
    line = item.split(" ")
    if "forward" in line[0]:
        horizontal = horizontal+ int(line[1])
    if "up" in line[0]:
        depth = depth- int(line[1])
    if "down" in line[0]:
        depth = depth + int(line[1])


print(depth*horizontal)



