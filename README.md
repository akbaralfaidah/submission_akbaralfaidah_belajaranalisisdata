# Bike Sharing Data Analysis Dashboard by Akbar Alfaidah ✨

Proyek ini adalah analisis data untuk sistem penyewaan sepeda (Bike Sharing System) dengan menggunakan dataset yang berisi informasi tentang penyewaan sepeda berdasarkan faktor-faktor seperti cuaca, hari kerja, dan waktu.

Dashboard ini dikembangkan menggunakan **Streamlit** untuk memvisualisasikan hasil analisis dan membuat prediksi menggunakan model regresi linier.

## Setup Environment

### Menggunakan Anaconda

Jika Anda menggunakan **Anaconda** untuk manajemen lingkungan virtual, ikuti langkah-langkah berikut:
```
# Membuat environment baru:
conda create --name bike-sharing-ds python=3.10

# Mengaktifkan environment:
conda activate bike-sharing-ds

# Menginstal pustaka yang dibutuhkan:
pip install -r requirements.txt
```

### Menggunakan Shell/Terminal

Jika Anda menggunakan pipenv atau terminal biasa, ikuti langkah-langkah berikut:
```
# Membuat folder proyek dan masuk ke dalamnya:
mkdir proyek_analisis_data
cd proyek_analisis_data

# Menginstal dependensi menggunakan pipenv:
pipenv install
pipenv shell

# Menginstal pustaka-pustaka yang dibutuhkan:
pip install -r requirements.txt
```

### Menjalankan Aplikasi Streamlit
Setelah environment terpasang, Anda dapat menjalankan aplikasi Streamlit dengan perintah berikut:
```
cd dashboard
streamlit run dashboard.py
```
