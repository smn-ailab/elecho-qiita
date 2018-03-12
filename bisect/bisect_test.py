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
str_list = json.load(f)
f.close()

f = open("random_search_list_1000000.json", "r")
search_list = json.load(f)
f.close()

# start to measure time
all_start_time = time.time()

str_list.sort()
list_length = len(str_list)

sort_time = time.time() - all_start_time

all_search_time = 0

for i in range(TIMES):
    # each bisect-search
    start_time = time.time()
    search_str = search_list[i]
    insert_point = bisect.bisect_left(str_list, search_str)
    end_point = insert_point
    while str_list[end_point].startswith(search_str):
        end_point += 1
        if end_point > list_length:
            break
    ans_list = str_list[insert_point:end_point]

    elapsed_time = time.time() - start_time
    print("elapsed time:", elapsed_time, "[sec]")
    print(len(ans_list))
    all_search_time += elapsed_time

all_elapsed_time = time.time() - all_start_time

print("sorting time:", sort_time, "[sec]")
print("all search time:", all_search_time, "[sec]")
print("all elapsed time:", all_elapsed_time, "[sec]")



