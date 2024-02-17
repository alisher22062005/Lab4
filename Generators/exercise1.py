import math

def square_root(N):
    for i in range(N):
        yield i*i

N=int(input())+1
square_root(N)

for i in square_root(N):
    print(i)


