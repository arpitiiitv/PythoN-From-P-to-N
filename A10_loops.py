myList = []
for i in range(10):
    myList.append(i+1)
print(myList)

for item in myList:
    if(item%2==0):
        print(item ," is even")

j=0
while j < len(myList):
    print("while ->",myList[j])
    j=j+2
    
    
x=10
while x<0:
    print(x)
