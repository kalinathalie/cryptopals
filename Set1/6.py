from binascii import hexlify, unhexlify

def byte_xor(a, b):
	return bytes([ x^y for (x,y) in zip(a, b)])
