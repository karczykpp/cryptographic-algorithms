## Implementacja i analiza trybów pracy szyfrów blokowych

# Założenia
Wszystkie testy wykonano przy pomocy biblioteki cryptography w języku Python.
Parametry:
- Rozmiar klucza: 256 bitów (32 bajty)
- Rozmiar wektora inicjującego (IV) / Nonce: 128 bitów 
- Rozmiar bloku danych: 128 bitów 

## Zadanie 1
- Tryby ECB i CTR charakteryzują się najkrótszymi czasami zarówno szyfrowania, jak i deszyfrowania. Wynika to z faktu, że oba te tryby umożliwiają pełne zrównoleglenie obliczeń.
- Tryb CBC jest znacznie wolniejszy, ponieważ wymaga sekwencyjnego przetwarzania bloków danych. Każdy blok musi być przetworzony przed rozpoczęciem szyfrowania kolejnego, co wprowadza opóźnienia.

## Zadanie 2
- ECB: Uszkodzenie 1 bitu w szyfrogramie powoduje, że cały, odpowiadający mu 16-bajtowy blok tekstu jawnego staje się nieczytelny - losowy ciąg danych. Błąd jednak nie propaguje na kolejne bloki.
- CBC: Uszkodzenie 1 bitu w szyfrogramie powoduje, że odpowiadający mu blok tekstu jawnego staje się nieczytelny, a także wpływa na kolejny blok, który również staje się nieczytelny. Błąd propaguje się więc na dwa bloki.
- OFB: błąd 1 bitu w szyfrogramie odwraca dokładnie ten sam 1 bit w tekście jawnym. Nie występuje żadna propagacja błędów na inne bloki.

## Zadanie 3
### Wnioski
- Tryb CBC jest w istocie nakładką matematyczną na tryb ECB.
- Implementacja udowodniła krytyczną rolę Wektora Inicjującego i przez to można robić XOR na pierwszym bloku wiadomości, który nie posiada swojego poprzednika.