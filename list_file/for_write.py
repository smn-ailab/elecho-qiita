import time

NUM = 10000000

list_ = [str(x) for x in range(NUM)]

start_time = time.time()
with open("text_for_write.txt", 'wt') as f:
    for ele in list_:
        f.write(ele+'\n')

elapsed_time = time.time() - start_time
print("elapsed time:", elapsed_time, "[sec]")
