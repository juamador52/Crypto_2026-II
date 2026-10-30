def Create_Key(Text):
    alp = [chr(n) for n in range(65, 91)]
    alp.remove("J")
    Key = []
    a = []
    for n in Text.upper():
        if n in ("I","J"):
            n = "I"
        if n not in alp:
            continue
        a.append(n.replace("I","I/J"))
        alp.remove(n)
        if len(a)==5:
            Key.append(a)
            a=[]
    for n in alp:
        if n == "I":
            n = "I/J"
        a.append(n)
        if len(a)==5:
            Key.append(a)
            a=[]
    return Key
        

def Playfair(Text, Key, Encrypt = True):
    T = "".join(Text.upper().split())
    P = [] 
    i = 0 
    while i<len(T): 
        pair = "" 
        a = T[i] 
        if i+1<len(T) and T[i]==T[i+1]: 
            pair += a+"X" 
            i += 1 
        else: 
            pair += a 
            if i+1<len(T): 
                pair += T[i+1] 
                i += 2 
            else: 
                pair += "X" 
                i += 1 
        P.append(pair) 

    i=0
    b=0
    dict_Key = {}
    for m in Key:
        for n in m:
            if i==5:
                i=0
                b+=1

            if n == "I/J":
                dict_Key["J"]=(b,i)
                dict_Key["I"]=(b,i)
                i+=1
                continue
            dict_Key[n]=(b,i)
            i+=1
        
    c=[]
    a=""
    for n in P:
        if Encrypt: 
            #same column 
            if dict_Key[n[0]][1]==dict_Key[n[1]][1]: 
                a+=Key[(dict_Key[n[0]][0]+1)%5][dict_Key[n[0]][1]] 
                a+=Key[(dict_Key[n[1]][0]+1)%5][dict_Key[n[1]][1]] 
            #same row 
            elif dict_Key[n[0]][0]==dict_Key[n[1]][0]: 
                a+=Key[dict_Key[n[0]][0]][(dict_Key[n[0]][1]+1)%5] 
                a+=Key[dict_Key[n[1]][0]][(dict_Key[n[1]][1]+1)%5]
                
        if (not Encrypt):
            #same column
            if dict_Key[n[0]][1]==dict_Key[n[1]][1]:
                a+=Key[(dict_Key[n[0]][0]-1)%5][dict_Key[n[0]][1]]
                a+=Key[(dict_Key[n[1]][0]-1)%5][dict_Key[n[1]][1]]
            #same row
            elif dict_Key[n[0]][0]==dict_Key[n[1]][0]:
                a+=Key[dict_Key[n[0]][0]][(dict_Key[n[0]][1]-1)%5]
                a+=Key[dict_Key[n[1]][0]][(dict_Key[n[1]][1]-1)%5]
        #Neither
        if not a:
            a += Key[dict_Key[n[0]][0]][dict_Key[n[1]][1]]
            a += Key[dict_Key[n[1]][0]][dict_Key[n[0]][1]]

        c.append(a)
        a=""
    u = " " if Encrypt else ""
    return u.join(c)

Plaintext=input("Mensaje: ")
Text=input("Palabra Clave: ")

Key=Create_Key(Text)
print("\nKey:", end="")
for n in Key:
    print(f"\t{n}")

c=Playfair(Plaintext, Key)
print(f"\nEncrypted: {c}")

m=Playfair(c, Key, False)
print(f"\nDecrypted: {m}")
