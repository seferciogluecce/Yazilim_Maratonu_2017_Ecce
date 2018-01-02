
say=int(input())

for a in range(0,say):
    arr = []
    k=int(input())
    n=1
    bas=True
    last=0
    sayı=7
    arr.append(0)
    arr.append(sayı)

    if max(arr)>k:
        n=len(arr)
        while(bas):
            if arr[n-1]<k:
                print(arr[n-1])
                bas=False
    while(bas):
        if n==len(arr):
            arr.append(arr[n - 1] + 6)
        sayı=arr[n]
        if sayı < k:
            last = n
        elif sayı > k:
            print(last)
            bas = False
        n+=1

