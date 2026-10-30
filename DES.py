from pyDes import *
import base64

Key = b"AMADOR52"

Imagen = input("Nombre de la imagen: ")
Ext = input("Extensión de la imagen: ")

k = des(Key, ECB, pad=None, padmode=PAD_PKCS5)

with open(Imagen+"."+Ext, "rb") as f:
    data = f.read()
d = base64.b64encode(k.encrypt(data))

d_h = base64.b64decode(d)
d_b = " ".join(format(byte, '08b') for byte in d_h)
data_decrypted = k.decrypt(d_h)
with open("RTA."+Ext, "wb") as b:
    b.write(data_decrypted)


print("Key:\t", Key)
print("\nEncrypt:")
print(" -Base 64: ")
print(" ", d)
print(" -Bytes: ")
print(" ", d_h)
print(" -Bits: ")
print(" ", d_b)

