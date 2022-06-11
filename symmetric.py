mystring=input()
n=len(mystring)
mid=n/2
l=[]
m=[]
count=0
if n%2==0:
    for x in range(0,int(mid)):
        l.append(mystring[x])
    for y in range(int(mid),n):
        m.append(mystring[y])
    if l==m:
        print("symmetric")
    else:
        print("non sym")
else:
    print("non symmetric")
        


        
