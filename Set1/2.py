from binascii import hexlify, unhexlify

def byte_xor(a, b):
	return bytes([ x^y for (x,y) in zip(a, b)])

string1 = unhexlify("1c0111001f010100061a024b53535009181c")
string2 = unhexlify("686974207468652062756c6c277320657965")

resultado = hexlify(byte_xor(string1, string2))
print(resultado)
assert resultado == "746865206b696420646f6e277420706c6179".encode()