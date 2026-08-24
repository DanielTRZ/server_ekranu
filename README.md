# server_ekranu

# 🖥️ Lokalny Streamer Pulpitu / LAN Screen Streamer

Prosta i lekka aplikacja w Pythonie, która pozwala na błyskawiczne udostępnianie ekranu komputera na dowolne urządzenie w tej samej sieci lokalnej (LAN) – np. na tablet, telefon czy telewizor – za pomocą zwykłej przeglądarki internetowej.

A simple and lightweight Python application that allows you to instantly share your computer screen to any device on the same local area network (LAN) – such as a tablet, phone, or TV – using a standard web browser.

---

## 🚀 Funkcje / Features
* **Zero instalacji u odbiorcy / Zero installation on the receiver:** Nie musisz instalować żadnych aplikacji na drugim urządzeniu – wystarczy przeglądarka internetowa. / No extra apps needed on the receiving device—just a web browser.
* **Wysoka jakość obrazu / High image quality:** Wykorzystuje bibliotekę OpenCV do dynamicznego kodowania klatek w wysokiej jakości. / Uses the OpenCV library for dynamic high-quality frame encoding.
* **Wygodny Panel Sterowania / Convenient Control Panel:** Proste okienko w Tkinterze z widocznym adresem IP i przyciskiem szybkiego wyłączenia serwera. / A simple Tkinter window showing the IP address and a quick server shutdown button.
* **Wielowątkowość / Multithreading:** Działa płynnie w tle dzięki Flaskowi i wątkom (Threaded). / Runs smoothly in the background thanks to Flask and threading.

---

## 🛠️ Wymagane biblioteki / Requirements
Przed uruchomieniem skryptu upewnij się, że masz zainstalowane wymagane pakiety:  
Before running the script, make sure you have the required packages installed:

```bash

pip install flask opencv-python mss numpy


▶️ Jak uruchomić? / How to run?
Pobierz lub sklonuj repozytorium. / Download or clone the repository.

Uruchom plik źródłowy:

Run the source file:

python serwer_ekranu.py

W panelu sterowania pojawi się adres w formacie http://<TWOJE_IP>:5000.

The control panel will display an address in the format http://<YOUR_IP>:5000.

Wpisz ten adres w przeglądarce na drugim urządzeniu (np. iPadzie czy TV) podłączonym do tej samej sieci Wi-Fi.

Enter this address in the browser on another device (e.g., iPad or TV) connected to the same Wi-Fi network.

