def power(a1,a2):
    res=a1
    for i in range(0,a2):
        res*=a1
    return res
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))   
out=power(a,b)    
print(out)
