x=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#print(x)
y=[]
z=[]
for i in x:
    y.append(i[::-1])
#print(y)
y.sort()
#print(y)
for j in y:
    z.append(j[::-1])
print(z)
