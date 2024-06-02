import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Baca file excel
@st.cache_data
def load_data():
    df = pd.read_excel('Kelompok_10.xlsx')
    return df

df = load_data()

# Mengatur judul halaman
st.title("Korelasi Data")

# Tampilkan data
st.write(df)

# Buat scatter plot
fig, axs = plt.subplots(3, figsize=(5, 15))

# Scatter plot untuk RataanNilaiEkspresi_Gal-Cln3 dan RataanNilaiEkspresi_Gal_Clb2
axs[0].scatter(df['RataanNilaiEkspresi_Gal-Cln3'], df['RataanNilaiEkspresi_Gal_Clb2'])
axs[0].set_xlabel('RataanNilaiEkspresi_Gal-Cln3')
axs[0].set_ylabel('RataanNilaiEkspresi_Gal_Clb2')

# Scatter plot untuk RataanNilaiEkspresi_Gal-Cln3 dan Nilai_aggregat
axs[1].scatter(df['RataanNilaiEkspresi_Gal-Cln3'], df['Nilai_aggregat'])
axs[1].set_xlabel('RataanNilaiEkspresi_Gal-Cln3')
axs[1].set_ylabel('Nilai_aggregat')

# Scatter plot untuk RataanNilaiEkspresi_Gal_Clb2 dan Nilai_aggregat
axs[2].scatter(df['RataanNilaiEkspresi_Gal_Clb2'], df['Nilai_aggregat'])
axs[2].set_xlabel('RataanNilaiEkspresi_Gal_Clb2')
axs[2].set_ylabel('Nilai_aggregat')

# Tampilkan grafik
st.pyplot(fig)
