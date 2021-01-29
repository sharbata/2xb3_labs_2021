import timeit
import csv

def copy_test():
    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = l1.copy()
    print("l1 copy: ", l2)


print("-".join(str(n) for n in range(201)))