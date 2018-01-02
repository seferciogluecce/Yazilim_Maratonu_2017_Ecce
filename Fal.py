ben=input()
sen=input()


biz=[0 for x in range(0,len(ben))]
for a in range(0,len(ben)):

    biz[a]= abs(ord(ben[a])-ord(sen[a]) )

print(sum(biz))