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
        try:
            store[digit].add(str)
        except KeyError:
            store[digit] = {str}
    return store

def find_digits(digits, store,reference_len):
    segments = {}
    store = find_three(store,digits,reference_len)
    store = find_six(store,digits,reference_len)
    store = find_two(store,digits,reference_len)
    store = find_five(store,digits,reference_len)
    store = find_zero(store,digits,reference_len)
    store = find_nine(store,digits,reference_len)
    return store

def find_two(store, digits,ref):
    for item in digits:
        if len(item) == 5:
            a = store[8] - store[6]
            for segments_a in a:
                if not all(elem in item for elem in store[3]):
                    if segments_a in item:
                        store_segments(2,item)
    return store

def find_five(store, digits,ref):
    for item in digits:
        if len(item) == 5:
            a = store[8] - store[6]
            for segments in a:
                if segments not in item:
                    if not all(elem in item for elem in store[3]):
                        store_segments(5,item)
    return store

def find_zero(store, digits,ref):
    for item in digits:
        if len(item) == 6:
            ef = store[4] - store[1]
            e = ef - store[3]
            f = ef - e
            for segments in f:
                if segments not in item:
                    store_segments(0,item)
    return store

def find_nine(store, digits,ref):
    for item in digits:
        if len(item) == 6:
            g = store[8] - store[4] - store[3]
            for segments in g:
                if segments not in item:
                    store_segments(9,item)
    return store


def find_six(store, digits,ref):
    for item in digits:
        if len(item) == 6:
            if not all(elem in item for elem in store[1]):
                store_segments(6,item)
    return store
    

def find_three(store, digits,ref):
    for item in digits:
        if len(item) == 5:
            if all(elem in item for elem in store[1]):
                store_segments(3,item)
    return store
                    

        


def starter_pack(digits, store):
    for item in digits:
        if len(item) == 2:
            store = store_segments(1,item) 
        if len(item) == 4:
            store = store_segments(4,item)       
        if len(item) == 7:
            store = store_segments(8,item)
        if len(item) == 3:
            store = store_segments(7,item)      
    return store

def calcul_output(store, case):
    big_digits = ""
    buffer = case.split()
    for word in buffer:
        set_digits = set({})
        for segments in word:
            set_digits.add(segments)
        for i in range(len(store)):
            if set_digits == store[i]:
                print(set_digits,store[i])
                big_digits = big_digits + str(i)
    return big_digits
            

content = get_input("")
#For Test : Uncomment
#content  = get_input("test")

not_digits_list = parse_content(content)


reference_len = {'0':6 ,'1' : 2, '2' : 5, '3' : 5,'4' : 4,'5': 5,'6': 6,'7' : 3, '8': 7,'9': '6'}
total = 0
for case , value in not_digits_list.items():
    store = {}
    digits_len , digits= setup_digits_len(case)
    store.update(starter_pack(digits, store))
    store.update(find_digits(digits, store,reference_len))
    somme = calcul_output(store,value)
    print(value ,somme)
    total = total + int(somme)

print(total)


