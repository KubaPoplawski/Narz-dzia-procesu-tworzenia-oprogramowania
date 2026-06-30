# Narz-dzia-procesu-tworzenia-oprogramowania


# MotoTrip - Twój Asystent Motocyklowy 

**MotoTrip** to desktopowa aplikacja napisana w języku Python z użyciem biblioteki **Tkinter (ttk)**. Aplikacja służy jako interaktywny asystent motocyklisty, umożliwiając planowanie tras, śledzenie stanu technicznego pojazdu oraz odbieranie i wysyłanie ostrzeżeń drogowych w czasie rzeczywistym.

Projekt został zaprojektowany z myślą o czytelności, nowoczesnym ciemnym motywem wizualnym (Dark Theme) oraz demonstracji praktycznego zastosowania struktury danych.

##  Główne Funkcje i Moduły

Aplikacja jest podzielona na 4 główne moduły dostępne w wygodnym widoku kart (Notebook):

1. **Moje Trasy** – Personalny menedżer tras użytkownika. Pozwala na dodawanie nazw, dystansów, poziomów trudności oraz opisów tras wraz z pełną walidacją danych (wymagany dystans jako liczba całkowita).
2. **Popularne Trasy** – Wbudowana baza rekomendowanych, kultowych odcinków motocyklowych w Polsce (np. *Droga Stu Zakrętów*) wraz z ocenami i oceną natężenia ruchu.
3. **Mój Motocykl** – Panel specyfikacji technicznej pojazdu (Marka, Model, Przebieg). Zmiany w profilu są logowane historycznie.
4. **Zgłoszenia na Drodze (Live Feed)** – System ostrzeżeń społecznościowych o utrudnieniach (olej na drodze, żwir, zablokowane przejazdy).


##  Zastosowane Struktury Danych

W kodzie zaimplementowano i zaprezentowano działanie kluczowych struktur danych:

* **Kolejka FIFO (First-In, First-Out) z ograniczeniem (`collections.deque`):**
    Wykorzystana w module **Zgłoszenia na Drodze**. Nowe alerty trafiają na początek kolejki, a system przechowuje maksymalnie 20 najświeższych komunikatów (`maxlen=20`), automatycznie usuwając najstarsze, gdy limit zostanie przekroczony.
* **Stos LIFO (Last-In, First-Out) za pomocą listy (`list`):**
    Zastosowany w **Historii edycji motocykla**. Każda zmiana specyfikacji jest odkładana na wierzchołek stosu (`append()`). Wyświetlanie logów w odwróconej kolejności (`reversed()`) sprawia, że użytkownik zawsze widzi najnowsze operacje na samej górze.
* **Tablice asocjacyjne / Słowniki (`dict`) oraz Listy (`list`):**
    Użyte do przechowywania parametrów motocykla oraz dynamicznych list obiektów tras.


##  Wymagania i Instalacja

Aplikacja korzysta wyłącznie z **biblioteki standardowej Pythona**, co oznacza, że nie musisz instalować żadnych dodatkowych pakietów zewnętrznych (takich jak `pip`).

### Wymagania:
* Python w wersji 3.x lub nowszej.

### Uruchomienie aplikacji:
1. Skopiuj plik z kodem źródłowym (np. `moto_trip_app.py`) do wybranego folderu.
2. Otwórz terminal / wiersz poleceń w tym folderze.
3. Uruchom program poleceniem:

Dane Autora
Autor: Popławski Kuba

Indeks: 13153

GitHub: @KubaPoplawski

Kontakt: kubapoplawski18@gmail.com

Projekt stworzony w ramach przedmiotu: Narzędzia procesu tworzenia oprogramowania

```bash
python moto_trip_app.py


