import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Dashboard Penyewaan Sepeda")

# Load Data
data_gabungan = pd.read_csv('main_data.csv')

# Visualisasi Rata-rata Jumlah Penyewaan Sepeda pada Jam Sibuk
st.header("Rata-rata Jumlah Penyewaan Sepeda pada Jam Sibuk Setiap Hari")

# Identifikasi jam sibuk terlebih dahulu
peak_hours = data_gabungan.groupby('hr')['cnt_hour'].mean().sort_values(ascending=False).head(3).index

# Menghitung rata-rata penyewaan harian pada jam sibuk
peak_hour_rentals = data_gabungan[data_gabungan['hr'].isin(peak_hours)].groupby('weekday_day')['cnt_hour'].mean()
peak_hour_rentals = peak_hour_rentals.round()

# Membuat visualisasi
fig, ax = plt.subplots(figsize=(10, 6))
peak_hour_rentals.plot(kind='bar', ax=ax)
ax.set_title("Rata-rata Jumlah Penyewaan Sepeda pada Jam Sibuk Setiap Hari (Dibulatkan)")
ax.set_xlabel("Hari dalam Seminggu")
ax.set_ylabel("Rata-rata Jumlah Penyewaan")
ax.set_xticks(range(7))
ax.set_xticklabels(['Min', 'Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sabtu'])
ax.tick_params(axis='x', rotation=0)

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Visualisasi Pengaruh Kondisi Cuaca Terhadap Jumlah Sewa Sepeda pada Hari Kerja dan Akhir Pekan
st.header("Pengaruh Kondisi Cuaca Terhadap Jumlah Sewa Sepeda pada Hari Kerja dan Akhir Pekan")

# Pilihan kondisi cuaca
weather_options = {1: "Cerah", 2: "Berawan", 3: "Hujan"}
selected_weather = st.selectbox("Pilih Kondisi Cuaca", list(weather_options.values()))

# Mengonversi input user ke bentuk numerik yang sesuai dengan dataset
weather_mapping = {v: k for k, v in weather_options.items()}
selected_weather_num = weather_mapping[selected_weather]

# Filter data berdasarkan kondisi cuaca yang dipilih
filtered_data = data_gabungan[data_gabungan['weathersit_day'] == selected_weather_num]
kerja_cuaca_data = filtered_data.groupby(['workingday_day'])['cnt_hour'].mean()

# Visualisasi
fig, ax = plt.subplots(figsize=(10, 6))
kerja_cuaca_data.plot(kind='bar', ax=ax, color=['blue', 'gray'])
ax.set_title(f'Pengaruh {selected_weather} Terhadap Jumlah Sewa Sepeda pada Hari Kerja dan Akhir Pekan')
ax.set_xlabel('Kategori Hari')
ax.set_ylabel('Rata-rata Jumlah Sewa')
ax.set_xticks(range(2))
ax.set_xticklabels(['Akhir Pekan', 'Hari Kerja'])
ax.tick_params(axis='x', rotation=0)

# Menampilkan plot di Streamlit
st.pyplot(fig)