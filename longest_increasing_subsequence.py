def index(arr, key, l, r):
    while (r - l) > 1:
        m = l + (r - l) // 2
        if arr[m] >= key:
            r = m
        else:
            l = m
    return r if arr[l] < key else l


def lis(arr, N):
    result = [0] * (N + 1)
    result[0] = float('-inf')
    curr = 1
    for i in range(N):
        if arr[i] > result[curr - 1]:
            result[curr] = arr[i]
            curr += 1
        elif arr[i] < result[1]:
            result[1] = arr[i]
        else:
            result[index(result, arr[i], 1, curr)] = arr[i]
    return curr - 1

if __name__ == '__main__':
    N = 10
    arr = [5, 6, 4, 3, 5, 6, 10, 7, 8, 9]
    print(lis(arr, N))

