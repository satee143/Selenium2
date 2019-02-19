__author__ = 'AMMA'
f=open('../drivers/abc.txt',"r")
d=[]
for x in f:
    d=x.split()
    print(d[1])
    #print(d)


