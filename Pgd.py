#Andrei
n = eval(input("Please enter a number: "))

squared = n * n
lenOG = len(str(n))
divisor = 10 ** lenOG
if squared - (n % divisor) == (squared // divisor) * divisor:
    print(True)
else:
    print(False)
