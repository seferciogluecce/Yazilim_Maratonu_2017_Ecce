m=input().split("\t")
bina=int(m[0]) #y
kat=int(m[1]) #x

cost=[x[:] for x in [[0]*bina]*kat]
minCost=cost[:][:]

for i in range(0,kat):
    tekkat=input().split("\t")
    for j in range(0,bina):
        cost[i][j]=int(tekkat[j])
        if j>0:
            minCost[0][j] = minCost[0][j - 1] + cost[0][j]
    if i>0:
        minCost[i][0] = minCost[i - 1][0] + cost[i][0]


for i in range(1,kat):
    for j in range(1,bina):
        minCost[i][j]=min(list(zip(*minCost))[j-1][:i+1])+cost[i][j]

print(min(list(zip(*minCost))[bina-1][:kat]))

