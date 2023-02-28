n = int(input().strip())
if(n%2) != 0:
    print("Weird")
elif n in range(2,6) and (n%2==0):
    print("Not Weird")
elif n in range(6,21) and (n%2==0):
    print("Weird")
else:
    print("Not Weird")