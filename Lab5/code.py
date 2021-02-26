from heap import *
import math
import random
import timeit
import csv

def timetest(runs, length, list, heap, build_heap):
    total = 0
    for _ in range(runs):
        heap.data = list(length)
        heap.length = len(heap.data)
        start = timeit.default_timer()
        build_heap()
        end = timeit.default_timer()
        total += end - start
    return total/runs

def heap_timing_output(heap, build_1, build_2, build_3, lower, upper, increment):
    build_1_runtime = 0
    build_2_runtime = 0
    build_3_runtime = 0
    for _ in range(lower, upper, increment):
        build_1_runtime = timetest(10, _, create_random_list, heap, build_1)
        build_2_runtime = timetest(10, _, create_random_list, heap, build_2)
        build_3_runtime = timetest(10, _, create_random_list, heap, build_3)

        print(str(_) + "\t" + str(build_1_runtime) + "\t" + str(build_2_runtime) + "\t" + str(build_3_runtime))


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

h1 = Heap([])
#heap_timing_output(h1, h1.build_heap1, h1.build_heap2, h1.build_heap2, 500, 100001, 500)
heap_timing_output(h1, h1.build_heap1, h1.build_heap2, h1.build_heap3, 500, 100001, 500)