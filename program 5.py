#Write a program that takes inputs until user enters -1 and then prints the frequency of even and odd numbers.

finish = 0
even = 0
odd = 0
while finish == 0:
    number = int(input('enter your number please: '))
    if number % 2 == 0 and number != 0:
        even = even + 1
    if number % 2 != 0:
        odd = odd + 1
        if number == -1:
            odd = odd -1 
            break
    if number == -1:
        break
print('total numbers of evens are : ', even)
print('total numbers of odds are : ', odd)