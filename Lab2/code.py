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


d = {"name":"Ammar", "age":"20", "marks":"L"}

