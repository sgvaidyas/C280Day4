#harvey
n = int(input("Enter a value: "))
cnt = 0
n1 = n
while n1 != 0:
    n1 = n1 // 10
    cnt += 1

nSqr = n * n    #25
lastDig = nSqr % (10 ** cnt)  #25%10 = 5

if n == lastDig:
    print(True)
else:
    print(False)
