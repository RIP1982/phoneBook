from input import *

def pull_line(key, value, path='data.csv'):
    data = input_read(path)
    for i in range(len(keys)):
        if key == keys[i]:
            return [line for line in data if line[key] == value]


    #









