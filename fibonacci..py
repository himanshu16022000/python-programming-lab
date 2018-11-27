n=int(input())
a=0
b=1
count=0
l=[]
if n<=0:
   print("enter positive no.)
elif n==1:
     print("0")
elif n==2:
     print("0,1)
else:
     l.append(0)
     l.append(1)
while count<n-2:
      l.append(a+b)
      c=a+b
      a=b
      b=c
     count+=1
 
print(l)  
