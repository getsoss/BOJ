n = int(input())
sum_gcdList = []

def gcd(a, b):
    if a % b == 0:
        return b

    else:
        return gcd(b, a % b)

for _ in range(n):
    n_list = list(map(int, input().split()))
    del n_list[0]
    n_list.sort(reverse = True)
    sum_gcd = 0
    for i in range(len(n_list)):
        for j in range(len(n_list)):
            if i > j:
                sum_gcd += gcd(n_list[i], n_list[j])
    sum_gcdList.append(sum_gcd)

for i in sum_gcdList:
    print(i)
    
