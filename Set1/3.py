from binascii import hexlify, unhexlify

def byte_xor(a, b):
	return bytes([ x^y for (x,y) in zip(a, b)])

string1 = unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

for x in range(1, 255):
	tentativa = b""
	for y in string1:
		char = byte_xor(bytes([x]), bytes([y]))
		if int.from_bytes(char, byteorder='big') >= 32 and int.from_bytes(char, byteorder='big') <= 122:
			tentativa += char
		else:
			break
	if len(tentativa) == 34:
		print(tentativa)

#b"Cooking MC's like a pound of bacon"