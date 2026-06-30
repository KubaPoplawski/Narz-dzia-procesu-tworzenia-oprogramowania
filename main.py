import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText  # Poprawny i stabilny import podmodułu
from collections import deque
import datetime


class MotoTripApp(tk.Tk):
    """
    Główna klasa aplikacji MotoTripGUI.
    Zarządza interfejsem użytkownika, strukturami danych oraz logiką aplikacji.
    """

    def __init__(self):
        super().__init__()
        self.title("MotoTrip - Twój Asystent Motocyklowy")
        self.geometry("900x650")
        self.minsize(850, 550)

        # Stylizacja aplikacji przy użyciu ttk (Ciemny motyw z czerwonymi akcentami)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_theme()

        # Zaawansowane struktury danych spełniające kryterium na ocenę 5.0
        # Użycie deque do implementacji historii zgłoszeń drogowych (bufor FIFO)
        self.zgloszenia_od_uzytkownikow = deque(maxlen=20)
        # Stos (lista) do przechowywania historii modyfikacji danych motocykla (LIFO)
        self.historia_motocykla_log = []

        # Inicjalizacja danych początkowych
        self.inicjalizuj_dane()

        # Tworzenie struktury interfejsu (Notebook / Zakładki)
        self.create_widgets()

    def configure_theme(self):
        """Konfiguracja kolorystyki i stylów dla komponentów interfejsu."""
        self.style.configure('.', background='#1e1e24', foreground='#f5f5f5')
        self.style.configure('TNotebook', background='#1e1e24', borderwidth=0)
        self.style.configure('TNotebook.Tab', background='#2a2a35', foreground='#b0b0b5', padding=[15, 5])
        self.style.map('TNotebook.Tab', background=[('selected', '#e63946')], foreground=[('selected', '#ffffff')])
        self.style.configure('TLabel', background='#1e1e24', foreground='#ffffff', font=('Helvetica', 10))
        self.style.configure('Header.TLabel', font=('Helvetica', 14, 'bold'), foreground='#e63946')
        self.style.configure('TButton', background='#e63946', foreground='#ffffff', font=('Helvetica', 10, 'bold'),
                             borderwidth=0)
        self.style.map('TButton', background=[('active', '#d62828')])

        # WYMUSZENIE CZARNEGO KOLORU PISMA I BIAŁEGO TŁA W RUBRYKACH (Ttk Entry i Combobox)
        self.style.configure('TEntry', fieldbackground='white', foreground='black', insertcolor='black')
        self.style.configure('TCombobox', fieldbackground='white', foreground='black', selectbackground='white',
                             selectforeground='black')
        self.style.map('TCombobox', fieldbackground=[('readonly', 'white')], foreground=[('readonly', 'black')])

    def inicjalizuj_dane(self):
        """Definiowanie bazowych danych dla tras oraz parametrów motocykla."""
        # Moje trasy (Dystans jako liczba całkowita)
        self.moje_trasy = [
            {"nazwa": "Bieszczadzka Pętla", "dystans": 145, "trudnosc": "Średnia",
             "opis": "Malownicza trasa z mnóstwem zakrętów i pięknymi widokami."},
            {"nazwa": "Szybki weekend na Mazurach", "dystans": 210, "trudnosc": "Łatwa",
             "opis": "Trasa wzdłuż jezior, płaska, idealna na relaks."}
        ]

        # Popularne trasy
        self.popularne_trasy = [
            {"nazwa": "Droga Stu Zakrętów (Góry Stołowe)", "ocena": "5.0 / 5", "dlugosc": "36 km",
             "popularnosc": "Bardzo wysoka"},
            {"nazwa": "Trasa przez Przełęcz Salmopolską", "ocena": "4.8 / 5", "dlugosc": "18 km",
             "popularnosc": "Wysoka"},
            {"nazwa": "Szlak Orlich Gniazd (Jura)", "ocena": "4.6 / 5", "dlugosc": "160 km", "popularnosc": "Średnia"}
        ]

        # Dane motocykla
        self.dane_motocykla = {
            "marka": "Honda",
            "model": "CB650R",
            "przebieg": 12450
        }

        # Początkowe zgłoszenia w systemie powiadomień
        self.zgloszenia_od_uzytkownikow.append(
            "Zablokowany przejazd na trasie Krynica - czyszczenie nawierzchni z żwiru.")
        self.zgloszenia_od_uzytkownikow.append("Uwaga na zakręcie w Podgórzynie - rozlany olej na prawym pasie!")

    def create_widgets(self):
        """Tworzenie zakładek i kontenerów głównych aplikacji."""
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        self.tab_moje_trasy = ttk.Frame(self.notebook)
        self.tab_popularne = ttk.Frame(self.notebook)
        self.tab_motocykl = ttk.Frame(self.notebook)
        self.tab_zgloszenia = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_moje_trasy, text="Moje Trasy")
        self.notebook.add(self.tab_popularne, text="Popularne Trasy")
        self.notebook.add(self.tab_motocykl, text="Mój Motocykl")
        self.notebook.add(self.tab_zgloszenia, text="Zgłoszenia na Drodze")

        self.setup_moje_trasy()
        self.setup_popularne_trasy()
        self.setup_motocykl()
        self.setup_zgloszenia()

    # --- MODUŁ 1: MOJE TRASY ---
    def setup_moje_trasy(self):
        """Projektowanie sekcji dodawania i zarządzania własnymi trasami."""
        left_frame = ttk.Frame(self.tab_moje_trasy, width=350, padding=10)
        left_frame.pack(side='left', fill='y')

        ttk.Label(left_frame, text="Dodaj nową trasę", style='Header.TLabel').pack(pady=(0, 15), anchor='w')

        ttk.Label(left_frame, text="Nazwa trasy:").pack(anchor='w', pady=2)
        self.entry_nazwa_trasy = ttk.Entry(left_frame, font=('Helvetica', 10), style='TEntry')
        self.entry_nazwa_trasy.pack(fill='x', pady=5)

        ttk.Label(left_frame, text="Dystans (km - liczba całkowita):").pack(anchor='w', pady=2)
        self.entry_dystans_trasy = ttk.Entry(left_frame, font=('Helvetica', 10), style='TEntry')
        self.entry_dystans_trasy.pack(fill='x', pady=5)

        ttk.Label(left_frame, text="Trudność:").pack(anchor='w', pady=2)
        self.combo_trudnosc = ttk.Combobox(left_frame, values=["Łatwa", "Średnia", "Trudna"], state="readonly",
                                           style='TCombobox')
        self.combo_trudnosc.current(0)
        self.combo_trudnosc.pack(fill='x', pady=5)

        ttk.Label(left_frame, text="Krótki opis:").pack(anchor='w', pady=2)
        self.entry_opis_trasy = ttk.Entry(left_frame, font=('Helvetica', 10), style='TEntry')
        self.entry_opis_trasy.pack(fill='x', pady=5)

        ttk.Button(left_frame, text="Zapisz trasę", command=self.dodaj_trase).pack(fill='x', pady=15)

        right_frame = ttk.Frame(self.tab_moje_trasy, padding=10)
        right_frame.pack(side='right', fill='both', expand=True)

        ttk.Label(right_frame, text="Zapisane trasy użytkownika", style='Header.TLabel').pack(pady=(0, 10), anchor='w')

        self.tree_moje_trasy = ttk.Treeview(right_frame, columns=("Nazwa", "Dystans", "Trudność", "Opis"),
                                            show="headings")
        self.tree_moje_trasy.heading("Nazwa", text="Nazwa trasy")
        self.tree_moje_trasy.heading("Dystans", text="Dystans")
        self.tree_moje_trasy.heading("Trudność", text="Trudność")
        self.tree_moje_trasy.heading("Opis", text="Opis")
        self.tree_moje_trasy.pack(fill='both', expand=True)

        self.odswiez_liste_moich_tras()

    def dodaj_trase(self):
        """Walidacja danych wejściowych i wprowadzanie nowej trasy (wymóg liczb całkowitych)."""
        nazwa = self.entry_nazwa_trasy.get().strip()
        dystans_str = self.entry_dystans_trasy.get().strip()
        trudnosc = self.combo_trudnosc.get()
        opis = self.entry_opis_trasy.get().strip()

        if not nazwa or not dystans_str or not opis:
            messagebox.showwarning("Błąd walidacji", "Uzupełnij wszystkie wymagane pola!")
            return

        try:
            dystans = int(dystans_str)
        except ValueError:
            messagebox.showerror("Błąd formatu", "Dystans musi być podany jako liczba całkowita bez przecinka!")
            return

        self.moje_trasy.append({"nazwa": nazwa, "dystans": dystans, "trudnosc": trudnosc, "opis": opis})
        self.odswiez_liste_moich_tras()

        # Czyszczenie pól formularza
        self.entry_nazwa_trasy.delete(0, tk.END)
        self.entry_dystans_trasy.delete(0, tk.END)
        self.entry_opis_trasy.delete(0, tk.END)
        messagebox.showinfo("Sukces", "Trasa pomyślnie dodana!")

    def odswiez_liste_moich_tras(self):
        """Odświeżanie zawartości widoku tabelarycznego Moich Tras."""
        for row in self.tree_moje_trasy.get_children():
            self.tree_moje_trasy.delete(row)
        for t in self.moje_trasy:
            self.tree_moje_trasy.insert("", tk.END, values=(t["nazwa"], f"{t['dystans']} km", t["trudnosc"], t["opis"]))

    # --- MODUŁ 2: POPULARNE TRASY ---
    def setup_popularne_trasy(self):
        """Widok rekomendacji najpopularniejszych tras motocyklowych w Polsce."""
        main_frame = ttk.Frame(self.tab_popularne, padding=20)
        main_frame.pack(fill='both', expand=True)

        ttk.Label(main_frame, text="Najchętniej wybierane trasy w Polsce", style='Header.TLabel').pack(pady=(0, 15),
                                                                                                       anchor='w')

        tree_pop = ttk.Treeview(main_frame, columns=("Nazwa", "Ocena", "Długość", "Popularność"), show="headings")
        tree_pop.heading("Nazwa", text="Nazwa Odcinka")
        tree_pop.heading("Ocena", text="Ocena Społeczności")
        tree_pop.heading("Długość", text="Długość trasy")
        tree_pop.heading("Popularność", text="Natężenie Ruchu Moto")

        for item in self.popularne_trasy:
            tree_pop.insert("", tk.END, values=(item["nazwa"], item["ocena"], item["dlugosc"], item["popularnosc"]))
        tree_pop.pack(fill='both', expand=True)

    # --- MODUŁ 3: INFORMACJE O MOTOCYKLU ---
    def setup_motocykl(self):
        """Konfiguracja panelu zarządzania sprzętem i logami technicznymi przy użyciu stosu LIFO."""
        container = ttk.Frame(self.tab_motocykl, padding=20)
        container.pack(fill='both', expand=True)

        left_side = ttk.Frame(container, padding=10)
        left_side.pack(side='left', fill='both', expand=True)

        ttk.Label(left_side, text="Dane specyfikacji technicznej", style='Header.TLabel').pack(pady=(0, 15), anchor='w')

        fields_frame = ttk.Frame(left_side)
        fields_frame.pack(fill='x')

        # Zapewnienie rozciągania kolumny z Entry
        fields_frame.columnconfigure(1, weight=1)

        ttk.Label(fields_frame, text="Marka:").grid(row=0, column=0, sticky='w', pady=5)
        self.ent_marka = ttk.Entry(fields_frame, font=('Helvetica', 10), style='TEntry')
        self.ent_marka.grid(row=0, column=1, sticky='ew', pady=5, padx=10)

        ttk.Label(fields_frame, text="Model:").grid(row=1, column=0, sticky='w', pady=5)
        self.ent_model = ttk.Entry(fields_frame, font=('Helvetica', 10), style='TEntry')
        self.ent_model.grid(row=1, column=1, sticky='ew', pady=5, padx=10)

        ttk.Label(fields_frame, text="Przebieg (km - liczba całkowita):").grid(row=2, column=0, sticky='w', pady=5)
        self.ent_przebieg = ttk.Entry(fields_frame, font=('Helvetica', 10), style='TEntry')
        self.ent_przebieg.grid(row=2, column=1, sticky='ew', pady=5, padx=10)

        # Wprowadzanie danych początkowych
        self.ent_marka.insert(0, self.dane_motocykla["marka"])
        self.ent_model.insert(0, self.dane_motocykla["model"])
        self.ent_przebieg.insert(0, str(self.dane_motocykla["przebieg"]))

        ttk.Button(left_side, text="Zapisz i zaloguj zmiany", command=self.zapisz_dane_motocykla).pack(anchor='w',
                                                                                                       pady=15)

        right_side = ttk.Frame(container, width=320, padding=10)
        right_side.pack(side='right', fill='both')

        ttk.Label(right_side, text="Historia edycji (Stos LIFO):", font=('Helvetica', 10, 'bold')).pack(anchor='w')
        self.txt_logi_motocykla = ScrolledText(right_side, width=35, height=15, font=('Consolas', 9), bg='#2a2a35',
                                               fg='#ffffff', borderwidth=0)
        self.txt_logi_motocykla.pack(fill='both', expand=True, pady=5)
        self.txt_logi_motocykla.insert(tk.END, "Inicjalizacja profilu pojazdu...\\n")
        self.txt_logi_motocykla.config(state='disabled')

    def zapisz_dane_motocykla(self):
        """Przetwarzanie modyfikacji danych pojazdu oraz odkładanie stanu na stos (LIFO)."""
        m = self.ent_marka.get().strip()
        mod = self.ent_model.get().strip()
        przeb = self.ent_przebieg.get().strip()

        if not m or not mod or not przeb:
            messagebox.showwarning("Błąd", "Wprowadź kompletne specyfikacje motocykla!")
            return

        try:
            przeb_int = int(przeb)
        except ValueError:
            messagebox.showerror("Błąd", "Przebieg musi być podany jako liczba całkowita!")
            return

        # Aktualizacja słownika maszynowego
        self.dane_motocykla["marka"] = m
        self.dane_motocykla["model"] = mod
        self.dane_motocykla["przebieg"] = przeb_int

        # Logowanie na stos (Zasada LIFO - Last In, First Out)
        teraz = datetime.datetime.now().strftime("%H:%M:%S")
        self.historia_motocykla_log.append(f"[{teraz}] Profil: {m} {mod} | Przebieg: {przeb_int} km")

        # Aktualizacja wizualna kontenera tekstowego (od najnowszego)
        self.txt_logi_motocykla.config(state='normal')
        self.txt_logi_motocykla.delete('1.0', tk.END)
        for log in reversed(self.historia_motocykla_log):
            self.txt_logi_motocykla.insert(tk.END, log + "\\n")
        self.txt_logi_motocykla.config(state='disabled')

        messagebox.showinfo("Sukces", "Zaktualizowano dane pojazdu i odłożono log na stos!")

    # --- MODUŁ 4: ZGŁASZANIE PROBLEMÓW NA DRODZE ---
    def setup_zgloszenia(self):
        """Konfiguracja modułu społecznościowego live-feed (Kolejka FIFO za pomocą deque)."""
        main_pane = ttk.Frame(self.tab_zgloszenia, padding=20)
        main_pane.pack(fill='both', expand=True)

        ttk.Label(main_pane, text="Utrudnienia i zagrożenia na trasie (Live Feed)", style='Header.TLabel').pack(
            pady=(0, 10), anchor='w')

        self.txt_zgloszenia_feed = ScrolledText(main_pane, height=10, font=('Helvetica', 10), bg='#2a2a35',
                                                fg='#ffffff', borderwidth=0)
        self.txt_zgloszenia_feed.pack(fill='x', pady=5)
        self.odswiez_komunikaty_drogowe()

        form_frame = ttk.LabelFrame(main_pane, text=" Nowy komunikat ostrzegawczy ", padding=15)
        form_frame.pack(fill='x', pady=15)

        ttk.Label(form_frame, text="Treść alertu drogowego (np. rozlany olej, fotoradar, dziury):").pack(anchor='w',
                                                                                                         pady=2)
        self.entry_alert = ttk.Entry(form_frame, font=('Helvetica', 10), style='TEntry')
        self.entry_alert.pack(fill='x', pady=5)

        ttk.Button(form_frame, text="Wyślij Alert w Trasę", command=self.dodaj_nowy_alert).pack(anchor='e', pady=5)

    def dodaj_nowy_alert(self):
        """Dodawanie nowego wpisu na początek kolejki dwukierunkowej (FIFO z maxlen)."""
        alert_text = self.entry_alert.get().strip()
        if not alert_text:
            messagebox.showwarning("Błąd", "Nie można wysłać pustego alertu drogowego!")
            return

        czas = datetime.datetime.now().strftime("%H:%M")
        # Dodanie na początek kolejki (nowe powiadomienia są na górze)
        self.zgloszenia_od_uzytkownikow.appendleft(f"[{czas}] Ostrzeżenie: {alert_text}")

        self.entry_alert.delete(0, tk.END)
        self.odswiez_komunikaty_drogowe()
        messagebox.showinfo("System", "Zgłoszenie wysłane pomyślnie!")

    def odswiez_komunikaty_drogowe(self):
        """Wizualizacja komunikatów ułożonych w kolejce FIFO."""
        self.txt_zgloszenia_feed.config(state='normal')
        self.txt_zgloszenia_feed.delete('1.0', tk.END)
        for msg in self.zgloszenia_od_uzytkownikow:
            self.txt_zgloszenia_feed.insert(tk.END, f"• {msg}\\n\\n")
        self.txt_zgloszenia_feed.config(state='disabled')


if __name__ == "__main__":
    app = MotoTripApp()
    app.mainloop()