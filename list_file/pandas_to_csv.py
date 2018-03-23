import time
from pandas import Series

NUM = 10000000

list_ = [str(x) for x in range(NUM)]

start_time = time.time()

_series = Series(list_)
_series.to_csv("text_pandas_to_csv.txt", index=False)

elapsed_time = time.time() - start_time
print("elapsed time:", elapsed_time, "[sec]")
