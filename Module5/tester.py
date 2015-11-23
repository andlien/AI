__author__ = 'Anders'

numberOfRuns = 5

lists = []
import Module5.design1

for i in range(numberOfRuns):
    lists.append(Module5.design1.main())

for i in range(len(lists)):
    print("####### DESIGN 1[" + str(i) + "] ########")
    for num in lists[i]:
        print(num)
    print("############################")

lists = []
import Module5.design2

for i in range(numberOfRuns):
    lists.append(Module5.design2.main())

for i in range(len(lists)):
    print("####### DESIGN 2[" + str(i) + "] ########")
    for num in lists[i]:
        print(num)
    print("############################")

lists = []
import Module5.design3

for i in range(numberOfRuns):
    lists.append(Module5.design3.main())

for i in range(len(lists)):
    print("####### DESIGN 3[" + str(i) + "] ########")
    for num in lists[i]:
        print(num)
    print("############################")

lists = []
import Module5.design4

for i in range(numberOfRuns):
    lists.append(Module5.design4.main())

for i in range(len(lists)):
    print("####### DESIGN 4[" + str(i) + "] ########")
    for num in lists[i]:
        print(num)
    print("############################")

lists = []
import Module5.design5

for i in range(numberOfRuns):
    lists.append(Module5.design5.main())

for i in range(len(lists)):
    print("####### DESIGN 5[" + str(i) + "] ########")
    for num in lists[i]:
        print(num)
    print("############################")