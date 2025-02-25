# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data():
    day_data = pd.read_csv('day.csv')  # Path yang benar untuk file day.csv
    return day_data
# Main function for the Streamlit dashboard
def main():
    st.title("Analisis Data Bike Sharing")
    st.sidebar.title("Menu")
    st.sidebar.subheader("Pilih Halaman untuk Visualisasi")

    # Load data
    day_data = load_data()

    # Display dataset preview
    if st.sidebar.checkbox('Tampilkan Data Awal'):
        st.subheader('Preview Data')
        st.write(day_data.head())

    # Menampilkan visualisasi suhu dan jumlah sewa sepeda
    if st.sidebar.checkbox('Visualisasi Suhu dan Jumlah Sewa Sepeda'):
        st.subheader('Hubungan Suhu dan Jumlah Sewa Sepeda')
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='temp', y='cnt', data=day_data)
        plt.title('Hubungan Suhu dan Jumlah Sewa Sepeda')
        plt.xlabel('Suhu')
        plt.ylabel('Jumlah Sewa Sepeda')
        st.pyplot()

    # Menampilkan visualisasi hari kerja dan jumlah sewa sepeda
    if st.sidebar.checkbox('Visualisasi Hari Kerja dan Jumlah Sewa Sepeda'):
        st.subheader('Jumlah Sewa Sepeda Berdasarkan Hari Kerja')
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='workingday', y='cnt', data=day_data)
        plt.title('Jumlah Sewa Sepeda Berdasarkan Hari Kerja')
        plt.xlabel('Hari Kerja (0=Weekend/Holiday, 1=Working Day)')
        plt.ylabel('Jumlah Sewa Sepeda')
        st.pyplot()

    # Menampilkan visualisasi pengaruh cuaca terhadap jumlah sewa sepeda
    if st.sidebar.checkbox('Visualisasi Pengaruh Cuaca terhadap Jumlah Sewa Sepeda'):
        st.subheader('Pengaruh Cuaca terhadap Jumlah Sewa Sepeda')
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='weathersit', y='cnt', data=day_data)
        plt.title('Pengaruh Cuaca terhadap Jumlah Sewa Sepeda')
        plt.xlabel('Jenis Cuaca')
        plt.ylabel('Jumlah Sewa Sepeda')
        st.pyplot()

    # Menampilkan kesimpulan
    if st.sidebar.checkbox('Tampilkan Kesimpulan'):
        st.subheader('Kesimpulan')
        st.write("### Kesimpulan Pertanyaan 1:")
        st.write("Cuaca memengaruhi jumlah sewa sepeda. Saat cuaca cerah atau sedikit berawan, jumlah sewa sepeda lebih tinggi, sedangkan saat cuaca buruk, jumlah sewa cenderung lebih rendah.")
        st.write("### Kesimpulan Pertanyaan 2:")
        st.write("Hari kerja berpengaruh pada jumlah sewa sepeda, di mana pada hari kerja, jumlah sewa sepeda lebih tinggi dibandingkan dengan akhir pekan atau hari libur.")

if __name__ == "__main__":
    main()

st.caption('Copyright © Akbar Alfaidah 2025')
