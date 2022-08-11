n=int(input("Enter number: "))
cnt = 0
j=n**n
n1=n
while(n != 0):
    n = n // 10
    cnt += 1

n=n1
#25 = 625   cnt=2

#  625%(10^1) == n
if j%10**(cnt)==n:
    print("true")
else:
    print("false")
