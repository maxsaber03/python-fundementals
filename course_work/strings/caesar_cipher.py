ALPHABET = "abcdefghijklmnopqrstuvwxyz "

def main():
    message = input("Enter the message to encode (letters + spaces only): ")
    key = int(input("Enter the key (integer shift): "))

    key = key % len(ALPHABET)
    shifted = ALPHABET[-key:] + ALPHABET[:-key]

    encoded = ""
    for char in message.lower():
        if char in ALPHABET:
            position = ALPHABET.index(char)
            encoded += shifted[position]
        else:
            print("Error: Unsupported character detected.")
            return

    decoded = ""
    for char in encoded:
        position = shifted.index(char)
        decoded += ALPHABET[position]

    print("Encoded Message:", encoded)
    print("Decoded Message:", decoded)

main()
