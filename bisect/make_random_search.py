import random
import string
import copy
import json

NUM = 1000000
LENGTH = 3

str_list = list()

for i in range(NUM):
    temp_str = "".join([random.choice(string.ascii_lowercase) for x in range(LENGTH)])
    str_list.append(copy.deepcopy(temp_str))

f = open('random_search_list_1000000.json', 'w')
json.dump(str_list, f, indent=4)

