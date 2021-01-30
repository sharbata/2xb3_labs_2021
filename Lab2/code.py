import timeit
import csv


list2 = []
for i in range(1000000):
    list2.append(0)


def lookups(n):
    return list2[n]

def lookups_test():
    csvfile=open('lookups.csv','w', newline='')
    obj=csv.writer(csvfile)
    temp = 0

    start = timeit.default_timer()
    for i in range(1000000):
            
        lookups(i)
            
        if(i / 500 > 0 and i % 500 == 0):
            end = timeit.default_timer()
            temp = end - start
            obj.writerow((i, temp))

    csvfile.close()


list3 = []


def append(n):
    list3.append(n)

def append_test():
    csvfile=open('append.csv','w', newline='')
    obj=csv.writer(csvfile)
    temp = 0

    start = timeit.default_timer()
    for i in range(1000000):
            
        append(i)

        if(i / 500 > 0 and i % 500 == 0):
            end = timeit.default_timer()
            temp = end - start
            obj.writerow((i, temp))

    csvfile.close()



lookups_test()

append_test()

#Test used for list copy method
def randList(size, maxValue):
    l1 = []
    for i in range(size):
        l1.append(random.randint(0, maxValue))
    return l1

def timeTest(runs, size, maxValue):
    total = 0 
    randomList = randList(size, maxValue)
    for i in range(runs):
        start = timeit.default_timer()
        l2 = randomList.copy()
        end = timeit.default_timer()
        total += end - start 
    avg = total/runs
    return avg 
        




