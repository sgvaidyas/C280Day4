#Theo
def task1():
    n = int(input("Choose a number:\n"))
    n1 = n
    cnt = 0
    finalNum = 0
    temp = -1
    # Get count
    while n1 > 0:
        n1 = int(n1 / 10)
        cnt += 1

    if cnt % 2 == 1:
        temp = n % 10
        n = n // 10
        cnt -= 1

    for i in range(1, int(cnt/2)+1):
        a = n // 10 ** (cnt - 1)
        n = n % 10 ** (cnt - 1)
        b = n // 10 ** (cnt - 2)
        n = n % 10 ** (cnt - 2)
        finalNum = finalNum*100 + 10*b + a
        cnt -= 2
    if temp > -1:
        finalNum = finalNum*10 + temp

    print(finalNum)


if __name__ == '__main__':
    task1()


'''

i<3   a                    n               b         n         fn             cnt-=2
========================================================================================
1     1234//(10^3) = 1     1234%1000    234//100=2   234%100   0*100+10*2+1     2  
						   234						  34       21

2     34//10 =3            34%10=4       4//1 = 4     4        2100+10*4+3
                                                               2143             0

'''
