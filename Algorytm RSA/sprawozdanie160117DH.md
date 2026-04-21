# Implementacja algorytmu Diffiego-Hellmana
## Ograniczenia
- Liczba $n$: Musi być liczbą pierwszą, i to bardzo dużą
- Generator $g$: Musi być pierwiastkiem pierwotnym modulo $n$. 

## Generowanie kluczy
Klucze prywatne ($x, y$): Muszą być wygenerowane za pomocą bezpiecznego generatora liczb losowych.

## Podsłuchiwanie
Atakujący, który podsłuchuje komunikację, może próbować odgadnąć klucze prywatne, ale jest to praktycznie niemożliwe przy odpowiednio dużych liczbach.
Ktoś może przechwycić X od A i wysłać do B i przechwycić Y od B i wysłać do A, podszywając się za A lub B, przez co obie osoby tak naprawdę ustaliły klucz z osobą C.

## Wnioski
D-H rozwiązuje problem bezpiecznego przekazywania klucza bez konieczności wcześniejszego spotkania stron.