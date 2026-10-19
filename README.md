# Google Play Store Review Scraper

Alat sederhana untuk mengunduh ulasan aplikasi dari Google Play Store ke CSV. Contoh bawaan menggunakan Superapp Polri. Notebook analisis sentimen tersedia di `notebooks/` sebagai contoh lanjutan.

## Persiapan

Clone repository, lalu masuk ke folder proyek:

```bash
git clone <URL_REPOSITORY>
cd analisis-sentimen-superapp-polri
```

Buat dan aktifkan virtual environment (Python 3.10 atau lebih baru):

```powershell
# Windows PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

## Mengambil ulasan

Pasang dependensi scraper dan jalankan dengan aplikasi contoh:

```bash
python -m pip install -r requirements.txt
python scraping.py
```

Hasil default tersimpan sebagai `data/ulasan_superapp_polri.csv`. Parameter dapat diubah, misalnya:

```bash
python scraping.py --app-id com.example.app --language id --country id --count 1000 --output data/ulasan.csv
```

Gunakan ID aplikasi dari bagian `id` pada URL Google Play Store. CSV memakai delimiter titik koma (`;`) dan encoding UTF-8 dengan BOM. Jumlah ulasan yang benar-benar tersedia dapat lebih sedikit dari nilai `--count`.

## Menjalankan notebook analisis

Notebook membaca CSV hasil scraper. Pasang dependensi tambahannya di environment yang sama:

```bash
python -m pip install -r requirements-analysis.txt
jupyter notebook
```

Buka `notebooks/analisis_sentimen_superapp_polri.ipynb` dan pilih kernel dari `.venv`. Notebook akan mencari CSV default di `data/`; bila memakai nama/lokasi lain, ubah jalur pada sel **Baca CSV**. Untuk Jupyter lokal tidak perlu unggah berkas lewat `google.colab`.

Untuk memakai Google Colab, unggah CSV ke sesi Colab lalu ubah jalur pada sel **Baca CSV** sesuai nama berkas.

Data hasil scraping, environment virtual, dan cache Python tidak disimpan di Git.
