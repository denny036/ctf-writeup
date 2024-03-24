expected_flag = 'ZT_YE\\0|akaY.LaLx0,aQR{"C'
decoded_flag = ""
for c in expected_flag:
    decoded_char = chr((ord(c) - 32) % 95 ^ 0xFF)
    decoded_flag += decoded_char

print(decoded_flag)
