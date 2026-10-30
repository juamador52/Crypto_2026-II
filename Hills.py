import numpy as np

def Inverse_Key(Key,x):
    adj = np.array([[Key[1][1],-Key[0][1]],
                    [-Key[1][0],Key[0][0]]])
    I_Key = x*adj
    for i in [0,1]:
        for j in [0,1]:
            I_Key[i][j]=I_Key[i][j]%26
    return I_Key

def EEA(a, b):
    if b == 0:
        return (a, 1, 0)

    q = a // b
    d0, x0, y0 = EEA(b, a % b)

    d,x,y = d0,y0,x0 - q*y0
    return (d, x, y)

def Hills(Text, Key, Inverse=False,P=False):
    det = int(round(np.linalg.det(Key)))
    det = det % 26
    if not det:
        raise ValueError("La matrix no es invertible, Det(A)=0")
    d,x,y=EEA(det,26)
    if d!=1:
        raise ValueError("La matrix no es invertible")
    if Inverse:
        Key = Inverse_Key(Key,x)
        if P:
            print("Inversa: ", Key[0])
            print("\t ", Key[1])
    
    alp = {chr(i+65):i for i in range(26)}
    U_Text = "".join(Text.upper().split())
    
    m = [U_Text[i:i+2] for i in range(0,len(U_Text),2)]
    c=""
    for pair in m:
        if len(pair)==1:
            m0 = alp[pair]
            r=m0*Key[0][0]+m0*Key[1][0]
            c+=chr(r%26+65)
            continue
            
        m0,m1=alp[pair[0]],alp[pair[1]]
        r=np.array([m0,m1])@Key
        c+=chr(r[0]%26+65)
        c+=chr(r[1]%26+65)

    return c

print("Encrypt:")
Text = input("Mensaje: ")
in0 = input("Clave:\t ")
in1 = input("\t ")

row0 = list(map(int, in0.split()))
row1 = list(map(int, in1.split()))

Key = np.array([row0,row1])

print(f"Ciphertext: {Hills(Text,Key)}")
print("\nDecrypt:")
Text = input("Mensaje: ")
in0 = input("Clave:\t ")
in1 = input("\t ")

row0 = list(map(int, in0.split()))
row1 = list(map(int, in1.split()))

Key = np.array([row0,row1])

print(f"Plaintext: {Hills(Text,Key,True,True)}")


     
    
