from pull_line import *

def cleaner_print(output):
    result = ''
    try:
        for element in output:
            for key, value in element.items():
                result += str(key) + ' : ' + str(value) + ' | '
        print(result)
    except:
        print('Input wrong request')

