import timeit
import csv
import random

#Test used for list copy()
def randList(size, maxValue):#list of length size containing arbitrary values
    l1 = []
    for i in range(size):
        l1.append(random.randint(0, maxValue))
    return l1

def timeTest(runs, size, maxValue):#timing function similar to one written in lecture
    total = 0 
    randomList = randList(size, maxValue)
    for i in range(runs):
        start = timeit.default_timer()
        l2 = randomList.copy()
        end = timeit.default_timer()
        total += end - start 
    avg = total/runs
    return avg 



#code to test list lookups() operation

list1 = []
for i in range(1000000):
    list1.append(0)

def lookups(n):#performs lookups operation, called in the next method
    return list1[n]

def lookups_test():#tests lookups 1 mil times, and documents time of every 500th call in timestamp
    csvfile=open('lookups.csv','w', newline='')#then it saves this info in a csv file, which can be opened in excel
    obj=csv.writer(csvfile)
    timestamp = 0

    start = timeit.default_timer()
    for i in range(1000000):
            
        lookups(i)
            
        if(i / 500 > 0 and i % 500 == 0):
            end = timeit.default_timer()
            timestamp = end - start
            obj.writerow((i, timestamp))

    csvfile.close()




#code to test list append(n) operation

list2 = []

def append(n):#performs append operation, called in the next method
    list2.append(n)

def append_test():#works same way as lookups_test
    csvfile=open('append.csv','w', newline='')
    obj=csv.writer(csvfile)
    timestamp = 0

    start = timeit.default_timer()
    for i in range(1000000):
            
        append(i)

        if(i / 500 > 0 and i % 500 == 0):
            end = timeit.default_timer()
            timestamp = end - start
            obj.writerow((i, timestamp))

    csvfile.close()
