from mst import *
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

def mst_timing_output(prim_1, prim_2, lower, upper, increment):
    prim_1_runtime = 0
    prim_2_runtime = 0
    for _ in range(lower, upper, increment):
        prim_1_runtime = timetest(10, _, create_random_graph, prim_1)
        prim_2_runtime = timetest(10, _, create_random_graph, prim_2)

        print(str(_) + "\t" + str(prim_1_runtime) + "\t" + str(prim_2_runtime))


def create_random_graph(n):
    G = WeightedGraph(n)
    for _ in range(round(n * math.sqrt(n))):
        G.add_edge(random.randint(0,n), random.randint(0,n), n)
    return G

#mst_timing_output(prim1, prim2, 50, 10000, 50)