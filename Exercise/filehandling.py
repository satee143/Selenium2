__author__ = 'AMMA'
f=open('../drivers/abc.txt','r')
m=[]
line=f.readline()
for x in range(0,6):
    a=line.split()
    for x in a:
        m.append(x)

print(m)
