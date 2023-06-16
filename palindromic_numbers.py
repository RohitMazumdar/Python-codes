L=[]
for i in range(100,1000):
    if int(i/100)==int(i%10):
        L.append(i)
print(L)
