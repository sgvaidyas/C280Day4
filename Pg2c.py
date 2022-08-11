#patrik
n = int(input())
tempNum = n
count = 0
while tempNum!=0:
    tempNum//=10
    count +=1
def checkPower(number):
    rightdig= number**2%10**count
    if rightdig==number:
        return True
    else: return False
print(checkPower(n))
