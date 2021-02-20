import math
import random
import timeit
import csv
from lab4 import *
from sorts import *

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
    csvfile=open('bottom_up_timing.csv','w')
    obj = csv.writer(csvfile)
    sorts_runtime = 0
    lab4py_runtime = 0
    for _ in range(lower, upper, increment):
        sorts_runtime = timetest(20, _, create_random_list, mergesort_bottom)
        lab4py_runtime = timetest(20, _, create_random_list, mergesort)

        print(str(_) + "\t" + str(sorts_runtime) + "\t" + str(lab4py_runtime))
        #obj.writerow((_,sorts_runtime,lab4py_runtime))
    csvfile.close()


def three_way_mergesort_timing_output(lower, upper, increment):
    sorts_runtime = 0
    lab4py_runtime = 0
    for _ in range(lower, upper, increment):
        sorts_runtime = timetest(20, _, create_random_list, mergesort_three)
        lab4py_runtime = timetest(20, _, create_random_list, mergesort)

        print(str(_) + "\t" + str(sorts_runtime) + "\t" + str(lab4py_runtime))

def timetest_worstcase(runs, factor, list, sort):
    total = 0
    for _ in range(runs):
        L = list(10000, factor)
        start = timeit.default_timer()
        sort(L)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def worst_case_mergesort_output(lower,upper,increment):
    for _ in range(lower, upper,increment):
        runtime = timetest_worstcase(20, _/1000, create_near_sorted_list, mergesort_bottom)

#bottom_up_timing_output(500, 100001, 500)
#three_way_mergesort_timing_output(500, 100001, 500)
#worst_case_mergesort_output(0,1000,50)

