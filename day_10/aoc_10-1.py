import numpy as np

def get_input(val):
    if val =='test'  : 
        with open("day_10/aoc_10_input-test.txt", 'r') as f:
            content = f.readlines()
    else :
        with open("day_10/aoc_10_input.txt", 'r') as f:
            content = f.readlines()
    return content

def parse_content(content):
    #Output
    output = []
    for item in content:
        buffer= []
        for element in item :
            if '\n' not in element:
                buffer.append(element)
        output.append(buffer)
    return output



content  = get_input("")
#For Test : Uncomment
#content  = get_input("test")

routes = parse_content(content)

reference = {'[' : ']', '(' : ')', '<' : '>', '{' : '}'}

parcours = []
error = []
close_liste = []
for line in routes :
    close = []
    continuer = True 
    for i in range(len(line)) :
        if continuer:
            if line[i] in reference.keys():
                parcours.append(line[i])
                close.append(reference[line[i]])
            if line[i] in reference.values():
                    for item in reference.items():
                        if item[1] == line[i]:
                            if item[0] == parcours[-1]:
                                parcours.pop()
                                close.pop()
                            else:
                                error.append(line[i])
                                continuer = False
    if continuer:
        close_liste.append(close)

final_close = []
for item in close_liste:
    final_close.append(item[::-1])

scores = []
for liste in final_close:
    res = 0
    for item in liste :
        if item == ')':
            res = res * 5
            res = res+1
        if item == ']':
            res = res * 5
            res = res+2
        if item == '}':
            res = res * 5
            res = res+3
        if item == '>':
            res = res * 5
            res = res+4
    scores.append(res)

scores.sort()
length = len(scores)
middle_index = length//2
middle_score = scores[middle_index:middle_index+1]
    
print(middle_score)


                            
