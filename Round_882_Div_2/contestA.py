t = int(input())

for j in range(t):
    n, k = map(int, input().split())

    ar = [0] * (n - 1)
    a = list(map(int, input().split()))

    for i in range(n - 1):
        ar[i] = abs(a[i] - a[i + 1])

    ar.sort()
    res = sum(ar[0:n-k])
    print(res)

