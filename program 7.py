#[Perfect Square] Write a function perfectSquare() which takes a parameter N as input and returns 
#True if N is a perfect square else returns False.


# def perfectSquare(N):
#     flag = 0
#     if N > 1:
#         for i in range(N):
#             if i*i == N:
#                 flag = 1
#     if flag == 1:
#         print(N, 'is perfect square')
#     else:
#         print(N,'is not perfect square')      
# Number = int(input('enter your number please: '))
# perfectSquare(Number)




#Write a program that keeps on taking input from user, until the user enters -1 and prints 
#whether the input number is a complete square or not using the above.

# finish = 0
# while finish == 0:
#     flag = 0
#     N = int(input('enter your number please: '))
#     if N > 0:
#         for i in range(N):
#             if i*i == N:
#                 flag = 1
#         if flag == 1:
#             print(N, 'is perfect square')
#         else:
#             print(N, 'is not perfect square')        
#     if N == -1:
#         print('program stops')
#         break
     

finish = 0
while finish == 0:
    flag = 0
    num = int(input('enter your number please: '))
    for i in range(num):
        for j in range(num):
            c = i * j
            if (c == num) and (i == j):
                flag = 1
    if flag == 1:
        print('perfect square')
    else:
        print('not')
    if num == -1:
        print('program stops')
        break