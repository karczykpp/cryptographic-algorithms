import numpy
import scipy
from sympy import primerange
import random
import math
from cryptography.hazmat.primitives.asymmetric import rsa

def print_hi(name):
    while True:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        numbers = private_key.private_numbers()

        p = numbers.p
        q = numbers.q

        if p % 4 == 3 and q % 4 == 3:
            break
    print(f"Liczba pierwsza p: {p%4},{p}")
    print(f"Liczba pierwsza q: {q}")
    N = p * q
    print(N)

    while True:
        X = random.randrange(2, N)

        if math.gcd(X, N) == 1:
            break

    bits = []
    x = (X*X) % N
    for i in range(20000):
        x = (x*x) % N
        bits.append(x % 2)

    print("Testy:")
    bity_1 = bits.count(1)
    seria1_1 = 0
    seria1_0 = 0
    seria2_1 = 0
    seria2_0 = 0
    seria3_1 = 0
    seria3_0 = 0
    seria4_1 = 0
    seria4_0 = 0
    seria5_1 = 0
    seria5_0 = 0
    seria6_1 = 0
    seria6_0 = 0
    i = 0
    maxDlugosc = 0
    while i < len(bits):
        bit = bits[i]
        dlugosc = 1
        j = i+1
        while j < len(bits) and bits[j] == bit:
            dlugosc += 1
            j+=1

        i+=dlugosc
        if dlugosc > maxDlugosc:
            maxDlugosc = dlugosc
        if dlugosc > 25:
            print("❌ Test długiej serii NIEZDANY")
        elif dlugosc == 1 and bit == 1:
            seria1_1 += 1
        elif dlugosc == 1 and bit == 0:
            seria1_0 += 1
        elif dlugosc == 2 and bit == 1:
            seria2_1 += 1
        elif dlugosc == 2 and bit == 0:
            seria2_0 += 1
        elif dlugosc == 3 and bit == 1:
            seria3_1 += 1
        elif dlugosc == 3 and bit == 0:
            seria3_0 += 1
        elif dlugosc == 4 and bit == 1:
            seria4_1 += 1
        elif dlugosc == 4 and bit == 0:
            seria4_0 += 1
        elif dlugosc == 5 and bit == 1:
            seria5_1 += 1
        elif dlugosc == 5 and bit == 0:
            seria5_0 += 1
        elif dlugosc >= 6 and bit == 1:
            seria6_1 += 1
        elif dlugosc >= 6 and bit == 0:
            seria6_0 += 1


    print(f"Liczba bitów 1: {bity_1}, liczba bitów 0: {len(bits) - bity_1}")
    print(f"Seria 1: 1 - {seria1_1}, 0 - {seria1_0}")
    print(f"Seria 2: 1 - {seria2_1}, 0 - {seria2_0}")
    print(f"Seria 3: 1 - {seria3_1}, 0 - {seria3_0}")
    print(f"Seria 4: 1 - {seria4_1}, 0 - {seria4_0}")
    print(f"Seria 5: 1 - {seria5_1}, 0 - {seria5_0}")
    print(f"Seria 6: 1 - {seria6_1}, 0 - {seria6_0}")

    print("Test pokerowy")
    i = 0
    segmenty = []
    while i < len(bits) - 4:
        segment = bits[i:i+4]
        segmenty.append(segment)
        i+=4
    segmenty_0000 = segmenty.count([0,0,0,0])
    segmenty_0001 = segmenty.count([0,0,0,1])
    segmenty_0010 = segmenty.count([0,0,1,0])
    segmenty_0011 = segmenty.count([0,0,1,1])
    segmenty_0100 = segmenty.count([0,1,0,0])
    segmenty_0101 = segmenty.count([0,1,0,1])
    segmenty_0110 = segmenty.count([0,1,1,0])
    segmenty_0111 = segmenty.count([0,1,1,1])
    segmenty_1000 = segmenty.count([1,0,0,0])
    segmenty_1001 = segmenty.count([1,0,0,1])
    segmenty_1010 = segmenty.count([1,0,1,0])
    segmenty_1011 = segmenty.count([1,0,1,1])
    segmenty_1100 = segmenty.count([1,1,0,0])
    segmenty_1101 = segmenty.count([1,1,0,1])
    segmenty_1110 = segmenty.count([1,1,1,0])
    segmenty_1111 = segmenty.count([1,1,1,1])

    poker = 16 / 5000 * (segmenty_0000**2 + segmenty_0001**2 + segmenty_0010**2 + segmenty_0011**2 + segmenty_0100**2 + segmenty_0101**2 + segmenty_0110**2 + segmenty_0111**2 + segmenty_1000**2 + segmenty_1001**2 + segmenty_1010**2 + segmenty_1011**2 + segmenty_1100**2 + segmenty_1101**2 + segmenty_1110**2 + segmenty_1111**2) - 5000
    print(f"Wartość testu pokerowego: {poker}")

    if 2315 <= seria1_1 <= 2685 and 2315 <= seria1_0 <= 2685 and 1114 <= seria2_1 <= 1386 and 1114 <= seria2_0 <= 1386 and 527 <= seria3_1 <= 723 and 527 <= seria3_0 <= 723 and 240 <= seria4_1 <= 384 and 240 <= seria4_0 <= 384 and 103 <= seria5_1 <= 209 and 103 <= seria5_0 <= 209 and 103 <= seria6_1 <= 209 and 103 <= seria6_0 <= 209:
        print("✔ Test serii OK")

    if maxDlugosc <= 26:
        print("✔ Test długiej serii OK")

    if 9725 <= bity_1 <= 10275:
        print("✔ Test pojedynczych bitów OK")
    else:
        print("❌ Test pojedynczych bitów NIEZDANY")

    if 2.16 < poker < 46.17:
        print("✔ Test pokerowy OK")
    else:
        print("❌ Test pokerowy NIEZDANY")







if __name__ == '__main__':
    print_hi('PyCharm')

