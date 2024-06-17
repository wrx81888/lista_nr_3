# Automatyzacja testów API z wykorzystaniem curl

## Opis
1. Skrypt `plik.py` automatyzuje testowanie endpointów API przy użyciu curl. Wysyła żądania HTTP GET do wybranej publicznej API, sprawdza status odpowiedzi HTTP i parsuje odpowiedzi JSON w celu weryfikacji obecności kluczowych elementów.
2. Prosta aplikajca `app.py` z funkcją dodawania dwóch liczb.
3. Testy jednostkowe dla aplikacji w pliku `app_test.py`
4. Plik MAkefile, który automatyzuje intalację zależności, uruchamianie testów oraz aplikacji.


## Wymagania
- Python 3
- curl

## Instalacja
1. Upewnij się, że masz zainstalowanego Pythona 3.
2. Upewnij się, że masz zainstalowanego curl.
3. Pobierz lub sklonuj repozytorium z plikiem `plik.py`, `app.py`, `app_test.py`, `Makefile`.


## Użycie
1. Otwórz terminal.
2. Przejdź do katalogu z plikiem `plik.py`.
3. Uruchom skrypt za pomocą polecenia:
    ```sh
    python plik.py
    ```

## Testowane Endpointy
Skrypt testuje następujące endpointy z JSONPlaceholder:
1. GET /posts/1 - sprawdza obecność kluczy: `userId`, `id`, `title`, `body`.
2. GET /comments/1 - sprawdza obecność kluczy: `postId`, `id`, `name`, `email`, `body`.
3. GET /users/1 - sprawdza obecność kluczy: `id`, `name`, `username`, `email`.

## Wyniki
Wyniki testów są wyświetlane w terminalu w formie:
Test 1: PASSED
Test 2: PASSED
Test 3: FAILED

### Instalacja zależności
```sh
make install
make test
make run
make api-test```
