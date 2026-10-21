from math import ceil
from collections import Counter

def overlaps(m,l,s):
 n=2*m+1
 I=set(range(l-1));J=set(range(l+3,m+3));U=I|J
 f=sum(1 for i in U if (i+s)%n in U)
 calc=(max(0,l-1-s)+max(0,m-l-s)
   +max(0,min(l-2,m+2-s)-max(0,l+3-s)+1)
   +max(0,min(l-2,s-m+1)-max(0,l+s-2*m+2)+1))
 assert f==calc,(m,l,s,f,calc)
 return f,U

def triple(U,n,a,b):return sum(1 for i in U if (i+a)%n in U and (i+b)%n in U)

cnt={'caseII':0,'caseIII':0,'generic':0}
for m in range(12,111):
 for l in range(4,m):
  for s in (1,2,3,4,5,m//2,m-1,m):
   overlaps(m,l,s);cnt['generic']+=1
 for p in range(4,(m+2)//2+1):
  if m%2==0 and p==m//2+1:continue
  l=max(5,p-2);q=m+2-p;r=m-1
  vals=[]
  for s in (p,q,r):
   f,U=overlaps(m,l,s);vals.append(f)
  expected=(m-9,4,5) if p<=6 else (m-p-2,p-3,5)
  assert tuple(vals)==expected,(m,p,'II',vals,expected)
  assert triple(U,2*m+1,p,m+2)==0,(m,p,'II t')
  cnt['caseII']+=1
 for p in range(2,(m+1)//2+1):
  if p==ceil(m/2):continue
  l=max(4,p-1);q=m+1-p;r=m
  vals=[]
  for s in (p,q,r):
   f,U=overlaps(m,l,s);vals.append(f)
  if p==2:expected=(m-5,4,5);T=2
  elif p==3:expected=(m-7,3,5);T=0
  elif p==4:expected=(m-8,3,5);T=0
  else:expected=(m-p-3,p-2,5);T=0
  assert tuple(vals)==expected,(m,p,'III',vals,expected)
  assert triple(U,2*m+1,p,m+1)==T,(m,p,'III t')
  cnt['caseIII']+=1
print('PASS',cnt)
