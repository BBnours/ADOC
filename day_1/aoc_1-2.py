with open("day_1/aoc_1_input.txt", 'r') as f:
    lines = [line.rstrip() for line in f]

lines = list(map(int, lines))
increase = 1

for i in range(len(lines)-4):
    window_first = sum(lines[i:i+3])
    window_second = sum(lines[i+1:i+4])
    if window_second > window_first:
        increase = increase + 1

print(increase)

