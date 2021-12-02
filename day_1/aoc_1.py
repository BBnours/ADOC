with open("aoc_1_input.txt", 'r') as f:
    lines = [line.rstrip() for line in f]

increase = 1

for item in lines:
    if before:
        if before < item:
            increase = increase + 1
        before = item

print(increase)       

