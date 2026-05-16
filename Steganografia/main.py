from PIL import Image
import os

def tekst_na_bity(tekst):
    bity = ''.join(format(ord(znak), '08b') for znak in tekst)
    return bity + '00000000'  # zera to stop


def bity_na_tekst(bity):
    wiadomosc = ""
    for i in range(0, len(bity), 8):
        bajt = bity[i:i + 8]
        if bajt == '00000000':
            break
        wiadomosc += chr(int(bajt, 2))
    return wiadomosc

def ukryj_wiadomosc(sciezka_we, sciezka_wy, tajny_tekst):
    obraz = Image.open(sciezka_we).convert('RGB')
    piksele = obraz.load()
    szerokosc, wysokosc = obraz.size

    bity_wiadomosci = tekst_na_bity(tajny_tekst)
    indeks_bitu = 0
    dlugosc_wiadomosci = len(bity_wiadomosci)

    print(f"Osadzam: {dlugosc_wiadomosci} bitów...")

    for y in range(wysokosc):
        for x in range(szerokosc):
            if indeks_bitu < dlugosc_wiadomosci:
                r, g, b = piksele[x, y]

                if indeks_bitu < dlugosc_wiadomosci:
                    r = (r & ~1) | int(bity_wiadomosci[indeks_bitu])
                    indeks_bitu += 1

                # zielony
                if indeks_bitu < dlugosc_wiadomosci:
                    g = (g & ~1) | int(bity_wiadomosci[indeks_bitu])
                    indeks_bitu += 1

                # niebieski
                if indeks_bitu < dlugosc_wiadomosci:
                    b = (b & ~1) | int(bity_wiadomosci[indeks_bitu])
                    indeks_bitu += 1

                piksele[x, y] = (r, g, b)
            else:
                break
        if indeks_bitu >= dlugosc_wiadomosci:
            break

    # png bezstratny, jpeg kompresuje
    obraz.save(sciezka_wy, "PNG")
    print(f"Sukces! Wiadomość ukryta w pliku: {sciezka_wy}")

def odczytaj_wiadomosc(sciezka_we):
    obraz = Image.open(sciezka_we).convert('RGB')
    piksele = obraz.load()
    szerokosc, wysokosc = obraz.size

    odczytane_bity = ""

    for y in range(wysokosc):
        for x in range(szerokosc):
            r, g, b = piksele[x, y]

            odczytane_bity += str(r & 1)
            odczytane_bity += str(g & 1)
            odczytane_bity += str(b & 1)

    return bity_na_tekst(odczytane_bity)

if __name__ == "__main__":
    testowy_obraz = Image.new('RGB', (100, 100), color=(255, 100, 100))
    testowy_obraz.save("01_orginalny.png")

    tajna_wiadomosc = "To jest tajna wiadomosc od prowadzacego!"

    print("ukrywanie")
    ukryj_wiadomosc("01_orginalny.png", "02_z_ukryta_wiadomoscia.png", tajna_wiadomosc)

    print("odczytanie")
    odzyskany_tekst = odczytaj_wiadomosc("02_z_ukryta_wiadomoscia.png")
    print(f"Odzyskana wiadomość: '{odzyskany_tekst}'")