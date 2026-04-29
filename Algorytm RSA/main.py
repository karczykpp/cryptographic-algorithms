import math

def RSA_Algorythm():
    p = 45007
    q = 55001
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

    bloki_tekstu = [message[i:i + 3] for i in range(0, len(message), 3)]
    print(f"\n1. Pocięty tekst:\n   {bloki_tekstu}")

    zaszyfrowana_wiadomosc = []

    for paczka in bloki_tekstu:
        m_i = 0
        for znak in paczka:
            m_i = (m_i * 1000) + ord(znak)
        c_i = pow(m_i, e, n)
        zaszyfrowana_wiadomosc.append(c_i)

    print(f"\n2. Zaszyfrowane bloki (liczby c_i):\n   {zaszyfrowana_wiadomosc}")

    odszyfrowana_wiadomosc = ""

    for c_i in zaszyfrowana_wiadomosc:
        m_i = pow(c_i, d, n)

        odkodowany_blok = ""
        while m_i > 0:
            znak = chr(m_i % 1000)
            odkodowany_blok = znak + odkodowany_blok
            m_i = m_i // 1000

        odszyfrowana_wiadomosc += odkodowany_blok

    print(f"\n3. Odszyfrowana wiadomość:\n   '{odszyfrowana_wiadomosc}'")


if __name__ == '__main__':
    RSA_Algorythm()
