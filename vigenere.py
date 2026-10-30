def Vigenere(Text, Key, t,Encrypt=True):
    U_Text = "".join(Text.upper().split())
    Key=Key.upper()
    c = ""
    for i in range(len(U_Text)):
        ro=ord(Key[i%len(Key)])-65
        co=ord(U_Text[i])-65
        if Encrypt:
            c+= chr((ro+co)%26+65)
        else:
            c+= chr((co-ro)%26+65)          
    c=[c[n:n+t] for n in range(0, len(c), t)]
    return " ".join(c)

print("Encrypted")
e_Text=input("  *Plaintext: ")
e_Key=input("\t*Key: ")
e_t=int(input("\t*t:   "))
print(f"Ciphertext: {Vigenere(e_Text,e_Key,e_t)}")

print("\nDecrypted")
d_Text=input("  *Ciphertext: ")
d_Key=input("\t*Key:  ")
d_t=int(input("\t*t:    "))
print(f"Plaintext: {Vigenere(d_Text,d_Key,d_t,False)}")






    
