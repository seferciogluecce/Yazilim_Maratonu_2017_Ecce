from collections import Counter

n,k = [int(arr_temp) for arr_temp in input().strip().split(' ')]
word=["" for x in range(0,n)]
for a in range(0,n):
    word[a]=input()
sına=int(input())
word.sort()
for t in range(0,sına):
    arama=1
    kel=input()
    if kel in word:
        for a in range(1,len(kel)):
            y=( [t for t in word if kel[:a]==t[:a]]  )
            if  y.index(kel) <= k - 1:
                print(a)
                break
            else:
                arama+=1
    else:
        print(-1)