import time

## Generate Primes less than the given "n"
def Prime_gen(n):
    series = [True]*(n+1)
    series[0],series[1]=False,False
    for k in range(3,n+1,2):
        series[k+1]=False
        for j in range(k**2,n+1,2*k):
            series[j]=False
    return [var for var in range(0,len(series),1) if series[var]]

def gcd(a,b):
    while b != 0:
        a,b = b, a % b
    return a

def coprime(m, n):
    return gcd(m,n) == 1

n = 12000
prime_list = Prime_gen(n)
number_list = [var for var in range(0,n+1,1)]

numerators = [[i] for i in range(n+1)]

k = 0
st = time.clock()
for k in set(prime_list):
    for i in set(range(k,n+1,k)):
        number_list[i] = int(number_list[i]*(1-1/k))


count = 0
for i in range(2, len(number_list)):
    for j in range(1,i):
        if coprime(i,j) == True:
            # print("{0}/{1}".format(j,i))
            if j/i > 1/3 and j/i < 1/2:
                count +=1


print("result is",count,"and runtime is",time.clock()-st)