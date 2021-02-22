n = int(input("Δώσε τον όρο της ακολουθίας Fibonacci: "))

n1, n2 = 0, 1
count = 0

if n < 0:
    print("Παρακαλώ δώστε έναν θετικό ακέραιο.")
elif n == 0:
    print("Ο", n,  "όρος είναι το 0")
elif n == 1:
    print("Ο αριθμός", n, "είναι πρώτος")
else:
    while count<n+1:
        x = n1 + n2
        n1 = n2
        n2 = x
        count += 1
    prime = True
    x = n2 - n1
    from random import randint
    for i in range(0,20):
        a = randint(2,1000000000000000000000000000000000000000000000000)
        if pow(a, x, x) != a % x: #(a ** x) % x = pow(a, x, x)
            print ("Ο αριθμός", x, "δεν είναι πρώτος")
            prime = False
            break
    if prime == True:
        print ("Ο αριθμός", x, "είναι πρώτος")
