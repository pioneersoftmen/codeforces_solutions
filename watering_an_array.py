t=int(input())

for i in range(t):
    
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))
    v=list(map(int,input().split()))
    
    m=0
    c=0
    
    for x in range(n):
        
        if a[x]==x+1:
            
            c+=1
            
    m=max(m,c+(d-1)//2)
    
    for x in range(min(2*n+2,d-1)):
        
        c=0
        
        for j in range(n):
            
            if j<v[x%k]:
                
                a[j]+=1
                
            if a[j]==j+1:
                
                c+=1
                
        m=max(m,c+(d-x-2)//2)
        
    print(m)