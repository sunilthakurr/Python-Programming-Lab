n=int(input())
lst=[]
count=0
for i in range(n):
    a=int(input())
    lst.append(a)
    if a%2==0:
        count+=1
if count > n//2:
    print("READY FOR BATTLE")
else:
    print("NOT READY")           
