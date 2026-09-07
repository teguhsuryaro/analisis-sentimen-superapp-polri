# Analisis Sentimen Ulasan AdaKami

Proyek ini digunakan untuk mengambil data ulasan aplikasi AdaKami dari Google Play Store sebagai dataset untuk analisis sentimen.

## Teknologi

- Python
- Pandas
- google-play-scraper

## Instalasi

Clone repository:

```bash
git clone URL_REPOSITORY
cd analisis-sentimen-adakami
```

Buat dan aktifkan virtual environment:

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Jika PowerShell menolak aktivasi script, gunakan Command Prompt:

```bat
.venv\Scripts\activate.bat
```

Pasang seluruh dependensi:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Menjalankan Scraping

Pastikan virtual environment sudah aktif, kemudian jalankan:

```bash
python scraping.py
```

Script akan mengambil ulasan AdaKami dari Google Play Store dan menyimpannya ke file `ulasan_adakami_3.csv`.
