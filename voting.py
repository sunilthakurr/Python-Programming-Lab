def vote_not(a):
    return a>=18
age=int(input("Enter the age"))
out=vote_not(age) 
print(out)           
#[i for i in a if fn_name(value)]