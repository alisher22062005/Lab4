def fromm_N_to_0(N):
    while N>=0:
        yield N
        N-=1


N=int(input())
fromm_N_to_0(N)

for i in fromm_N_to_0(N):
    print(i)
