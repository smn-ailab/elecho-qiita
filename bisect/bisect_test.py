import json
import bisect
import time
import random
import string
import bisect

LENGTH = 3
TIMES = 1000

# open files
f = open("random_str_list_1000000.json", 'r')
sorted_str_list = json.load(f)
f.close()

f = open("random_search_list_1000000.json", "r")
search_list = json.load(f)
f.close()

# start to measure time
all_start_time = time.time()

sorted_str_list.sort()
list_length = len(sorted_str_list)

sort_time = time.time() - all_start_time

all_search_time = 0

for i in range(TIMES):
    # each bisect-search
    start_time = time.time()
    search_str = search_list[i]
    top_point = bisect.bisect_left(sorted_str_list, search_str)
    end_point = bisect.bisect_left(sorted_str_list, search_str[:-1]+chr(ord(search_str[-1])+1))

    ans_list = sorted_str_list[top_point:end_point]

    elapsed_time = time.time() - start_time
    print("elapsed time:", elapsed_time, "[sec]")
    print(len(ans_list))
    all_search_time += elapsed_time

all_elapsed_time = time.time() - all_start_time

print("sorting time:", sort_time, "[sec]")
print("all search time:", all_search_time, "[sec]")
print("all elapsed time:", all_elapsed_time, "[sec]")



