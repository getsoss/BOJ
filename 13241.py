a, b = map(int, input().split())

def gcd(num1, num2):
    if(num2 > num1):
        temp = num2
        num2 = num1
        num1 = temp
        
    if(num1 % num2 == 0):
        return num2
    
    else:
        temp = num2
        num2 = num1 % num2
        num1 = temp
        return gcd(num1, num2)

print(int(a * b / gcd(a, b)))

