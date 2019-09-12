from binascii import hexlify, unhexlify

def byte_xor(a, b):
	return bytes([ x^y for (x,y) in zip(a, b)])

with open("4.txt", "r") as file:
	hashes = file.readlines()
	for hashe in hashes:
		string1 = unhexlify(hashe[:-1])
		for x in range(1, 255):
			tentativa = b""
			for y in string1:
				char = byte_xor(bytes([x]), bytes([y]))
				if int.from_bytes(char, byteorder='big') >= 32 and int.from_bytes(char, byteorder='big') <= 122:
					tentativa += char
				else:
					break
			if len(tentativa) == 29:
				print(tentativa)
#b'Now that the party is jumping'