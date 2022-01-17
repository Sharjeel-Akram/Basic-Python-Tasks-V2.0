#Write a Program which finds a triplet a, b and c (3 integers) whose sum satisfies this: 
#a2 + b2 + c2 = 1000


# def Square_Function(Number):
#     for i in range(Number):
     
#         for j in range(Number):
        
#             for k in range(Number):
            
#                 if ((i*i) + (j*j) + (k*k) ) == Number:
#                     print(i, j, k)          
# Number = 1000
# Square_Function(Number)


#. write a Program which Prints all the triplet a, b and c which satisfies this: a + b + c = 1000


# def Square_Function(Number):
#     for i in range(Number):
     
#         for j in range(Number):
        
#             for k in range(Number):
            
#                 if (i +j + k) == Number:
#                     print(i, j, k)          
# Number = 1000
# Square_Function(Number)


#Find three consecutive numbers whose multiplication is equal to the Required Number, (Your 
#program should prompt for the number N and outputs 3-numbers those if we multiply equals 
#to N. Also, if there isn’t any 3– tuple of numbers then it should say NO).
def consecutive(num):

    for a in range(num):
        for b in range(num):
            for c in range(num):
                if a*b*c==num:
                    print(a,b,c)
number=int(input('enter number'))
consecutive(number)