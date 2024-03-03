# Proyek Analisa Data Bike Sharing Dataset

## Deskripsi

Proyek ini dimaksudkan untuk melakukan analisis terhadap data dalam Bike Sharing Dataset. Tujuan utamanya adalah untuk menghasilkan pemahaman mendalam dan informasi yang bermanfaat dari data yang telah dianalisis.

## Tahapan Proyek

1. Data Wrangling:
- Mengumpulkan data
- Menilai data
- Membersihkan data

2. Exploratory Data Analysis:
- Merumuskan pertanyaan bisnis untuk eksplorasi data
- Membuat eksplorasi data

3. Data Visualization:
- Membuat visualisasi data yang menjawab pertanyaan bisnis

4. Dashboard:
- Menyiapkan DataFrame yang akan digunakan
- Membuat komponen filter pada dashboard
- Menyusun dashboard dengan berbagai visualisasi data

## Struktur Direktori

- **/data**: Berisi data yang digunakan dalam proyek, disimpan dalam format .csv.
- **/dashboard**: Memuat file main.py yang bertanggung jawab untuk membuat dashboard berdasarkan hasil analisis data.
- **notebook.ipynb**: File ini digunakan untuk melakukan analisis data.
- **url.txt**: Berisi link ke deployment Deployment pada  **Streamlit** <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit logo"></img>

## Preview Dashboard
![Dashboard Streamlit Preview](https://raw.githubusercontent.com/mhmmadgiatt/Proyek-analisis-data-bike-sharing/preview.jpg)

## Instalasi

1. Clone repository ini ke komputer lokal Anda menggunakan perintah berikut:

   ```shell
   git clone https://github.com/mhmmadgiatt/Proyek-analisis-data-bike-sharing.git
   ```

2. Pastikan Anda memiliki lingkungan Python yang sesuai dan library yang diperlukan. Anda dapat menginstal pustaka-pustaka tersebut dengan menjalankan perintah berikut:

    ```shell
    pip install -r requirements.txt
    pip install streamlit
   
    ```

## Penggunaan Dashboard
1. Masuk ke direktori proyek Local

    ```shell
    cd dashboard/
    streamlit run dashboard.py
    ```
2. Atau bisa dengan kunjungi website ini [Proyek Bike Sharing Streamlit](https://dashboardpy-cd78pgyaiexdde4esezvh6.streamlit.app/)
