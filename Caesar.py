def Caesar(Text,K=3,Encrypt=True):
    U_Text="".join(Text.upper().split())
    M=[U_Text[i:i+5] for i in range(0,len(U_Text), 5)]
    C=[]
    for i in M:
        c=""
        for l in i:
            if Encrypt:
                c+=chr(((ord(l)+K-65)%26)+65)
            else:
                c+=chr(((ord(l)-K-65)%26)+65)
        C.append(c)
    return " ".join(C)

Text=input("Mensaje: ")
K=int(input("k:\t "))

c=Caesar(Text,K)
print(f"Encrypted: {c}")
print(f"Decrypted: {Caesar(c,K,False)}")
