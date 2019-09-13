from binascii import hexlify, unhexlify

def byte_xor(a, b):
	return bytes([ x^y for (x,y) in zip(a, b)])

string1 = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal""".encode()
key = "ICE".encode()

resultado = b""
run = 0
for x in string1:
	char = byte_xor(bytes([key[run%3]]), bytes([x]))
	run+=1
	resultado += hexlify(char)

print(resultado)

assert resultado == """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f""".encode()