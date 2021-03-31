from shortest_paths import *
from lab9 import *
import timeit
import math
import random

def timetest_size(runs, size, graph, algo, parameters_num):
    total = 0
    for _ in range(runs):
        G = graph(size, 1000)
        start = timeit.default_timer()
        if(parameters_num == 2):
            algo(G, random.randint(0,size))
        else:
            algo(G, random.randint(0,size), 5)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def timetest_k(runs, k, graph, algo, parameters_num):
    total = 0
    size = 20
    for _ in range(runs):
        G = graph(size, 1000)
        start = timeit.default_timer()
        if(parameters_num == 2):
            algo(G, random.randint(0,size))
        else:
            algo(G, random.randint(0,size), k)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def timing_output_size(algo_1, algo_2, lower, upper, increment):
    algo_1_runtime_size = 0
    algo_2_runtime_size = 0
    for _ in range(lower, upper, increment):
        algo_1_runtime_size = timetest_size(5, _, create_random_complete_graph, algo_1, 2)
        algo_2_runtime_size = timetest_size(5, _, create_random_complete_graph, algo_2, 3)

        print(str(_) + "\t" + str(algo_1_runtime_size) + "\t" + str(algo_2_runtime_size))

def timing_output_k(algo_1, algo_2, lower, upper, increment):
    algo_1_runtime_size = 0
    algo_2_runtime_size = 0
    for _ in range(lower, upper, increment):
        algo_1_runtime_size = timetest_k(5, _, create_random_complete_graph, algo_1, 2)
        algo_2_runtime_size = timetest_k(5, _, create_random_complete_graph, algo_2, 3)

        print(str(_) + "\t" + str(algo_1_runtime_size) + "\t" + str(algo_2_runtime_size))


timing_output_size(bellman_ford_approx, bellman_ford, 5, 101, 1)


