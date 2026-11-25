
import streamlit as st

st.title("Program Analisis Lalu Lintas")

st.write("Aplikasi untuk menghitung jumlah kendaraan.")

sepeda_motor = st.number_input(
    "Jumlah sepeda motor", min_value=0, value=204
)

kendaraan_ringan = st.number_input(
    "Jumlah kendaraan ringan", min_value=0, value=82
)

kendaraan_berat = st.number_input(
    "Jumlah kendaraan berat", min_value=0, value=41
)

total = sepeda_motor + kendaraan_ringan + kendaraan_berat

st.subheader("Hasil Analisis")
st.write("Total kendaraan:", total)
