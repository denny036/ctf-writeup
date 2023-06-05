for c in flag:
	encoded_char = chr((ord(c) ^ 0xFF) % 95 + 32)
print(encoded_char)
