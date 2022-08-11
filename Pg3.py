def isPrime(n):
    for i in range(2,(n//2)+1):
        if n%i == 0:
            return False
    return True

def sumAllDigits(n):
    sum=0
    while(n!=0):
        sum+=n%10
        n//=10
    return sum

num = int(input("Enter num = "))
print("Res = " ,(isPrime(num) and isPrime(sumAllDigits(num))))
