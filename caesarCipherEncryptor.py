def caesarCipherEncryptor(string, key):
    # Write your code here.
    alphabet = [chr(x) for x in range(97, 123)]
    res = []
    for char in string:
        res.append(alphabet[(alphabet.index(char) + key) % 26])

    return "".join(res)
