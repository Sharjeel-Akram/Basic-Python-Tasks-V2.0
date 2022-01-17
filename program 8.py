#Write a function which takes a number N as parameter and tells whether N is a prime number 
#or not (returns true when N is a prime else return False).


# def prime_Number(N):
#     flag = 0
#     if num > 1:
#         flag = 1
#         for i in range(2,(num-1)):
#             if num % i == 0: 
#                 flag = 0
#     if num == 2:
#         flag = 1
#     if flag == 1:
#         print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")

# num = int(input("Enter your number please: "))
# prime_Number(num)

#task2
# def Factors(Num):
#     factor=[]
    
#     for i in range(2,Num):
#         if Num%i==0:
#             flag=False
#             for j in range(2,int(i/2+1)):
#                 if i % j ==0:
#                     flag=True
#                     break
#             if flag==False:
#                 factor.append(i)

#     return factor     
# print(Factors(25))   
def LargestPrime(num):
    primefactor=1
    i=2
    while i <= num/i:
        if num%i==0:
            primefactor=i
            num/=i
        else:
            i+=1
    
    if primefactor < num:
        primefactor=num
    return primefactor
print(LargestPrime(25))