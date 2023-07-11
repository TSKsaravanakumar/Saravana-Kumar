def string(x):
    #print(a)
    global a, b
    a=0
    b=0
    for i in x:
     #print(i)
     if i.isupper():
        a=a+1
     else:
        b=b+1
    return a,b
string("The quick Brow Fox".replace(" ",""))
print("No. of Upper case characters :",a)
print("No. of Lower case Characters :",b)