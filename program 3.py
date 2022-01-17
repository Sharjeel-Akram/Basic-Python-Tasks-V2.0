#Write a Function which takes as parameter N and returns N’th Triangle Number.



def triangular_Numbers(N):
    num1 = 1
    num2 = 2
    for i in range(N_limit-1):
        i = i             # this is just for no reason just to  use i variable
        num1 = num1 +num2
        num2 = num2+1
    print('nth term is :', num1)
N_limit = int(input('enter your limit please: ')) 
triangular_Numbers(N_limit)