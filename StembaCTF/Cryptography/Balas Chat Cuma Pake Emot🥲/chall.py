flag = open('flag.txt','r').read()
emot = open('cipher.emot','wb')
mapper = dict([(i-0x1f443,chr(i)) for i in range(0x1f443,0x1f44b)])

cipher = ""
for i in flag:
    n = ord(i)
    res = ""
    while n:
        m = int(n % len(mapper) )
        res += mapper[m]
        n //= 6
    cipher += res
    cipher += "_"

emot.write(cipher.encode())
