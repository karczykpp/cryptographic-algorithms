import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

klucz = os.urandom(32)
wektor_iv = os.urandom(16)
nonce = os.urandom(16)

print(" ZADANIE 1: Pomiary czasu")

rozmiary = {
    "1 MB": 1000000,
    "10 MB": 10000000,
    "50 MB": 50000000
}

tryby_pracy = [
    ("ECB", modes.ECB()),
    ("CBC", modes.CBC(wektor_iv)),
    ("CFB", modes.CFB(wektor_iv)),
    ("OFB", modes.OFB(wektor_iv)),
    ("CTR", modes.CTR(nonce))
]

for nazwa, bajty in rozmiary.items():
    print(f"\n--- Generowanie danych dla pliku {nazwa} ---")
    dane = os.urandom(bajty)

    for nazwa_trybu, tryb in tryby_pracy:
        c = Cipher(algorithms.AES(klucz), tryb)

        # szyfrowanie
        enc = c.encryptor()
        start = time.time()
        zaszyfrowane = enc.update(dane) + enc.finalize()
        czas_szyfrowania = time.time() - start

        # deszyfrowanie
        dec = c.decryptor()
        start = time.time()
        odszyfrowane = dec.update(zaszyfrowane) + dec.finalize()
        czas_deszyfrowania = time.time() - start

        print(f"Tryb {nazwa_trybu}: Szyfrowanie = {czas_szyfrowania:.4f}s | Deszyfrowanie = {czas_deszyfrowania:.4f}s")

print(" ZADANIE 3: Wlasna implementacja CBC za pomoca ECB")

wiadomosc = b"To jest tajna wiadomosc 32 bajty"
print("Wiadomosc jawna: ", wiadomosc)

szyfrogram = b""
poprzedni_blok = wektor_iv

for i in range(0, len(wiadomosc), 16):
    blok = wiadomosc[i:i + 16]

    po_xorze = bytearray()
    for j in range(16):
        po_xorze.append(blok[j] ^ poprzedni_blok[j])

    c = Cipher(algorithms.AES(klucz), modes.ECB())
    enc = c.encryptor()
    zaszyfrowany_blok = enc.update(bytes(po_xorze)) + enc.finalize()

    szyfrogram += zaszyfrowany_blok
    poprzedni_blok = zaszyfrowany_blok

print("Szyfrogram: ", szyfrogram.hex()[:40], "...")

odkodowana_wiadomosc = b""
poprzedni_blok = wektor_iv

for i in range(0, len(szyfrogram), 16):
    blok = szyfrogram[i:i + 16]

    c = Cipher(algorithms.AES(klucz), modes.ECB())
    dec = c.decryptor()
    odszyfrowany_blok = dec.update(blok) + dec.finalize()

    po_xorze = bytearray()
    for j in range(16):
        po_xorze.append(odszyfrowany_blok[j] ^ poprzedni_blok[j])

    odkodowana_wiadomosc += bytes(po_xorze)
    poprzedni_blok = blok

print("Odszyfrowane: ", odkodowana_wiadomosc)
