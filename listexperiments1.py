L=[]
n = eval(input("Enter the length of the list:"))

for i in range(0,n):
    number=eval(input("Enter a number:"))
    L.append(number)

print("The List is: ")
print(L)

print("Total of of items in the list:")
print(len(L))

print("Last item of the List:")
print(L[-1])

left = 0
right = len(L)-1
while(left<right):
    temp=L[left]
    L[left]=L[right]
    L[right]=temp
    left+=1 
    right-=1 
print("List in reverse order:")
print(L)

if 5 in L:
    print("YES")
else:
    print("NO")

print("Number of 5 in the list:")
print(L.count(5))

del L[0]

del L[-1]

L.sort()
print(L)

count = 0
for i in range(0,len(L)):
    if L[i]<5:
        count+=1 
print("Item less than 5:")
print(count)