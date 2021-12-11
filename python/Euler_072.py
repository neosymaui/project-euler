import time

def Prime_gen(n):
    series = [True]*(n+1)
    series[0],series[1]=False,False
    for k in range(3,n+1,2):
        series[k+1]=False
        for j in range(k**2,n+1,2*k):
            series[j]=False
    return [var for var in range(0,len(series),1) if series[var]]

n = 1000000
prime_list = Prime_gen(n)
number_list = [var for var in range(0,n+1,1)]
k = 0
st = time.clock()
for k in set(prime_list):
    for i in set(range(k,n+1,k)):
        number_list[i] = int(number_list[i]*(1-1/k))
print(number_list)
print("result is",sum(number_list)-1,"and runtime is",time.clock()-st)