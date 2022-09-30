from cleaner_print import *
from add_data import *

add_data(input_read('source.txt'), 'data.csv')
cleaner_print(pull_line(input('Input key: LastName or Name or Number: '), input('Enter a request: ')))