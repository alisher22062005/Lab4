import math

def even_numbers(N):
    for i in range(N):
        if i%2==0:
            yield i
            

N=int(input())+1
result=""
for i in even_numbers(N):
    result=result+str(i)+","

print(result)
