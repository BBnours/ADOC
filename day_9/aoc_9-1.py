import numpy as np

def get_input(val):
    if val =='test'  : 
        with open("day_9/aoc_9_input-test.txt", 'r') as f:
            content = f.readlines()
    else :
        with open("day_9/aoc_9_input.txt", 'r') as f:
            content = f.readlines()
    return content

def parse_content(content):
    #Output
    output = []
    for item in content:
        buffer= []
        for number in item :
            if '\n' not in number:
                buffer.append(int(number))
        output.append(buffer)
    return output


##content  = get_input("")
#For Test : Uncomment
content  = get_input("test")

map_parsed = parse_content(content)

heigh = np.matrix(map_parsed)
print(heigh)
map_down = heigh[1:,:]
print('down\n',map_down)
map_up = heigh[:-1,:]
print('up\n',map_up)
map_right = heigh[:,1:]
print('right\n',map_right)
map_left = heigh[:,:-1]
print('left\n',map_left)
for i in range(0,heigh.shape[0]):
    for j in range(0,heigh.shape[1]):
        q = 1
                    

             



