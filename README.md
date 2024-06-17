# Automatyzacja testów API z wykorzystaniem curl

## Opis
Skrypt automatyzuje testowanie endpointów API przy użyciu curl. Wysyła żądania HTTP GET do wybranej publicznej API, sprawdza status odpowiedzi HTTP i parsuje odpowiedzi JSON w celu weryfikacji obecności kluczowych elementów.

## Wymagania
- Python 3
- curl

## Instalacja
1. Upewnij się, że masz zainstalowanego Pythona 3.
2. Upewnij się, że masz zainstalowanego curl.
3. Pobierz lub sklonuj repozytorium z plikiem `api_test.py`.

## Użycie
1. Otwórz terminal.
2. Przejdź do katalogu z plikiem `api_test.py`.
3. Uruchom skrypt za pomocą polecenia:
    ```sh
    python api_test.py
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

