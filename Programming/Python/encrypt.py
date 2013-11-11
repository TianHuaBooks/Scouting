
def enc(str):
	result = ""
	for i in str:
		result += chr(ord(i) ^ 13)
	return result

