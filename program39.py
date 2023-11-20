a=open("Demo.txt","r")
b=open("t","w")
c=a.readlines()
d=len(c)
for i in range(0,d):
    if i%2==0:
        b.write(c[i])
    else:
        pass
b.close()
b=open("t","r")
c=b.read()
print(c)
a.close()
b.close()

