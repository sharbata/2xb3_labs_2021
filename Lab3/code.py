from lab4 import *
from sorts import *
import random
import timeit
import csv

def timetest(runs, length, list, sort):
    total = 0
    for _ in range(runs):
        L = list(length)
        start = timeit.default_timer()
        sort(L)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def bottom_up_timing_output(lower, upper, increment):
    csvfile=open('bottom_up_timing.csv','w', newline='')
    obj = csv.writer(csvfile)
    sorts_runtime = 0
    lab4py_runtime = 0
    for _ in range(lower, upper, increment):
        sorts_runtime = timetest(20, _, create_random_list, mergesort_bottom)
        lab4py_runtime = timetest(20, _, create_random_list, mergesort)

        obj.writerow(_,sorts_runtime,lab4py_runtime)
    csvfile.close()


bottom_up_timing_output(100, 10001, 100)

