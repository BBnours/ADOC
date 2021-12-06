from collections import Counter

def parseContent(content):
    ## Parsing the file to get usables inputs
    startLine = []
    finishLine = []
    start = []
    finish= []
    for item in content:
        buffer = item.split('->')
        startLine.append(buffer[0].strip())
        finishLine.append(buffer[1].strip())
    for i in range(len(startLine)):
        start.append(startLine[i].split(','))
        finish.append(finishLine[i].split(','))
    start = [tuple(x) for x in start]
    start = [tuple(map(int, x)) for x in start]
    finish = [tuple(x) for x in finish]
    finish = [tuple(map(int, x)) for x in finish]
    return start, finish

def make_line_vertical(debut, end):
    ## Find range of vertical lines
    line = []
    if debut[0] == end[0]:
        if debut[1] < end[1]:
            for itt in range(int(debut[1]), int(end[1])+1):
                line.append((int(debut[0]), itt))
        if debut[1] > end[1]:
            for itt in range (int(end[1]),int(debut[1])+1):
                line.append((int(end[0]), itt))
        if debut[1] == end[1]:
                line.append(int(debut[0]), int(debut[1])+1)
        return line

def make_line_horizontal(debut, end):
    ## Find range of horizontal lines
    line = []
    if debut[1] == end[1]:
        if debut[0] < end[0]:
            for itt in range(int(debut[0]), int(end[0])+1):
                line.append((itt,int(debut[1])))
        if debut[0] > end[0]:
            for itt in range( int(end[0]),int(debut[0])+1):
                line.append((itt, int(end[1])))
        if debut[0] == end[0]:
            line.append(int(debut[0]), int(debut[1]))
        return line

def count_tuples(line):
    ## determine the number of points where at least two lines overlap
    nb = 0
    val = Counter(line)
    uniqueList = list(set(line))
    for i in uniqueList:
        if val[i]>= 2:
            nb =nb + 1
            #print(i, "-", val[i])
    return nb

with open("day_5/aoc_5_input.txt", 'r') as f:
    content = f.readlines()
start, finish = parseContent(content)

lines = []

# parcours all the inputs to make the lines
for i in range(len(start)):
    buffer_hori = make_line_horizontal(start[i], finish[i])
    if buffer_hori:
        lines.append(buffer_hori)
    buffer_verti = make_line_vertical(start[i], finish[i])
    if buffer_verti:
        lines.append(buffer_verti)

#Flattened the list of list
list_of_lines = [val for sublist in lines for val in sublist]

#Count the number of reccurence in the list
print( count_tuples(list_of_lines))


'''
## Test : An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3
assert make_line_vertical((1,1),(1,3)) == [(1,1),(1,2),(1,3)]
## Test : An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
assert make_line_horizontal((9,7),(7,7)) == [(7,7),(8,7),(9,7)]
#Test : this is anywhere in the diagram with a 2 or larger - a total of 5 points.
assert count_tuples(list_of_lines) == 5
'''
