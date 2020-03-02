a=[]
for m in range(3):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    #print(i,j,k,l)
                    a.append([m,i,j,k,l])
            
        
print(a[1][1])

p = 0
for i in range(81*3):
    count1 = 0
    for j in range(5):
        if a[i][j] == 1:
            count1 += 1
    if (count1 % 2) == 0:
        p += 1
print(p)


for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if 2*i+5*j+14*k == 41:
                print(i,j,k)

