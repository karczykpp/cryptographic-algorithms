import math

def RSA_Algorythm():
    p = 1249
    q = 9967
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    while e < phi:
        if math.gcd(e, phi) == 1:
            break
        e += 1
    d = pow(e, -1, phi)
    print(d)
    print("Klucz publiczny: (", e, ",", n, ")")
    print("Klucz prywatny: (", d, ",", n, ")")

    message = "Nazywam się Jakub Karcz i studuję informatykę na Politechnice Poznańskiej."
    print(f". Wiadomość do zaszyfrowania:")
    print(f"   '{message}'")
    encrypted_msg = [pow(ord(char), e, n) for char in message]

    print(f". Wiadomość zaszyfrowana (tablica liczb c):")
    print(f"   {encrypted_msg}")

    decrypted_msg_chars = [chr(pow(char_c, d, n)) for char_c in encrypted_msg]
    decrypted_msg = "".join(decrypted_msg_chars)

    print(f". Wiadomość odszyfrowana:")
    print(f"   '{decrypted_msg}'")

if __name__ == '__main__':
    RSA_Algorythm()
