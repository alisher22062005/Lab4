import math

def div_3_and_4(N):
    for i in range(N):
        if i%3==0 and i%4==0:
            yield i

N=int(input())+1
for i in div_3_and_4(N):
    print(i)

