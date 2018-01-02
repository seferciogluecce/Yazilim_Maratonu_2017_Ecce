

sehir=int(input())

merd=[x[:] for x in [[999999]*sehir]*sehir]
for a in range(0,sehir) :
    merd[a][a]=0

for kt in range(0,sehir-1):
    x,y,z=[int (a) for a in input().split(" ")]
    merd[x-1][y-1]=z
    merd[y - 1][x - 1] = z


for i in range(0,sehir):
    for j in range( sehir):
        for k in range(sehir):
            merd[i][j] = min(merd[i][j],
                             merd[i][k] + merd[k][j]
                             )
print(merd)
sum=0
for a in range(sehir):
    for b in range(a,sehir):
        sum+=merd[a][b]

print(sum*2)

