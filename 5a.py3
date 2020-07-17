def lis(A):
    T = [None] * len(A)

    for i in range(len(A)):
        T[i] = 1
        for j in range(i):
            if A[j] < A[i] and T[i] < T[j] + 1:
                T[i] = T[j] + 1

    return max(T[i] for i in range(len(A)))

n=input()
A=list(map(int,input().split()))
print(lis(A))