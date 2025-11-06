# SMGP Downloader (QGIS Plugin)

**SMGP Downloader** to wtyczka do **QGIS**, umożliwiająca pobieranie wybranych polskich map geologicznych w oparciu o wskazaną lokalizację bądź numer arkusza.  
Narzędzie automatyzuje proces wyszukiwania i pobierania danych kartograficznych, zapewniając ich bezpośrednią integrację z QGIS.

---

## Funkcjonalności

- Wyszukiwanie lokalizacji i automatyczne przypisanie do odpowiedniego arkusza (10k, 50k, 200k)  
- Pobieranie map geologicznych z serwera na podstawie numeru arkusza  
- Walidacja danych wejściowych przed rozpoczęciem pobierania  
- Zarządzanie siatkami arkuszy i warstwami wektorowymi  
- Wybór katalogu zapisu wyników  
- Interfejs graficzny oparty o Qt Designer i PyQt  
- Obsługa wielu języków poprzez pliki tłumaczeń `.qm`

---



## Struktura projektu
```text
SMGP_dowloader/
│
├── __init__.py
├── SMGP_dowloader.py             # Główny plik wtyczki
├── SMGP_dowloader_dialog.py      # Klasa interfejsu użytkownika
├── resources.qrc                 # Definicja zasobów (ikony, grafiki)
├── icon.png                      # Ikona wtyczki
│
├── utils_find_point.py           # Wyszukiwanie arkusza na podstawie punktu
├── utils_validate.py             # Walidacja numeru arkusza i danych wejściowych
├── utils_download_map.py         # Logika pobierania map z serwera
├── utils_grid_manager.py         # Zarządzanie siatkami arkuszy
├── utils_gui.py                  # Obsługa interfejsu i zdarzeń GUI
├── utils_select_output.py        # Wybór katalogu zapisu
│
├── grids/                        # Siatki do pobrania
│   ├── 10k/10k_grid.shp
│   ├── 50k/50k_grid.shp
│   ├── 200k/200k_grid.shp
```
## Wymagania

- QGIS 3.22 lub nowszy  
- Python 3.9+  
- Biblioteki:
  - PyQt5  
  - qgis.core, qgis.gui  
  - osgeo.ogr (opcjonalnie, jeśli używana w siatkach)

---

## Instalacja

1. Pobierz repozytorium lub paczkę ZIP z wtyczką.  
2. Skopiuj katalog `SMGP_dowloader` do folderu z wtyczkami QGIS:
3. Włącz wtyczkę z poziomu:  **Wtyczki → Zainstalowane → SMGP Downloader**

## Licencja

Projekt udostępniany jest na licencji  
**GNU General Public License v2.0 (GPLv2)** lub nowszej.  

Szczegóły znajdują się w nagłówkach plików źródłowych.

---

## Autor

**Karol Majewski / PIG-PIB**  
majewskikar@gmail.com  
2025
