from collections import Counter
import numpy as np



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
            for itt in range (int(debut[1]),int(end[1])-1,-1):
                line.append((int(end[0]), itt))
        if debut[1] == end[1]:
                line.append(int(debut[0]), int(debut[1])+1)
        print('verti',line) 
        return line

def make_line_horizontal(debut, end):
    ## Find range of horizontal lines
    line = []
    if debut[1] == end[1]:
        if debut[0] < end[0]:
            for itt in range(int(debut[0]), int(end[0])+1):
                line.append((itt,int(debut[1])))
        if debut[0] > end[0]:
            for itt in range(int(debut[0]), int(end[0])-1,-1):
                line.append((itt, int(end[1])))
        if debut[0] == end[0]:
            line.append(int(debut[0]), int(debut[1]))
        print('hori',line) 
        return line

def make_line_diago(debut,end):
    #Find range of diagonal lines
    line = []
    if debut[1] != end[1]:
        if debut[0] != end[0]:
            if debut[1] < end[1]:
                rangeY = range(int(debut[1]), int(end[1])+1)
            if debut[1] > end[1] :
                rangeY = range(int(debut[1]),int(end[1])-1,-1)
            if debut[0] < end[0]:
                rangeX = range(int(debut[0]), int(end[0])+1)
            if debut[0] > end[0]:
                rangeX = range(int(debut[0]),int(end[0])-1,-1)
            for i in range(len(rangeY)):
                line.append((rangeX[i],rangeY[i]))  
            print('diago',line) 
            return line


def count_tuples(line):
    ## determine the number of points where at least two lines overlap
    nb = 0
    val = Counter(line)
    uniqueList = list(set(line))
    for i in uniqueList:
        if val[i]>= 2:
            nb =nb + 1
            print(i, "-", val[i])
    return nb

"""
def display(lines):
    res1 = min(lines)[0], max(lines)[0]
    res2 = min(lines)[1], max(lines)[1]

    x = np.arange(res1[0], res1[1], 1)
    y = np.arange(res2[0], res2[1], 1)
    xx, yy = np.meshgrid(x, y, sparse=True)

    for coords in lines :
        xx[coords] = coords[0]
        yy[i,j]

    print( np.meshgrid(x, y, sparse=True))

"""

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
    buffer_diagonal = make_line_diago(start[i], finish[i])
    if buffer_diagonal:
        lines.append(buffer_diagonal)

#Flattened the list of list
list_of_lines = [val for sublist in lines for val in sublist]

#Count the number of reccurence in the list
print( count_tuples(list_of_lines))

#display matrix
#display(list_of_lines)


'''
#21381 high
20889 low
## Test : An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3
assert make_line_vertical((1,1),(1,3)) == [(1,1),(1,2),(1,3)]
## Test : An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
assert make_line_horizontal((9,7),(7,7)) == [(7,7),(8,7),(9,7)]
#Test : this is anywhere in the diagram with a 2 or larger - a total of 5 points.
assert count_tuples(list_of_lines) == 12
'''
