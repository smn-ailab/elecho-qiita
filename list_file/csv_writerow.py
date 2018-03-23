import time
import csv

NUM = 10000000

list_ = [str(x) for x in range(NUM)]

start_time = time.time()
with open("text_csv_writerow.txt", 'wt') as f:
    writer = csv.writer(f)
    for ele in list_:
        writer.writerow([ele])

elapsed_time = time.time() - start_time
print("elapsed time:", elapsed_time, "[sec]")
