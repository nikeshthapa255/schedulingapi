#lehoczy

"""
INPUT
3
7 3
12 3
20 5
"""

def check(i, p, c):
    j=list(range(i+1))
    k=[]
    for l in j:
        k.extend(list(range(p[i]//p[l] )))
    s=set([(m+1)*(p[i]//p[l]) for l in j for m in k])
    print(i,j,k,s)
    for t in s:
        ch=sum([ c[idx]*((t+p[idx]-1)//p[idx]) for idx in j])
        #print(i,ch)
        if ch<p[i]:
            return True
    return False

num=int(input())
p,c=[],[]
for _ in range(num):
    i,j=map(int,input().split())
    p.append(i)
    c.append(j)
priority=list(range(num))
#RM
priority.sort(key=lambda x:c[x])
p=[p[i] for i in priority]
c=[c[i] for i in priority]

print(p,c)
ans=[False for _ in range(num)]
for i in range(num):
    ans[i]=check(i,p,c)

print(*priority, sep="\t")
print(*ans, sep="\t")
