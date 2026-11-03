import pyaes
import base64

Version = int(input("Versión AES: "))
if Version == 128:
    Key = b"AMADOR52AMADOR52"
elif Version == 192:
    Key = b"AMADOR52AMADOR5212345678"
elif Version == 256:
    Key = b"AMADOR52AMADOR521234567812345678"

Imagen = input("Nombre de la imagen: ")
Ext = input("Extensión de la imagen: ")

k = pyaes.AESModeOfOperationECB(Key)

with open(Imagen + "." + Ext, "rb") as f:
    data = f.read()
Padding = 16 - (len(data) % 16)
data += bytes([Padding] * Padding)

Encrypted = b""
for i in range(0, len(data), 16):
    Encrypted += k.encrypt(data[i:i+16])
d = base64.b64encode(Encrypted)
d_h = base64.b64decode(d)
d_b = " ".join(format(byte, '08b') for byte in d_h)

with open("base64.txt", "w") as f:
    f.write(d.decode())
with open("bytes.txt", "wb") as f:
    f.write(d_h)
with open("bits.txt", "w") as f:
    f.write(d_b)

data_decrypted = b""
for i in range(0, len(d_h), 16):
    data_decrypted += k.decrypt(d_h[i:i+16])
Padding = data_decrypted[-1]
data_decrypted = data_decrypted[:-Padding]

with open("RTA." + Ext, "wb") as b:
    b.write(data_decrypted)

print("Key:\t", Key)
print("\nEncrypt:")
print(" - Base 64:\n ", d)
print(" - Bytes:\n ", d_h)
print(" - Bits:\n ", d_b)



