def Armn (x):
    sum=0
    t=x
    while(t>0):
         d=t%10
         sum+=d**3
         t=t//10
    if sum==x:
       return "armstrong number"
    else:
       return "not a armstrong number"
x=int(input())
print(Armn(x))

   


