import math

def square(N,N2):
    for i in range(N,N2):
        yield i*i

N=1
N2=10+1

square(N,N2)

for i in square(N,N2):
    print(i)