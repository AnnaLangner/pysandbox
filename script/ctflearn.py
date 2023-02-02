
input = "BUH'tdy,|Bim5y~Bdt76yQ"
alphabet = "1234567890-=QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?qwertyuiop[]asdfghjkl;'\zxcvbnm,./"

def substitute(letter):
    idx = alphabet.find(letter)
    idx2 = idx-2
    if idx2 < 0:
        idx += len(alphabet)
    return alphabet[idx2]


output = ''.join([substitute(l) for l in input])
print(output)
