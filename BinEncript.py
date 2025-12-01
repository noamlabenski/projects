file = input("enter the file name to encrypt or decrypt: ")

with open(file, "rb") as f:
    data = f.read()

enc = bytes([b ^ 5 for b in data])

with open(file, "wb") as f:
    f.write(enc)