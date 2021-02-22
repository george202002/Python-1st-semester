import string
import math

file = open("textdoc.txt", "r")

content = file.read()

content = content.translate(str.maketrans('', '', string.punctuation))
#print(content)
code = [ord(count) for count in content]

mul = 0
A = 0
C = 0
E = 0
G = 0
I = 0
K = 0
M = 0
O = 0
Q = 0
S = 0
U = 0
W = 0
Y = 0
a = 0
c = 0
e = 0
g = 0
i = 0
k = 0
m = 0
o = 0
q = 0
s = 0
u = 0
w = 0
y = 0
for count in code:
    if count != 32 and count % 2:
        mul = mul + 1
        if count == 65:
            A= A+1
        elif count== 67:
            C= C+1
        elif count== 69:
            E= E+1
        elif count== 71:
            G= G+1
        elif count== 73:
            I= I+1
        elif count== 75:
            K= K+1
        elif count== 77:
            M= M+1
        elif count== 79:
            O= O+1
        elif count== 81:
            Q= Q+1
        elif count== 83:
            S= S+1
        elif count== 85:
            U= U+1
        elif count== 87:
            W= W+1
        elif count== 89:
            Y= Y+1
        elif count== 97:
            a= a+1
        elif count== 99:
            c= c+1
        elif count== 101:
            e= e+1
        elif count== 103:
            g= g+1
        elif count== 105:
            i= i+1
        elif count== 107:
            k= k+1
        elif count== 109:
            m= m+1
        elif count== 111:
            o= o+1
        elif count== 113:
            q= q+1
        elif count== 115:
            s= s+1
        elif count== 117:
            u= u+1
        elif count== 119:
            w= w+1
        elif count== 121:
            y= y+1

print("A: ", math.ceil((A/mul)*100)*"*")
print("C: ", math.ceil((C/mul)*100)*"*")
print("E: ", math.ceil((E/mul)*100)*"*")
print("G: ", math.ceil((G/mul)*100)*"*")
print("I: ", math.ceil((I/mul)*100)*"*")
print("K: ", math.ceil((K/mul)*100)*"*")
print("M: ", math.ceil((M/mul)*100)*"*")
print("O: ", math.ceil((O/mul)*100)*"*")
print("Q: ", math.ceil((Q/mul)*100)*"*")
print("S: ", math.ceil((S/mul)*100)*"*")
print("U: ", math.ceil((U/mul)*100)*"*")
print("W: ", math.ceil((W/mul)*100)*"*")
print("Y: ", math.ceil((Y/mul)*100)*"*")
print("a: ", math.ceil((a/mul)*100)*"*")
print("c: ", math.ceil((c/mul)*100)*"*")
print("e: ", math.ceil((e/mul)*100)*"*")
print("g: ", math.ceil((g/mul)*100)*"*")
print("i: ", math.ceil((i/mul)*100)*"*")
print("k: ", math.ceil((k/mul)*100)*"*")
print("m: ", math.ceil((m/mul)*100)*"*")
print("o: ", math.ceil((o/mul)*100)*"*")
print("q: ", math.ceil((q/mul)*100)*"*")
print("s: ", math.ceil((s/mul)*100)*"*")
print("u: ", math.ceil((u/mul)*100)*"*")
print("w: ", math.ceil((w/mul)*100)*"*")
print("y: ", math.ceil((y/mul)*100)*"*")

file.close()
