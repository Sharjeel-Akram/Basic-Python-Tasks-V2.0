#Write a program that takes inputs until user enter -1 and your program tells the maximum and 
#minimum no. [You can’t list or array for this question.]

number = int(input('enter your number please: '))
finish = 0
Maximum = 0
Minimum = number
while finish == 0:
    number = int(input('enter your number please: '))
    if number > Maximum:
        Maximum = number

        if number == -1:
            if number < Minimum:
                number = Minimum
            else:
                Minimum = Minimum
    if number == -1:
        print('program stops')
        break

print(Maximum)
print(Minimum)
