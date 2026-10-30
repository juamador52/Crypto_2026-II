def OTP(Text, Key):
    """
    Implementa OTP para cifrar o descifrar un mensaje
    
    Acepta el mensaje y la llave como cadenas de texto o bytes
    
    Retorna un mensaje cifrado o descifrado representado como bytes
    """
    if isinstance(Text, str):
        Text = Text.encode()

    if isinstance(Key, str):
        Key = Key.encode()

    if len(Text) != len(Key):
        raise ValueError("El mensaje y la llave deben tener la misma longitud")

    Crip = b""
    for i in range(len(Text)):
        Crip += bytes([Text[i] ^ Key[i]])

    return Crip


Text = input("Mensaje: ")
Key = input("Llave:\t ")

Crip = OTP(Text, Key)

print("\nEncriptado:")
print(f"   - Bytes:  {Crip}")
print(f"   - String: {Crip.decode()}")

Rta = OTP(Crip, Key)

print("\nDesencriptado:")
print(f"   - Bytes:  {Rta}")
print(f"   - String: {Rta.decode()}")

