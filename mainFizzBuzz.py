from cryptage import crypt, decrypt

msg = crypt("Hello World!", 3)
print(msg)
print(decrypt(msg))
