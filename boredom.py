A=[0]*100001;a=b=0
for i in map(int,[*open(0)][1].split()):A[i]+=i
for i in A:a,b=max(a,b+i),a
print(a)