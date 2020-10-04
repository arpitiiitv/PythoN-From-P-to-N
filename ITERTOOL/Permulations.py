from itertools import permutations

S=input("Enter string:")
P= list(map(int,input("Enter list:").split()))
k=5 #length of required Permutation
#provide sorted string will get sorted permutation
li=list(permutations(sorted(S),k))
lj= list(permutations(sorted(P),k))
print(len(li))
print(len(lj))
for i in li:
    print(''.join(i))
for j in lj:
    print(j)
