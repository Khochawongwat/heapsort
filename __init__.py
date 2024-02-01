def heapify(X: list, n, i) -> any:
    mx = i

    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and X[i] < X[l]:
        mx = l

    if r < n and X[mx] < X[r]:
        mx = r

    if mx != i:
        X[i], X[mx] = X[mx], X[i]
        heapify(X, n, mx)


def heap_sort(X: list) -> list:
    n = len(X)

    for i in range(n, -1, -1):
        heapify(X, n, i)

    for i in range(n-1, 0, -1):
        X[i], X[0] = X[0], X[i]
        heapify(X, i, 0)
        
    return X