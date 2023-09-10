from string import punctuation

alphabet = list(punctuation)
data = "bHEC_T]PLKJ{MW{AdW]Y"

def main():
    for key in alphabet:
        decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in data])
        if "Flag{" in decrypted:
            print(decrypted)
            break

if __name__ == "__main__":
    main()
