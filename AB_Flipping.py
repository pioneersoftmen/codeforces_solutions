t = int(input())

for _ in range(t):
   n = int(input())
   s = input()
   A, B = list(), list()
   for i in range(n):
      if s[i] == 'A':
         A.append(i)
      if s[n - i - 1] == 'B':
         B.append(n - i - 1)
   print(A, B)
   count = 0

   for k in range(min(len(A), len(B))):
      if B[k] > A[k]:
         count += B[k] - A[-k - 1]
   
   print(count)
      
