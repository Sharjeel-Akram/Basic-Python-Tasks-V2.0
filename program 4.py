#Write a function that takes a parameter N and returns the factorial of N.

num1 = int(input('enter your number please: '))
fact = 1
for i in range(num1):
    fact += fact*i
print('the factorial of number is ', fact)

#Write a function which will take two parameters and returns nPr (number of permutations).

def permutation(N,C):
    factN = 1
    for i in range(N):
        factN += factN*i
    factC = 1
    for i in range(C):
        factC += factC*i
    return factN // factC
N = int(input('enter your number please: '))
R = int(input('enter your number please: '))
C = N-R
permutation_N = permutation(N,C)
print('permutation of given numbers are: ', permutation_N)


#Write a function which will take two parameters and returns nCr (number of combinations). For a, b parts, use the function defined in question 5.

def Combination(N,C):
    factN = 1
    for i in range(N):
        factN += factN*i
    factR = 1
    for i in range(R):
        factR += factR*i
    factC = 1
    for i in range(C):
        factC += factC*i
    return factN // (factR * factC)
N = int(input('enter your number please: '))
R = int(input('enter your number please: '))
C = N-R
Combination_N = Combination(N,C)
print('Combination of given numbers are: ', Combination_N)
