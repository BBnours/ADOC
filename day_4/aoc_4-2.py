with open("day_4/aoc_4_input.txt", 'r') as f:
    content = f.readlines()

def get_drawn(content):
    numbers_to_drawn = []
    for idx, item in enumerate(content):
        if item == "\n":       
            buffer = content[:idx]
            content = content[idx:]
            numbers_to_drawn = buffer[0].split(',')
            return numbers_to_drawn,content

def split_grids(content):
    buffer = []
    content.remove("\n")
    for item in content:
        buffer.append(item.split())
        buffer = list(filter(None, buffer))
    #flattened = [val for sublist in buffer for val in sublist]
    composite_list = [buffer[x:x+5] for x in range(0, len(buffer),5)]
    return composite_list

def bingo(grids, drawn,list_winner):
    for grid_number, grid in enumerate(grids):
        if grid_number not in list_winner:
            for i in range(5):
                column = [item[i] for item in grid]
                if (all(x in drawn for x in column)):
                    list_winner.append(grid_number)
                    if len(list_winner)== len(grids):
                        return drawn[-1], grid
        if grid_number not in list_winner:
            for row in grid:
                if (all(x in drawn for x in row)):
                    list_winner.append(grid_number)
                    if len(list_winner) == len(grids):
                        return drawn[-1], grid


            
def calculate(last, unmarked):
    somme = 0
    last_number = int(last) 
    print('last_number',last_number) 
    for number in unmarked:
        somme = int(number) + somme
    res = somme * last_number
    return res

def extract(bundle, drawn):
    flattened = [val for sublist in bundle[1] for val in sublist]
    unmark = list(set(flattened) - set(drawn))
    return unmark

drawn, content = get_drawn(content)
grids = split_grids(content)

list_winner = []
for idx, item in enumerate(drawn):
    winner = bingo(grids,drawn[:idx],list_winner)
    if winner:  
        unmarked = extract(winner,drawn[:idx])
        print(calculate(winner[0], unmarked))


