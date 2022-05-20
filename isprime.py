lst = []
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
def primeinrange(i,j):
    for i in range(i,j+1):
        if i <=1:
            return False
        elif i == 2 :
            lst.append(i) 
        lst.append(i)         
num=int(input("Enter the number"))
print(isprime(num))
a=int(input("Enter the lower bound"))
b=int(input("Enter the upper bound"))
print(primeinrange(a,b))
print(lst)
