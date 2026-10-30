import random

def CL(Freq, Seed=0):
    Layout={chr(i+65):[Freq[i],[]] for i in range(0,26)}
    M={i for i in range(100)}
    
    if Seed:
        random.seed(Seed)
    else:
        random.seed()

    for i in Layout:
        In_M = random.sample(list(M), Layout[i][0])
        Layout[i][1] = In_M
        M-=set(In_M)
    return Layout

def HC(Text,Layout,Encrypt=True,Seed=0):
    if Seed:
        random.seed(Seed)
    else:
        random.seed()
    
    if Encrypt:
        U_Text=Text.upper().split()
        m="".join(U_Text)
        c = []      
        for i in m:
            c.append(str(random.choice(Layout[i][1])))
        c=" ".join(c)
    else:
        U_Text=Text.split()
        m=list(map(int,U_Text))
        c = ""
        for n in m:
            for i in Layout:
                if n in Layout[i][1]:
                    c+=i
                    break
    return c
        
#Usare la misma frecuencia que el de clase
Freq = [8,2,3,4,12,2,2,6,6,1,1,4,2,6,7,2,1,6,6,9,3,1,2,1,2,1]
m=100
Seed = int(input("Semilla: "))

Layout = CL(Freq,Seed)
print("Layout:")
for i in Layout:
    print(f" {i}: {Layout[i][1]}")

print("Encrypt:")
Plaintext = input(" -Mensaje: ")
c = HC(Plaintext, Layout, True, Seed)
print(f" -Cifrado: {c}")

print("\nDecrypt:")
print(f" -Cifrado: {c}")
m = HC(c, Layout, False)
print(f" -Mensaje: {m}")



