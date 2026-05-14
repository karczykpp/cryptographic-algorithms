from PIL import Image, ImageDraw
import random


def stworz_testowy_obraz():
    img = Image.new('1', (100, 100), color=1)
    draw = ImageDraw.Draw(img)

    draw.rectangle([20, 20, 80, 80], fill=0)
    draw.ellipse([35, 35, 65, 65], fill=1)

    return img

def generuj_udzialy(obraz):
    szerokosc, wysokosc = obraz.size

    udzial1 = Image.new('1', (szerokosc * 2, wysokosc))
    udzial2 = Image.new('1', (szerokosc * 2, wysokosc))

    pix_org = obraz.load()
    pix_u1 = udzial1.load()
    pix_u2 = udzial2.load()

    for y in range(wysokosc):
        for x in range(szerokosc):
            piksel = pix_org[x, y]
            los = random.choice([0, 1])

            if piksel > 0:
                if los == 0:
                    # Patern Czarny -Biały
                    pix_u1[x * 2, y] = 0;
                    pix_u1[x * 2 + 1, y] = 255
                    pix_u2[x * 2, y] = 0;
                    pix_u2[x * 2 + 1, y] = 255
                else:
                    # Patern Biały - Czarny
                    pix_u1[x * 2, y] = 255;
                    pix_u1[x * 2 + 1, y] = 0
                    pix_u2[x * 2, y] = 255;
                    pix_u2[x * 2 + 1, y] = 0
            else:
                if los == 0:
                    # Paterny na odwrot dla czarnego piksela
                    pix_u1[x * 2, y] = 0;
                    pix_u1[x * 2 + 1, y] = 255
                    pix_u2[x * 2, y] = 255;
                    pix_u2[x * 2 + 1, y] = 0
                else:
                    pix_u1[x * 2, y] = 255;
                    pix_u1[x * 2 + 1, y] = 0
                    pix_u2[x * 2, y] = 0;
                    pix_u2[x * 2 + 1, y] = 255

    return udzial1, udzial2

def zloz_udzialy(u1, u2):
    szerokosc, wysokosc = u1.size
    wynik = Image.new('1', (szerokosc, wysokosc))

    pix_w = wynik.load()
    pix_u1 = u1.load()
    pix_u2 = u2.load()

    for y in range(wysokosc):
        for x in range(szerokosc):
            pix_w[x, y] = min(pix_u1[x, y], pix_u2[x, y])

    return wynik


if __name__ == "__main__":
    print("1. Tworzenie oryginalnego obrazu 100x100")
    org = stworz_testowy_obraz()
    org.save("01_oryginal.png")

    print("2. Szyfrowanie 200x100")
    u1, u2 = generuj_udzialy(org)
    u1.save("02_udzial_1.png")
    u2.save("03_udzial_2.png")

    print("3. Składanie folii")
    zlozony = zloz_udzialy(u1, u2)
    zlozony.save("04_wynik_zlozenia.png")

    print("Gotowe! Sprawdź wygenerowane pliki w folderze z programem.")