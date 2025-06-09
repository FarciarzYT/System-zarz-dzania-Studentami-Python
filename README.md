Student Manager CLI App 🎓

📖 Opis
To prosty projekt konsolowej aplikacji do zarządzania studentami, napisany w Pythonie z wykorzystaniem programowania obiektowego (OOP). Umożliwia:

- Dodawanie studentów
- Usuwanie studentów
- Wyświetlanie wszystkich studentów (z sortowaniem po średniej)
- Wyświetlanie najlepszego studenta
- Modyfikację danych studentów
- Zapis i odczyt danych do/z pliku JSON

📂 Struktura katalogów
```
project/
│
├── main.py
├── models/
│   ├── Student.py
│   └── StudentManager.py
├── cli/
│   └── cli.py
├── utils/
│   └── helper.py
├── data/
│   └──studentdata.json
├──  README.md
└──  requriments.txt
```
🚀 Uruchomienie

Upewnij się, że masz zainstalowanego Pythona 3. Następnie:

python main.py

📦 Funkcje

- ✅ OOP – klasy Student, StudentManager
- 📊 Obliczanie średniej ocen
- 📈 Sortowanie po średniej
- 💾 Zapis/odczyt do pliku JSON
- 🎛️ CLI menu
- 🚫 Obsługa błędów (try/except)

🛠️ Przykład dodawania studenta

Student name: Farciarz
Student surname: Turbo
Student group: A
Student grades: 5,4,6
Student presence: 92

🔮 Planowane funkcje (do przyszłego rozwoju)

- GUI (np. z Tkinter lub PyQT)
- Walidacja unikalności ID
- Eksport do CSV
- Historia zmian
- Statystyki grupowe
- Cofanie Zmian
- user-friendly edycja Studentów
- Rozbudować Projekt o zarządzanie nauczycielami,klasami,itd.
- Zamontować baze danych PostgreSQL
- Logowanie jako Dyrektor,nauczyciel,student(aby sprawdzić swoje oceny oraz zobaczyć jak wypada się na tle klasy)
- Dodanie materiałów naukowych dla każdej klasy 





🧠 zamrożenia projektu na czas nieokreślony 