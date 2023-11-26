import random
import math
l=[]
pp=[]
prompt=input("Enter string: ")
for i in prompt:
    l.append(ord(i))
    
c=len(prompt)
fa=[]
pr=list(prompt)
for i in pr:
    fa.append(pr.count(i))
   
fu=1
for i in set(fa):
    fu*=math.factorial(i)
 
fact= round(math.factorial(c)/fu)

p=''
count=0
s=''
l1=l.copy()
while True:
    if len(pp) != fact:
        for i in range (c):
            if l!= []:
                a=random.choice(l)
                l.remove(a)
                s+=(chr(a))
        if s not in pp:
            pp.append(s)
            
        s=''
        l=l1.copy()
    else:
        break


print()
print("ALl POSSIBLE PERMUATIONS OF THE ENTERED STRING:",len(pp))
print()
print(pp)

   


