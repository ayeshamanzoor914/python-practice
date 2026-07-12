

# Binary to decimal
binary=input("Enter a binary number:") #python will take 1010 like string
decimal=int(binary,2 )
print("Decimal Equivalent:",decimal)
# num=23,23,34,56,78
# x=23
# i=0
# idx=0
# while   i<=len(num):
#     if(num[i]==x):
#         print("Found at idx:",i)
#         i+=1
# i=100 #counting 1 to 100
# while  i>=1:
#     print(i)
#     i-=1
# count vowels and consonants
# vowels_count=0
# consonants_count=0
# sentence=input("Enter a sentence:")
# vowels='AEIOUaeiou'
# for i in sentence:
#     if i in vowels:
#         vowels_count+=1
#     else:
#         consonants_count+=1
# print("Vowels",vowels_count)
# print("consonants",consonants_count)
# a= range(1,11,3)
# for i in range (len(a)):
#     print(a[i])
#prime numbers and their sum
# start=int(input("enter a number:"))
# end =int(input("enter a number:"))
# sum_prime=0
# print("prime numbers are:")
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num,end=',')
#             sum_prime+=num
# print("sum of prime numbers:",sum_prime)
# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
# cal_sum(2,6)
# def ave_3(a,b,c):#Average fun.
#     ave=(a+b+c)/3
#     print(ave)
# ave_3(a=4,b=5,c=8)
# ave_3(8,10,90)
# print("Ayesha manzoor",end=' ')
# print("Daughter of manzoor")
# def list_fruits ():
#     list="a","b","c","d","e"
#     print(list)

# def len_list(list): # to print length of a list #len=integer always
#     list=("apple","banana","orange")
#     print(len(list))
# len_list(list)

# def cal_fac(n):# factorial
#     fac=1
#     for i in range(2,n+1):
#         fac*=i
#     print(fac)
# cal_fac(2)
# def converter(USD):#convert usd to inr rupees
#     int=USD*200
#     print(USD,"USD=",int,"Inr")
# converter(3)
# def even_odd(n):
#     i=n
#     if (n%2==0):
#         print("Even")
#     else:
#         print("Odd")
# even_odd(11)
# def fact(n):
#     f=1
#     for i in range(n,n+1):
#         f=f*i
#     return f
# def permutations(n,r):
#     p=fact(n)/fact(n-r)
#     return p
# def combinations(n,r):
#     c=fact(n)/fact(r)*fact(n-r)
#     return c
# n=int(input("Enter the value of n:"))
# r=int(input("Enter the value of r:"))
# if r>n:
#     print("r should be less than n")
# else:
#     p=permutations(n,r)
#     c=combinations(n,r)
# print("permutations=",p)
# print("combinations=",c)
# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))
# large=lambda x,y:x if x>y else y
# num=large(a,b)
# print("Larger number is:")
# def table(n,x):
#     print("Table of")
#     for i in range(1,x+1):
#         print(n,"x",i,"=",n*i)
# limit=int(input("Enter range for table:"))
# table(num,limit)
# sentence=input("Enter a string:")
# upper=lambda x:x.upper()
# new_Text=upper(sentence)
# print("Upper text string:",new_Text)
# def invert(string):
#     rev=""
#     for i in string:
#         rev=i+rev
#     print("Reversed string:",rev)
# invert(new_Text)
# def f_c(f):
#     c=(f-32)*5/9
#     return c
# def c_f(c):
#     f=(9/5*c)+32
#     return f
# print("1:F to C")
# print("2: C to F")
# choice=int(input("Enter your choice of conversion:"))
# if choice==1:
#     f=float(input("Enter temperature in fahrenheit:"))
#     print("Temperature in celsius:",f_c(f))
# elif choice==2:
#     c=float(input("Enter temperature in celsius:"))
#     print("Temperature in fahrenheit:",c_f(c))
# n=int(input("Enter number of subjects:"))
# total_points=0
# total_credit=0
# for i in range(n):
#     print("Subject #",i+1)
#     grade=float(input("Enter grade points:"))
#     credit=int(input("Enter credit hours:"))
#     total_points=total_points+(grade*credit)
#     total_credit=total_credit+credit
# gpa=total_points/total_credit
# print("Your GPA is:",gpa)
# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))
# small=lambda x,y:x if x<y else y
# num=small(a,b)
# print("Smaller num is:",num)
# def square_table(n,r):
#     print("square table of:",n)
#     for i in range(1,r+1):
#         print(n,"^2 x",i,"=", (n**2)*i)
# limit=int(input("enter range:"))
# square_table(num,limit)
# upper= lambda x,y:x if x<y else y
# num=upper(a,b  )
# numbers=24,12,8,9,11
# even=list(filter(lambda x:x%2==0,numbers))
# print("even numbers:",even)












