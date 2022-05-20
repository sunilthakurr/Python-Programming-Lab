def ar_pr_circle(r):
    return 3.14*r*r,2*3.14*r
r=float(input("Enter the radius of curcle"))   
out1, out2=ar_pr_circle(r)
print(f'area of circle is{out1} and circumference is {out2}')