limit = int(input("how many numbers you want: "))
num1 = 0
num2 = 1
if limit == 0:
    print("fibonacci series")
    print('Invalid Input')
if limit == 1: 
    print("fibonacci series")
    print(num1)
if limit > 1:
    print("fibonacci series")
    print(num1)
    print(num2)
    for i in range(limit-2):
        num3 = num1 + num2
        print(num3)
        num1 = num2
        num2 = num3