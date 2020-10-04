from itertools import combinations_with_replacement as cwr
S="ARPIT"
P= list(map(int, input("enter list").split()))
k=int(input("Enter the length of substring")) #LENGTH OF SUBSTRING OF s
Combination_result=list(cwr(S,k))
combination_res= list(cwr(P,k))
print(len(Combination_result))
print(len(combination_res))
for i in Combination_result:
    print(''.join(i),end=",")
for i in combination_res:
    print(i)
    
