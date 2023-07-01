def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True
    
    
inp = 600851475143
p = 1
l = set()

while True:
    if inp == 1:
        break
    
    if not isPrime(p):
        p += 1
        continue
        
    if inp % p == 0:
        inp /= p
        l.add(p)
    else:
        p += 1

print(max(l))
