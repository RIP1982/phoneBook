from keys import *

def input_read(path):
    try:
        with open(path, 'r', encoding='UTF8') as f:
            temp = f.read().split('\n')
            f.close()
            lines = []
            for elem in temp:
                temp_dict = {}
                person = elem.split(' ')
                for i in range(len(person)):
                    temp_dict[keys[i]] = person[i]
                lines.append(temp_dict)
    except:
        print('Input does not exist')
        exit()

    return lines