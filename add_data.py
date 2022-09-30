import os.path
from input import *

def add_data(data, path = 'data.csv'):
    if os.path.getsize(path) > 0:
        temp = ''
    elif os.path.getsize(path) == 0:
        temp = ''
    else:
        temp = '\n'
    f = open(path, 'a', encoding='UTF8')
    new_data = only_new(data)
    for line in new_data:
        for element in line:
            temp += str(line[element]) + ' '
        temp = temp[:-1] + '\n'
    f.write(temp[:-1])
    f.close()

def only_new(data, path='data.csv'):
    already_exests = input_read(path)
    return [element for element in data if element not in already_exests]