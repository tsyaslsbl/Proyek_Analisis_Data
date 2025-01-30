import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Dashboard Penyewaan Sepeda")

#Upload dataset
upload_file = st.file_uploader ("Upload dataset disini", type=["csv"])

if upload_file:
    df = pd.read_csv(upload_file)

    #Menampilkan DataFrame
    st.subheader("Data Penyewaan Sepeda")
    st.write(df)

    #Grafik Penyewaan Sepeda per Hari
    st.subheader("Grafik Penyewaan Sepeda per Hari")

    if 'dteday' in df.columns and 'cnt_day' in df.columns:
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(x=df['dteday'], y=df['cnt_day'], ax=ax)
        ax.set_ylabel("Total Penyewaan Sepeda")
        ax.set_xlabel("Tanggal")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.error("Kolom 'dteday' atau 'cnt_day' tidak ditemukan dalam dataset.")
    
    #Grafik Penyewaan Sepeda pada tahun 2011
    # Buat dataset baru khusus di tahun 2011
    df["dteday"] = pd.to_datetime(df['dteday'])
    data_2011 = df[df['dteday'].dt.year == 2011]

    # Dari dataset 2011, kita buatkan grouping data month dan cnt (penyewaan) agar memudahkan menghitung rata-rata
    data_bulanan_2011 = data_2011.groupby('mnth_day')['cnt_day'].sum().reset_index()

    #Grafik Penyewaan Sepeda per bulan pada tahun 2011
    st.subheader("Penyewaan Sepeda per Bulan pada Tahun 2011")

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=data_bulanan_2011['mnth_day'], y=data_bulanan_2011['cnt_day'], palette="Blues", ax=ax)
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Total Penyewaan")
    ax.set_xticks(range(12))  # Pastikan ada 12 bulan
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"])
    st.pyplot(fig)

else:
    st.warning ("File CSV kosong")


## PADA GRAFIK PERTAMA, SAYA TIDAK TAHU BAGAIMANA CARA AGAR XLABEL TIDAK SEPANJANG ITU (BISA DIBACA), THATS WHY SAYA MENCOBA BIKIN GRAFIK KEDUA