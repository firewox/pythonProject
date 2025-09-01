def operate(a,b):
    a_fenzi,a_fenmu = a.split("/")
    b_fenzi,b_fenmu = b.split("/")

    a_fenzi_lst = list(a_fenzi)
    a_fenmu_lst = list(a_fenmu)
    b_fenzi_lst = list(b_fenzi)
    b_fenmu_lst = list(b_fenmu)

    for i in set(a_fenzi+a_fenmu):
        while i in a_fenzi_lst and i in b_fenzi_lst:
            a_fenzi_lst.remove(i)
            b_fenzi_lst.remove(i)
        while i in a_fenmu_lst and i in b_fenmu_lst:
            a_fenmu_lst.remove(i)
            #b_fenmu_lst.remove(i)
    return "".join(a_fenzi_lst)==b_fenzi and "".join(a_fenmu_lst)==b_fenmu


import sys
input = sys.stdin.read()
data = input().split()
T=int(data[0])
results=[]
index=1
for t in range(T):
    a,b = data[index],data[index+1]
    index += 2
    if operate(a,b):
        results.append("Yes")
    else:
        results.append("No")

for re in results:
    print(re)