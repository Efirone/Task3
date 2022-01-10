max=0
summ=0
maxday=0
summweight=0
Lipkiweight=0
firstoctober=0
Starts=set()
Destinations=set()
file=open('travels.txt','r')
last=1
for i in file:
    L=i.split()
    Starts.add(L[2])
    Destinations.add(L[3])
    if(L[0]==last):
        summweight+=int(L[6])
        summ+=1
    else:
        if(summ>max):
            maxday=last
            max=summ
            maxweight=summweight
        summ=1
        summweight=int(L[6])
    last=L[0]
    if(L[2]=='Липки'):
        Lipkiweight+=int(L[6])
    if(L[0]=='1'):
        firstoctober+=int(L[4])

file.close()
print(maxday)
print(maxweight)
print()
print(Lipkiweight)
print()
print(firstoctober)
print()
L1=list(Starts)

file=open('travels.txt','r')
starts = {L1[i]: 0 for i in range(len(Starts))}
destinations = {L1[i]: 0 for i in range(len(Starts))}
for i in file:
    L=i.split()
    starts[L[2]]+=int(L[6])
    destinations[L[3]]+=int(L[6])
print(Starts)
print(len(Starts))
print(starts)
print()
print(Destinations)
print(len(Destinations))
print(destinations)
print()
file.close()
file=open('travels.txt','r')
fuel= {L1[i]: 0 for i in range(len(Starts))}
distance={L1[i]: 0 for i in range(len(Starts))}
for i in file:
    L=i.split()
    fuel[L[3]]+=int(L[5])
    distance[L[3]]+=int(L[4])



avgfuel={L1[i]: 0 for i in range(len(Starts))}
for i in L1:
    avgfuel[i]=fuel[i]/distance[i]
print(avgfuel)
file.close()
