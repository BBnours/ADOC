def parse_content(content):
    #Output
    buffer = []
    output = {}
    for item in content:
        sentence = item.split('|')
        output[sentence[0]] = sentence[1].rstrip('\n')
    return output
            
def count_digits(dic): 
    counter = 0
    for word in dic.values() :
        for item in word.split():
            buff = len(item)
            if buff == 3 or buff == 7 or buff == 2 or buff == 4:
                counter = counter + 1
    return counter

def get_input(val):
    if val =='test'  : 
        with open("day_8/aoc_8_input-test.txt", 'r') as f:
            content = f.readlines()
    else :
        with open("day_8/aoc_8_input.txt", 'r') as f:
            content = f.readlines()
    return content

def setup_digits_len(sentence):
    digits = []
    digits = sentence.split()
    digits_len = {}
    for item in digits :
        digits_len[item] = len(item)
    
    return digits_len,digits

def store_segments(digit,item):
    for str in item :
        print(str)
        try:
            store[digit].add(str)
        except KeyError:
            store[digit] = {str}
    return store

    

content  = get_input("")
#For Test : Uncomment
content  = get_input("test")

not_digits_list = parse_content(content)

print(count_digits(not_digits_list))


