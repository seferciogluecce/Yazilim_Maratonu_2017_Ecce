from collections import Counter
t =int(input())

for a in range(0,t):
    bound=[int(x) for x in input().split("\t")]
    keo,eli=0,0
    for y in range(bound[0],bound[1]+1):
        print("**********************************")
        print(y,bin(y),str(bin(y)).count('0'),str(bin(y)).count('1'))

        if(str(bin(y)).count('1')%2==0):
            print("keo win")
        heap=[int(a) for a in str(y)]
        c=Counter(heap)
        #print(heap)
        x = 0
        for val in heap:
            print(x,val)

            x = x ^ val
        #print(x)

        if x > 0:
            print("keo wins", y)
            keo+=1
        else:
            eli+=1
            print("eli wins",y)
    print(keo,eli)


