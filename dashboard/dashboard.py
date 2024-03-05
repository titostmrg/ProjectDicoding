import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.title('Penyewaan Sepeda')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

all_df = pd.read_csv("dashboard/all_data.csv")

with tab1:
    st.header("Chart")
    st.container()
    holiday_df = all_df[all_df['holiday_x'] == 1]
    non_holiday_df = all_df[all_df['holiday_x'] == 0]

    avg_holiday = holiday_df['cnt_y'].mean()
    avg_non_holiday = non_holiday_df['cnt_y'].mean()

    plt.figure(figsize=(8, 6))
    plt.bar(['Hari Biasa', 'Hari Libur'], [avg_non_holiday, avg_holiday], color=['blue', 'orange'])

    plt.title('Rata-Rata Jumlah Peminjaman Sepeda pada Hari Libur dan Hari Biasa')
    plt.xlabel('Tipe Hari')
    plt.ylabel('Rata-Rata Jumlah Peminjaman Sepeda')

    st.pyplot(plt)


 
with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")