## Implementacja algorytmu RSA

#  Cel ćwiczenia

Celem ćwiczenia było zapoznanie się z algorytmem RSA oraz jego praktycznym zastosowaniem w publicznym systemie kryptograficznym. Zadanie polegało na implementacji szyfrowania i deszyfrowania wiadomości przy użyciu wygenerowanych kluczy.

##  Założenia

W programie wykorzystano liczby pierwsze czterocyfrowe:
- p = 1249  
- q = 9967

W rzeczywistych zastosowaniach algorytmu RSA stosuje się liczby znacznie większe - co najmniej 1024 bity, ale dla celów ćwiczenia użyto mniejszych liczb, aby ułatwić obliczenia.

##  Generowanie kluczy

### Obliczenia:

- n = p · q = 1249 · 9967 = 12 448 783  
- φ(n) = (p − 1)(q − 1) = 1248 · 9966 = 12 437 568

### Wyznaczenie e:

Wartość e została wyznaczona jako najmniejsza liczba względnie pierwsza z φ(n):

- e = 5 

### Wyznaczenie d:

Wartość d została obliczona jako odwrotność modularna:

- d ≡ e⁻¹ mod φ(n)  
- d = 7 462 541

### Klucze:

- Klucz publiczny: (e, n) = (5, 12 448 783)  
- Klucz prywatny: (d, n) = (7 462 541, 12 448 783)  

##  Wiadomość

Wiadomość użyta w programie:
- Nazywam się Jakub Karcz i studuję informatykę na Politechnice Poznańskiej.

##  Szyfrowanie

Każdy znak wiadomości został zamieniony na kod ASCII, a następnie zaszyfrowany według wzoru:
- C = M^e mod n

Wynikiem jest tablica liczb całkowitych reprezentujących zaszyfrowaną wiadomość.

##  Deszyfrowanie

Deszyfrowanie odbywa się według wzoru:
- m = c^d mod n

## Odpowiedzi na pytania

### 1. Jakie elementy algorytmu są trudne w realizacji?

Najtrudniejsze elementy to:

- generowanie dużych liczb pierwszych
- obliczanie odwrotności modularnej (d)
- zapewnienie, że e i φ(n) są względnie pierwsze
- wydajne operacje potęgowania modulo dla dużych liczb

---

### 2. Co stanowi o bezpieczeństwie algorytmu RSA?

Bezpieczeństwo RSA opiera się na:

- trudności faktoryzacji liczby n na czynniki pierwsze p i q
- użyciu bardzo dużych liczb pierwszych
- poprawnym doborze parametrów (e, d)
- tajności klucza prywatnego

---

##  Wnioski

- Algorytm RSA jest skuteczną metodą szyfrowania asymetrycznego.
- Bezpieczeństwo systemu zależy głównie od wielkości użytych liczb pierwszych.

---