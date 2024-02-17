import math

def even_numbers(N):
    for i in range(N):
        if i%2==0:
            yield i

N=int(input())+1
print(list(even_numbers(N)))
