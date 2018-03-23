import time
import csv

NUM = 10000000

list_ = [str(x) for x in range(NUM)]

start_time = time.time()
list1 = [[x] for x in list_]
with open("text_csv_writerows.txt", 'wt') as f:
    writer = csv.writer(f)
    writer.writerows(list1)

elapsed_time = time.time() - start_time
print("elapsed time:", elapsed_time, "[sec]")
