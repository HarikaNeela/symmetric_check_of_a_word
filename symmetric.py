'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

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
'''
print(l)
print(m)

for p in range(0):
    if(l[p]==m[p]):
        count+=1
if count==mid:
    print("symmetric")
else:
    print("non sym")
        
    '''
if l==m:
        print("symmetric")
else:
    print("non sym")
        


    
        