import math

def square(N):
    for i in range(N):
        yield i*i

N=int(input())+1
square(N)

for i in square(N):
    print(i)


