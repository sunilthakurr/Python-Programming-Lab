def isprime(n):
    count=0
    if n <=1:
        return False
    elif n == 2:
        return True    
    for _ in range(2,(n//2)+1):
        if n%_ == 0:
            return False
    return True
         
num=int(input("Enter the number"))
print(isprime(num))
