n = int(input())
nlist = list(map(int, input().split()))

sum_nlist = sum(nlist)
hap = 0

for i in nlist:
    sum_nlist -= i     
    hap += sum_nlist * i   

print(hap)
