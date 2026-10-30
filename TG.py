import numpy as np

def Create_Grille(Size, Cells):
    Grille = np.zeros((Size, Size), dtype=int)
    for i in Cells:
        r = (i - 1) // Size
        c = (i - 1) % Size
        Grille[r][c] = 1
    return Grille

def Format(Text, Size):
    return " ".join(Text[i:i+Size] for i in range(0, len(Text), Size))

def Turning(Text, Size=2, Rot=1, Mode=1, Cells=[1]):
    U_Text = "".join(Text.upper().split())
    t = len(Cells)
    Block = Size * Size

    if len(U_Text) > Block:
        r = "".join(
            Turning(U_Text[i:i+Block], Size, Rot, Mode, Cells).replace(" ", "")
            for i in range(0, len(U_Text), Block))
        return Format(r, Size)
    Grille = Create_Grille(Size, Cells)
    Grid = np.full((Size, Size), "X", dtype=str)

    if Mode:
        m = [U_Text[i:i+t] for i in range(0, len(U_Text), t)]
        for n in range(4):
            a = 0
            for row, col in np.argwhere(Grille == 1):
                if n < len(m) and a < len(m[n]):
                    Grid[row][col] = m[n][a]
                a += 1

            Grille = np.rot90(Grille, -1 if Rot else 1)

        r = "".join(Grid.flatten())
    else:
        Grid = np.array(list(U_Text.ljust(Block, "X"))).reshape((Size, Size))
        r = ""

        for n in range(4):
            for row, col in np.argwhere(Grille == 1):
                r += Grid[row, col]

            Grille = np.rot90(Grille, -1 if Rot else 1)
    return Format(r, Size)



print("Encrypt:")
Text=input(" -Mensaje:   ")
Size=int(input(" -Tamaño:    "))
Rot=int(input(" -Dirección: "))           
Mode=int(input(" -Modo:      "))
Cells=input(" -Celdas:    ")
Cells=list(map(int,Cells.split()))
c=Turning(Text,Size,Rot,Mode,Cells)
print(f"\n -Ciphertext: {c}")

print("Encrypt:")
print(f" -Mensaje:   {c}")
print(f" -Tamaño:    {Size}")
print(f" -Dirección: {Rot}")           
print(" -Modo:      0")
print(f" -Celdas:    {str(Cells)}")
m=Turning(c,Size,Rot,0,Cells)
print(f"\n -Ciphertext: {m}")
     
                        
            
        
        
    
