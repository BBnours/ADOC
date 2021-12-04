import pandas as pd


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

def determine_oxygen_and_co2(df):
    df_oxygen = df
    df_co2 = df
    

    for item in df:
        one_oxy = (df_oxygen[item].values == 1).sum()
        zero_oxy = (df_oxygen[item].values == 0).sum()
        one_co2 = (df_co2[item].values == 1).sum()
        zero_co2 = (df_co2[item].values == 0).sum()
        ## For Oxygen -> most common
        if len(df_oxygen.index) > 1:
            print(df_oxygen)
            print('----')
            if zero_oxy < one_oxy :
                df_oxygen = df_oxygen[df_oxygen[item].values == 1]
            if zero_oxy > one_oxy :
                df_oxygen = df_oxygen[df_oxygen[item].values == 0]
            if one_oxy == zero_oxy :
                df_oxygen = df_oxygen[df_oxygen[item].values == 1]
        if len(df_co2.index) > 1:
        ## For CO2 -> least common
            if zero_co2 < one_co2 :
                df_co2 = df_co2[df_co2[item].values == 0]
            if zero_co2 > one_co2 :
                df_co2 = df_co2[df_co2[item].values == 1]
            if one_co2 == zero_co2 :
                df_co2 = df_co2[df_co2[item].values == 0]
    return df_oxygen ,df_co2

def to_string(df):
    string = ""
    for item in df.iloc[0]:
        string = string + str(item)
    return string

with open("day_3/aoc_3_input.txt", 'r') as f:
    input_test = [line.rstrip() for line in f]

#input_test = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
df = pd.DataFrame()
tobe_df = trans_list(input_test)
df = pd.DataFrame(tobe_df)

oxygen, co2 = determine_oxygen_and_co2(df)
oxygen_decimal = to_string(oxygen)
co2_decimal = to_string(co2)
res = int(oxygen_decimal, 2) * int(co2_decimal, 2)

print(res)


