import random

if __name__ == "__main__":
    n = 997
    g = 2
    print(f"Liczba pierwsza (n): {n}")
    print(f"Generator (g): {g}\n")

    x = random.randint(2, n - 2)
    X = pow(g, x, n)
    print(f"Użytkownik A wybiera losową liczbę x: {x}")
    print(f"Użytkownik A oblicza X = g^x mod n: {X}\n")

    y = random.randint(2, n - 2)
    Y = pow(g, y, n)
    print(f"Użytkownik B wybiera losową liczbę y: {y}")
    print(f"Użytkownik B oblicza Y = g^y mod n: {Y}\n")

    print("Użytkownik A i B wymieniają się wartościami X i Y.\n")
    print(f"Użytkownik A otrzymuje Y: {Y}")
    print(f"Użytkownik B otrzymuje X: {X}\n")

    k_a = pow(Y, x, n)
    k_b = pow(X, y, n)

    print(f"Klucz A: {k_a}")
    print(f"Klucz B: {k_b}")

    if k_a == k_b:
        print("\nSukces! Uzgodniono wspólny klucz sesyjny.")
    else:
        print("\nBłąd! Klucze się różnią.")