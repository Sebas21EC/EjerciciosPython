A=[1,5,2,3,4,1,8,3,1,6,1]
for i in range((len(A)-1),-1,-1):
    if A[i] in A[:i]:
        del(A[i]);

print(A)