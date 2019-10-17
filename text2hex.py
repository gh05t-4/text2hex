# Created by SKS bros.

text = input("Enter the text: ")
hexval = ""

for i in text:
    h = hex(ord(i))
    hexval = hexval + h + " "

print("\nHex:\n\n" + hexval)
print("\n")
