import time
import numpy

NUM = 10000000

list_ = [str(x) for x in range(NUM)]

start_time = time.time()
numpy.savetxt("text_numpy_savetext.txt", list_, fmt='%s', delimiter=',')

elapsed_time = time.time() - start_time
print("elapsed time:", elapsed_time, "[sec]")
