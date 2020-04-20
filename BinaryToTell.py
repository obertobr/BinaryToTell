import mouse
import time
import winsound

#texto > binario

b = input("palavra:").encode() #transforma oque você escreveu em bits
bi = int.from_bytes(b, "big") 
bs = bin(bi) # transforma em binario
bi = bs[2:]
print(bi)

#binario > som

for a in bi:
    if a == "1":
        winsound.Beep(1000,100) # se for 1 da um beep de 1000hz
        print(1)
    else:
        winsound.Beep(500,100) # se for 0 da um beep de 500hz
        print(0)
    winsound.Beep(2000,100) # quando acbar da um beep de 2000hz

#binario > texto

binary_int = int(bi, 2)
byte_number = binary_int.bit_length() + 7 // 8
binary_array = binary_int.to_bytes(byte_number, "big")
ascii_text = binary_array.decode()

print(ascii_text[int(byte_number - (byte_number/8)):])