import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.title('Penyewaan Sepeda')
tab1, tab2 = st.tabs(["Rata Peminjaman Sepeda", "Tren"])

all_df = pd.read_csv("all_data.csv")

with tab1:
    st.header("Bagaimana pola penggunaan sepeda berubah selama hari libur dibandingkan dengan hari biasa?")

    st.header("Barplot")

    holiday_df = all_df[all_df['holiday_x'] == 1]
    non_holiday_df = all_df[all_df['holiday_x'] == 0]

    avg_holiday = holiday_df['cnt_y'].mean()
    avg_non_holiday = non_holiday_df['cnt_y'].mean()

    plt.figure(figsize=(8, 6))
    plt.bar(['Hari Biasa', 'Hari Libur'], [avg_non_holiday, avg_holiday], color=['blue', 'orange'])

    plt.title('c')
    plt.xlabel('Tipe Hari')
    plt.ylabel('Rata-Rata Jumlah Peminjaman Sepeda')

    st.pyplot(plt)

    st.header("Scatterplot")
    st.container()
    plt.figure(figsize=(8, 6))
    sns.stripplot(x='holiday_x', y='cnt_y', data=all_df, jitter=True, alpha=0.5)

    plt.title('Distribusi Jumlah Peminjaman Sepeda pada Hari Libur dan Hari Biasa')
    plt.xlabel('Tipe Hari')
    plt.ylabel('Jumlah Peminjaman Sepeda')

    st.pyplot(plt)

 
with tab2:
    st.header("Bagaimana pola penggunaan sepeda berubah selama hari libur dibandingkan dengan hari biasa?")
    
    st.write("Area")
    plt.figure(figsize=(12, 6))
    plt.fill_between(all_df['dteday_x'], all_df['cnt_y'], color='red', alpha=0.4)

    plt.title('Tren Penggunaan Sepeda Sewaan dari Waktu ke Waktu')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Peminjaman Sepeda')

    st.pyplot(plt)

    st.write("Scatterplot")
    plt.figure(figsize=(12, 6))
    plt.scatter(all_df['dteday_x'], all_df['cnt_y'], color='blue')

    plt.title('Tren Penggunaan Sepeda Sewaan dari Waktu ke Waktu')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    st.pyplot(plt)

    st.write("Scatterplot")
    plt.figure(figsize=(12, 6))
    plt.scatter(all_df['mnth_x'], all_df['cnt_y'], c=all_df['cnt_y'], cmap='viridis', alpha=0.6)

    plt.colorbar(label='Jumlah Peminjaman Sepeda')

    plt.title('Tren Penggunaan Sepeda Sewaan dari Waktu ke Waktu')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    st.pyplot(plt)

    st.write("Boxplot")
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=all_df, x='mnth_x', y='cnt_y')

    plt.title('Tren Penggunaan Sepeda Sewaan dari Waktu ke Waktu')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    st.pyplot(plt)