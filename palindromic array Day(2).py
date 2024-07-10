#Day 2
def PalinArray(arr):
    # Code here
    def pal(i):
        i = str(i)
        return i == i[::-1]
    a = all(pal(i) for i in arr)
    return a

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr):
            print("true")
        else:
            print("false")
