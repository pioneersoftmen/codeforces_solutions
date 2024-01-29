for s in [*open(0)][2::2]:
 n=len(a:=sorted(list(map(int, s.split()))));j=n-1;b=sum(a);c=b//2
 while c>0:c-=a[j];j-=1
 print((b+1)//2+n-j-1)