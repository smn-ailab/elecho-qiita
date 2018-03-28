import time
from pandas import Series

import dask.dataframe as dd
import dask.multiprocessing

NUM = 10000000

list_ = [str(x) for x in range(NUM)]

start_time = time.time()

pds = dd.from_pandas(Series(list_), npartitions=1)
pds.to_csv(["dask_series_entire.txt"], index=False)

elapsed_time = time.time() - start_time
print("elapsed time:", elapsed_time, "[sec]")
