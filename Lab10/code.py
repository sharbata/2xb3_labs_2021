from vertex_cover import *
from lab10 import *
import timeit
import math
import random

def size_test(runs, size, graph, algo):
    total = 0
    for _ in range(runs):
        G = graph(size)
        start = timeit.default_timer()
        algo(G)
        total += end - start
    return total/runs

def size_output(algo_1, algo_2, lower, upper, increment):
    algo_1_runtime_size = 0
    algo_2_runtime_size = 0
    for _ in range(lower, upper, increment):
        algo_1_runtime_size = timetest_size(20, _, create_random_graph, algo_1, 2)

        print(str(_) + "\t" + str(algo_1_runtime_size) + "\t" + str(algo_2_runtime_size))

timing_output_size(vc_approx1, vc_approx2, 5, 101, 1)