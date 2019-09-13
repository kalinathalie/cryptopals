from Crypto.Cipher import AES
from base64 import b64decode
key = b'YELLOW SUBMARINE'

with open("7.txt", "r") as file:
	encrypted = b64decode(file.read())
	cipher = AES.new(key, AES.MODE_ECB)
	decrypted = cipher.decrypt(encrypted).decode()
	print(decrypted)