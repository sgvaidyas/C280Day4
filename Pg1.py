#Olha
def get_length(n):
    len = 0
    while n > 0:
        len += 1
        n //= 10
    return len
n = int(input("Enter the number:"))
while n < 0:
    n = int(input("Enter the number:"))
length = get_length(n)
res = 0
start = 0
if length % 2 != 0:
    res += n % 10
    n //= 10
    start += 1
for i in range(start, length + 1, 2):
    first_num = n % 10
    second_num = (n % 100 - first_num) // 10
    print(first_num,second_num)
    res += second_num * 10**i
    res += first_num * 10**(i + 1)
    n //= 100
print(res)
'''
n = 12345
len = 5

res = 0
start = 0

res = 5
n = 1234
start = 1

for i in range(start, length + 1, 2):
    first_num = n % 10
    second_num = (n % 100) // 10
    res += second_num * 10**i
    res += first_num * 10**(i + 1)
    n //= 100


n      i  fn sc        res               n=n//100
-----------------------------------------------------
1234   1  4  34//10=3  5+(3*10)=35        12
                       35 += 4(100)=435
12     3  2  12//10=1  435+ (1*10^3)
                       435+1000=1435
                       1435+2*(10^4)
                       21435               0
0      5  0   0         ------------------------------------->    


'''
