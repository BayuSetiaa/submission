# Dashboard E-Commerce

## Fitur

- **Analisis Retensi Pelanggan**: Menyediakan wawasan tentang faktor-faktor yang mempengaruhi retensi pelanggan, termasuk pelanggan berulang, skor ulasan rata-rata, dan metode pembayaran yang disukai.
- **Tren Penjualan Bulanan**: Menampilkan tren volume penjualan dari waktu ke waktu, membantu mengidentifikasi musiman dan periode puncak.
- **Produk Terlaris**: Memvisualisasikan kategori produk paling populer, membantu dalam manajemen inventaris dan strategi pemasaran.

## Struktur File

```plaintext
submission/
│
├── dashboard/
│   ├── dashboard.py                   # Skrip utama untuk menjalankan dashboard Streamlit
│   ├── main_data.csv                  # Dataset gabungan yang digunakan oleh dashboard
│
├── data/
│   ├── E-Commerce Public Dataset/
│   │   ├── customers_dataset.csv
│   │   ├── geolocation_dataset.csv
│   │   ├── order_items_dataset.csv
│   │   ├── order_payments_dataset.csv
│   │   ├── order_reviews_dataset.csv
│   │   ├── orders_dataset.csv
│   │   ├── product_category_name_translation.csv
│   │   ├── products_dataset.csv
│   │   ├── sellers_dataset.csv
│
├── env/                               # (Opsional) Folder lingkungan virtual
├── notebook.ipynb                     # Jupyter notebook untuk analisis data eksploratif
├── README.md                          # File dokumentasi
├── requirements.txt                   # Daftar dependensi
└── url.txt                            # URL penting untuk referensi
```

## Memulai

### Instalasi

1. **Kloning Repository:**

   ```bash
   git clone https://github.com/BayuSetiaa/submission.git
   cd submission
   ```

2. **Siapkan Lingkungan Virtual (Opsional tapi Direkomendasikan):**

   ```bash
   python3 -m venv env
   source env/bin/activate   # Di macOS/Linux
   env\Scripts\activate      # Di Windows
   ```

3. **Instal Paket yang Dibutuhkan:**

   ```bash
   pip install -r requirements.txt
   ```

### Menjalankan Dashboard

Untuk menjalankan dashboard Streamlit, gunakan perintah berikut:

```bash
streamlit run dashboard/dashboard.py
```

Perintah ini akan membuka tab baru di browser web default Anda dengan dashboard interaktif.

## Penggunaan

- **Analisis Retensi Pelanggan**: Navigasikan ke bagian ini untuk melihat wawasan tentang pelanggan berulang, faktor-faktor yang mempengaruhi retensi, dan korelasi antara ulasan dan perilaku pelanggan.
- **Tren Penjualan Bulanan**: Lihat tren volume penjualan pada basis bulanan.
- **Produk Terlaris**: Jelajahi kategori produk terlaris berdasarkan data penjualan.

## Dataset

Dataset yang digunakan dalam proyek ini tersedia secara publik dan dapat ditemukan di direktori `data/E-Commerce Public Dataset`. Ini termasuk:

- **`customers_dataset.csv`**: Informasi tentang pelanggan, termasuk ID dan lokasi mereka.
- **`order_items_dataset.csv`**: Detail item yang dipesan, termasuk ID produk, harga, dan biaya pengiriman.
- **`order_payments_dataset.csv`**: Informasi tentang pembayaran yang dilakukan oleh pelanggan, termasuk metode pembayaran.
- **`order_reviews_dataset.csv`**: Ulasan yang diberikan oleh pelanggan untuk pesanan mereka.
- **`orders_dataset.csv`**: Detail tentang setiap pesanan, termasuk ID pesanan, ID pelanggan, dan status pesanan.
- **`products_dataset.csv`**: Informasi tentang produk yang tersedia di platform.
