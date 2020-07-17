def edit_distance(a, b):
    T = [[float("inf")] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        T[i][0] = i*cost[1]
    for j in range(len(b) + 1):
        T[0][j] = j*cost[0]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                T[i][j] = T[i - 1][j - 1]
            else:
                T[i][j] = min((T[i - 1][j] +cost[1]),(T[i][j - 1] + cost[0]), (T[i - 1][j - 1] +cost[2]))
    return T[len(a)][len(b)]

n=list(map(int,input().split()))
a=input()
b=input()
cost=list(map(int,input().split()))
print(edit_distance(a,b))