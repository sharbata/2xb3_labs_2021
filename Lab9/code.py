from shortest_paths import *
from lab9 import *
import timeit
import math
import random

def timetest(runs, size, graph, prim):
    total = 0
    for _ in range(runs):
        G = graph(size)
        start = timeit.default_timer()
        prim(G)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def timing_output(algo_1, algo_2, lower, upper, increment):
    algo_1_runtime = 0
    algo_2_runtime = 0
    for _ in range(lower, upper, increment):
        algo_1_runtime = timetest(10, _, create_random_complete_graph, algo_1)
        algo_2_runtime = timetest(10, _, create_random_complete_graph, algo_2)

        print(str(_) + "\t" + str(algo_1_runtime) + "\t" + str(algo_2_runtime))

timing_output(bellman_ford_approx, bellman_ford, )

