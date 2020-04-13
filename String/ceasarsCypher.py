def caesarCipherEncryptor(string, key):
    # Write your code here.

    # Taking modulo very important here
    key = key % 26

    if key == 0:
        return string

    charArray = []

    for ch in string:
        new_idx = ord(ch) + key
        if new_idx > ord('z'):
            new_idx = ord('a') - 1 + new_idx % ord('z')
        charArray.append(chr(new_idx))
    return "".join(charArray)