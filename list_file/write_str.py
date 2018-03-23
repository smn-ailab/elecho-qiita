import time

NUM = 10000000

list_ = [str(x) for x in range(NUM)]

start_time = time.time()

str_ = '\n'.join(list_)
with open("text_write_str.txt", 'wt') as f:
    f.write(str_)

elapsed_time = time.time() - start_time
print("elapsed time:", elapsed_time, "[sec]")
