# Funkcje skrótu – właściwości i implementacja

## Omówienie sposobu implementacji
Użyto wbudowanej biblioteki hashlib, która zawiera zbiór algorytmów takich jak: MD5, SHA-1, SHA-2, SHA-3.

Do znalezenia kolizji 12-bitowej napisano pętle, która losowała ciągi znaków i sprawdzała pierwsze 3 znaki szesnastkowe ich skrótu w poszukiwaniu duplikatów.

Aby zbadać własność SAC, skróty szesnastkowe zamieniono na postać binarną i zliczono zmienione bity

## Rola soli i bezpieczeństwo krótkich haseł
Większość krótkich słów jest powszechnie znana i znajduje się w słownikach, które atakujący mogą łatwo wykorzystać do odgadnięcia hasła. Dodanie soli (losowego ciągu znaków) do hasła przed jego skróceniem sprawia, że nawet te same hasła będą miały różne skróty, co znacząco utrudnia ataki słownikowe i tęczowe.


## Czy funkcja MD5 jest bezpieczna
Funkcja MD5 jest uważana za niebezpieczną do zastosowań kryptograficznych, ponieważ istnieją znane metody znajdowania kolizji (różne dane dają ten sam skrót). Dlatego nie jest zalecana do zabezpieczania haseł czy innych danych wrażliwych. Zamiast tego, lepiej używać bardziej bezpiecznych funkcji skrótu, takich jak SHA-256 lub bcrypt.

## Efekt lawinowy
Zbadano zmiane jednego słowa, Kot zmieniono na Kou i po przeliczeniu skrótów okazało się, że różniły się one w 12 bitach, co potwierdza efekt lawinowy, czyli niewielka zmiana danych wejściowych prowadzi do znacznej zmiany skrótu.
