import json
import bisect
import time
import random
import string

LENGTH = 3
TIMES = 1000

# open files
f = open("random_str_list_1000000.json", 'r')
str_list = json.load(f)
f.close()

f = open("random_search_list_1000000.json", "r")
search_list = json.load(f)
f.close()

# start to measure time
all_start_time = time.time()

all_search_time = 0

for i in range(TIMES):
    # each linear-search
    start_time = time.time()
    search_str = search_list[i]
    ans_list = [x for x in str_list if x.startswith(search_str)]
    elapsed_time = time.time() - start_time
    print("elapsed time:", elapsed_time, "[sec]")
    print(len(ans_list))
    all_search_time += elapsed_time

all_elapsed_time = time.time() - all_start_time

print("all search time:", all_search_time, "[sec]")
print("all elapsed time:", all_elapsed_time, "[sec]")



