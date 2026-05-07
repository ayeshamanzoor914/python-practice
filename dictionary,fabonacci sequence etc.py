marks={"Ali":"20","Hamza":"60","Alina":"80"}
max_marks=max(marks,key=marks.get)
print(max_marks)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(4))
 remember #fib(4)=fib(3)+fib(2) #2+1=3
 fib(3)=fib(2)+fib(1) #1+1=2
 fib(2)=fib(1)+fib(0) #1+0=1

memo={}
def fib(n):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        memo[n]=fib(n-1)+fib(n-2)
        return memo[n]
print(fib(3))

names=["ali","hamza","muhammad"]
marks=[10,9,11]
for n, m in zip(names,marks):
    print("what is your name {0}? it is {1}." .format(n,m))

keys=[1,2,6]
values=[9,8]
print(dict(zip(keys,values)))