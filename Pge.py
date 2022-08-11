n = int(input("Enter n ="))
contains = True
n1 = n
while (contains):
  print(n1,end = "")
  n1 = n1**2
  count = 0
  n2 = n1
  while (n2!=0):
    n2=n2//10
    count +=1
  if(n1%10**(count-1)==n):
    print(" = ",n1)
    contains = True
  else:
    print(" = ",n1)
    contains = False
  n=n1
