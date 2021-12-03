import pandas as pd
import numpy as np

with open("day_3/aoc_3_input.txt", 'r') as f:
    input_test = [line.rstrip() for line in f]
df = pd.DataFrame()
tobe_df = []
gamma_rate = ""

def trans_list(input_test):
    liste = []
    for item in input_test:
        x = [int(a) for a in str(item)]
        liste.append(x)
    return liste

def count_occ(df):
    gamma = ""
    for item in df:
        a = (df[item].values == 1).sum()
        b = (df[item].values == 0).sum()
        if a < b :
            gamma = gamma + "0"
        else :
            gamma = gamma + "1"
    return gamma

def invert(gamma_rate):
    inverse_s = gamma_rate.replace('1', '2')
    inverse_s = inverse_s.replace('0', '1')
    inverse_s = inverse_s.replace('2', '0')
    return int(inverse_s, 2)

tobe_df = trans_list(input_test)
df = pd.DataFrame(tobe_df)
gamma_rate = count_occ(df)
epsilon_rate = invert(gamma_rate)
gamma_rate = int(gamma_rate, 2)

res = gamma_rate * epsilon_rate
print(res)
