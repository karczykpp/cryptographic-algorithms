import hashlib
import time
import string
import random

def zadanie_1():
    print("--- ZADANIE 1: GENERATOR SKRÓTÓW ---")
    tekst = input("Wpisz słowo do wygenerowania skrótów: ")
    bajty = tekst.encode('utf-8')

    print(f"\nHashe dla słowa '{tekst}':\n")

    print("MD5:")
    print(hashlib.md5(bajty).hexdigest())

    print("\nSHA-1:")
    print(hashlib.sha1(bajty).hexdigest())

    print("\nSHA-2 (224):")
    print(hashlib.sha224(bajty).hexdigest())

    print("\nSHA-2 (256):")
    print(hashlib.sha256(bajty).hexdigest())

    print("\nSHA-2 (384):")
    print(hashlib.sha384(bajty).hexdigest())

    print("\nSHA-2 (512):")
    print(hashlib.sha512(bajty).hexdigest())

    print("\nSHA-3 (256):")
    print(hashlib.sha3_256(bajty).hexdigest())

    print("\nSHA-3 (512):")
    print(hashlib.sha3_512(bajty).hexdigest())

def zadanie_2():
    krotki_tekst = "Kot".encode('utf-8')
    dlugi_tekst = ("Kot " * 10000).encode('utf-8')

    algorytmy = ['md5', 'sha1', 'sha256', 'sha512']
    powtorzenia = 100000
    print("--- ZADANIE 2: TEST SZYBKOŚCI ---")
    for algorytm in algorytmy:
        print(f"\nAlgorytm: {algorytm.upper()}")
        start = time.time()
        for _ in range(powtorzenia):
            hashlib.new(algorytm, krotki_tekst).hexdigest()
        end = time.time()
        print(f"Czas dla krótkiego tekstu: {end - start:.4f} sekund")

        start = time.time()
        for _ in range(powtorzenia):
            hashlib.new(algorytm, dlugi_tekst).hexdigest()
        end = time.time()
        print(f"Czas dla długiego tekstu: {end - start:.4f} sekund")


def zadanie_3():
    print("\n--- ZADANIE 3: BEZPIECZEŃSTWO KRÓTKICH HASEŁ ---")

    haslo = input("Wpisz krótkie hasło: ")

    skrot_md5 = hashlib.sha256(haslo.encode('utf-8')).hexdigest()

    print(f"\nTwój wygenerowany skrót MD5 to: {skrot_md5}")


def zadanie_5():
    print("\n--- ZADANIE 5: SZUKANIE KOLIZJI ---")

    widziane_skroty = {}
    proby = 0

    while True:
        proby += 1
        testowe_slowo = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        pelny_hash = hashlib.sha256(testowe_slowo.encode()).hexdigest()
        prefiks = pelny_hash[:10]

        if prefiks in widziane_skroty:
            print(f"ZNALAZŁEM KOLIZJĘ po {proby} próbach!")
            print(f"Słowo A: '{widziane_skroty[prefiks]}' -> Hash: {prefiks}...")
            print(f"Słowo B: '{testowe_slowo}' -> Hash: {prefiks}...")
            break
        else:
            widziane_skroty[prefiks] = testowe_slowo


def zadanie_6():
    print("\n--- ZADANIE 6: EFEKT LAWINY ---")

    s1 = "kuba"
    s2 = "kubb"

    h1 = hashlib.sha256(s1.encode()).hexdigest()
    h2 = hashlib.sha256(s2.encode()).hexdigest()

    b1 = bin(int(h1, 16))[2:].zfill(256)
    b2 = bin(int(h2, 16))[2:].zfill(256)

    roznice = 0
    for i in range(256):
        if b1[i] != b2[i]:
            roznice += 1

    procent = (roznice / 256) * 100

    print(f"Słowo 1: '{s1}' -> Hash: {h1[:30]}...")
    print(f"Słowo 2: '{s2}' -> Hash: {h2[:30]}...")
    print(f"\nLiczba zmienionych bitów: {roznice} na 256")
    print(f"Procentowa zmiana: {procent:.2f}%")

    if 45 <= procent <= 55:
        print("Wniosek: Efekt lawiny zachodzi (wynik bliski 50%).")
    else:
        print("Wniosek: Słaby efekt lawiny.")

if __name__ == "__main__":
    #zadanie_1()
    #zadanie_2()
    #zadanie_3()
    #zadanie_5()
    zadanie_6()