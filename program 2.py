#Write a program which prints the triangle Numbers sequence up to N. Take value of N as  input from the user.


num1 = 1
num2 = 2
N_limit = int(input('enter your limit please: '))
print(num1)
for i in range(N_limit-1):
    num1 = num1 +num2
    num2 = num2+1
    print(num1)


