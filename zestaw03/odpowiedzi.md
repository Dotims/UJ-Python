# Odpowiedzi do zadań 3.1 i 3.2

## 3.1

```python
x = 2; y = 3;
```
Poprawne. Średnik na końcu jest zbędny, ale dozwolony.

```python
if (x > y):
    result = x;
else:
    result = y;
```
Poprawne. Nawiasy wokół warunku i średniki są zbędne.

```python
for i in "axby": if ord(i) < 100: print (i)
```
Błąd składni (`SyntaxError`). Po dwukropku w tej samej linii mogą być tylko proste instrukcje, a `if` jest instrukcją złożoną. Trzeba przenieść `if` do nowej linii z wcięciem.

```python
for i in "axby": print (ord(i) if ord(i) < 100 else i)
```
Poprawne, bo `ord(i) if ord(i) < 100 else i` to wyrażenie, a nie instrukcja. Wypisuje `97`, `x`, `98`, `y`.

## 3.2

```python
L = [3, 5, 4] ; L = L.sort()
```
`sort()` sortuje listę w miejscu i zwraca `None`, więc `L` staje się `None`. Powinno być `L.sort()` albo `L = sorted(L)`.

```python
x, y = 1, 2, 3
```
Trzy wartości i tylko dwie zmienne: `ValueError: too many values to unpack`.

```python
X = 1, 2, 3 ; X[1] = 4
```
`X` jest krotką, a krotek nie można zmieniać: `TypeError`.

```python
X = [1, 2, 3] ; X[3] = 4
```
Lista ma indeksy 0-2, indeks 3 nie istnieje: `IndexError`. Element dodaje się przez `X.append(4)`.

```python
X = "abc" ; X.append("d")
```
Napisy nie mają metody `append` i są niezmienne: `AttributeError`. Można zrobić `X = X + "d"`.

```python
L = list(map(pow, range(8)))
```
`pow` potrzebuje dwóch argumentów, a `map` z jednym ciągiem podaje tylko jeden: `TypeError`. Np. kwadraty: `list(map(pow, range(8), [2] * 8))`.
