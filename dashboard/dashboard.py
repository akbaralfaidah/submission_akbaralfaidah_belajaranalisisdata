# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset


@st.cache
def load_data():
    day_data = pd.read_csv('day.csv')  # Path yang benar untuk file day.csv
    day_data['dteday'] = pd.to_datetime(
        day_data['dteday'])  # Pastikan format tanggal benar
    return day_data

# Main function for the Streamlit dashboard


def main():
    st.title("Analisis Data Bike Sharing")
    st.sidebar.title("Menu")

    # Load data
    day_data = load_data()

    # Filtering berdasarkan tanggal
    st.sidebar.subheader("Filter Berdasarkan Tanggal")
    start_date = st.sidebar.date_input('Tanggal Mulai', min_value=day_data['dteday'].min(
    ), max_value=day_data['dteday'].max(), value=day_data['dteday'].min())
    end_date = st.sidebar.date_input('Tanggal Akhir', min_value=day_data['dteday'].min(
    ), max_value=day_data['dteday'].max(), value=day_data['dteday'].max())
    filtered_data = day_data[(day_data['dteday'] >= pd.to_datetime(
        start_date)) & (day_data['dteday'] <= pd.to_datetime(end_date))]

    # Filter berdasarkan musim
    st.sidebar.subheader("Filter Berdasarkan Musim")
    season_filter = st.sidebar.selectbox(
        "Pilih Musim", ['Semua', 'Musim Dingin', 'Panas', 'Musim Gugur', 'Musim Semi'])
    if season_filter != 'Semua':
        filtered_data = filtered_data[filtered_data['season'] == [
            'Semua', 'Musim Dingin', 'Panas', 'Musim Gugur', 'Musim Semi'].index(season_filter)]

    # Filter berdasarkan cuaca
    st.sidebar.subheader("Filter Berdasarkan Cuaca")
    weather_filter = st.sidebar.selectbox(
        "Pilih Jenis Cuaca", ['Semua', 'Cerah', 'Berawan', 'Hujan/Berkabut'])
    if weather_filter != 'Semua':
        weather_mapping = {1: 'Cerah', 2: 'Berawan', 3: 'Hujan/Berkabut'}
        filtered_data = filtered_data[filtered_data['weathersit'] == list(
            weather_mapping.values()).index(weather_filter)]

    # Display dataset preview
    if st.sidebar.checkbox('Tampilkan Data Awal'):
        st.subheader('Preview Data')
        st.write(filtered_data.head())

    # Menampilkan visualisasi suhu dan jumlah sewa sepeda
    if st.sidebar.checkbox('Visualisasi Suhu dan Jumlah Sewa Sepeda'):
        st.subheader('Hubungan Suhu dan Jumlah Sewa Sepeda')
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='temp', y='cnt', data=filtered_data)
        plt.title('Hubungan Suhu dan Jumlah Sewa Sepeda')
        plt.xlabel('Suhu')
        plt.ylabel('Jumlah Sewa Sepeda')
        st.pyplot()

    # Menampilkan visualisasi hari kerja dan jumlah sewa sepeda
    if st.sidebar.checkbox('Visualisasi Hari Kerja dan Jumlah Sewa Sepeda'):
        st.subheader('Jumlah Sewa Sepeda Berdasarkan Hari Kerja')
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='workingday', y='cnt', data=filtered_data)
        plt.title('Jumlah Sewa Sepeda Berdasarkan Hari Kerja')
        plt.xlabel('Hari Kerja (0=Weekend/Holiday, 1=Working Day)')
        plt.ylabel('Jumlah Sewa Sepeda')
        plt.xticks([0, 1], ['Akhir Pekan/Hari Libur', 'Hari Kerja'])
        st.pyplot()

    # Menampilkan visualisasi pengaruh cuaca terhadap jumlah sewa sepeda
    if st.sidebar.checkbox('Visualisasi Pengaruh Cuaca terhadap Jumlah Sewa Sepeda'):
        st.subheader('Pengaruh Cuaca terhadap Jumlah Sewa Sepeda')
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='weathersit', y='cnt', data=filtered_data)
        plt.title('Pengaruh Cuaca terhadap Jumlah Sewa Sepeda')
        plt.xlabel('Jenis Cuaca')
        plt.ylabel('Jumlah Sewa Sepeda')
        plt.xticks([0, 1, 2], ['Cerah', 'Berawan', 'Hujan/Berkabut'])
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
