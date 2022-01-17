# program to print 2nd maximum number


list = []
for i in range(5):
    num = int(input('enter a num: '))
    list.append(num)
max1 = list[0]
max2 = list[0]
index = 0
for i in range(len(list)):
    if list[i] > max1:
        max1 = list[i]
        index = i
for i in range(len(list)):
    if index != i:
        if list[i] > max2:
            max2 = list[i]

print('second maximum = ', max2)




#program to find 2nd minimum


list = []
for i in range(5):
    num = int(input('enter a num: '))
    list.append(num)
max1 = list[0]
max2 = list[0]
index = 0
for i in range(len(list)):
    if list[i] > max1:
        max1 = list[i]
        index = i
    min1 = list[i]
    min2 = list[i]
    index = 0
    for i in range(len(list)):
        if list[i] < min1:
            min1 = list[i]
            index = i
    for i in range(len(list)):
        if index != i:
            if list[i] < min2:
                min2 = list[i]

print('second manimum = ', min2)