# finding cross product of 2 list
from itertools import product
#A=[1,2,3,4,5]
A = list(map(int, input("Enter A").split()))
B = list(map(int, input("Enter B").split()))
#B=[6,7,8]
cross_product=list(product(A,B))
print(cross_product)
                       
