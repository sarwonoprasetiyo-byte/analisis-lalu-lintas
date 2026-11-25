import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from analisis_data import (
    df,
    baca_data,
    hitung_volume,
    rekap_per_arah,
    rekap_per_jam,
    hitung_persentase,
)

st.set_page_config(
    page_title="Analisis Volume Lalu Lintas",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 Analisis Volume Lalu Lintas")
st.write(
    "Website untuk melihat volume kendaraan berdasarkan jam dan arah "
    "Utara–Selatan."
)

# Memproses data
data_valid = baca_data(df.copy())
hasil = hitung_volume(data_valid)
rekap_arah = rekap_per_arah(hasil)
rekap_jam = rekap_per_jam(hasil)
persentase = hitung_persentase(hasil)

total_kendaraan = int(hasil["total"].sum())
jam_puncak = rekap_jam.loc[rekap_jam["total"].idxmax()]

# Ringkasan utama
kolom1, kolom2, kolom3 = st.columns(3)

kolom1.metric(
    "Total kendaraan",
    f"{total_kendaraan:,}"
)

kolom2.metric(
    "Jam puncak",
    f"{int(jam_puncak['jam']):02d}.00–"
    f"{int(jam_puncak['jam']):02d}.59"
)

kolom3.metric(
    "Volume pada jam puncak",
    f"{int(jam_puncak['total']):,} kendaraan/jam"
)

st.divider()

# Pilihan tampilan
pilihan = st.selectbox(
    "Pilih tampilan data",
    [
        "Rekap per jam",
        "Rekap per arah",
        "Persentase jenis kendaraan",
        "Data lengkap"
    ]
)

if pilihan == "Rekap per jam":
    st.subheader("Rekap Volume Kendaraan per Jam")
    st.dataframe(rekap_jam, use_container_width=True)

elif pilihan == "Rekap per arah":
    st.subheader("Rekap Volume Kendaraan per Arah")
    st.dataframe(rekap_arah, use_container_width=True)

elif pilihan == "Persentase jenis kendaraan":
    st.subheader("Persentase Jenis Kendaraan")
    tabel_persen = persentase.rename("Persentase (%)").to_frame()
    st.dataframe(tabel_persen, use_container_width=True)

else:
    st.subheader("Data Lengkap")
    st.dataframe(hasil, use_container_width=True)

st.divider()

# Grafik gabungan per jam
st.subheader("Grafik Volume Lalu Lintas Gabungan")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(
    rekap_jam["jam"],
    rekap_jam["total"],
    marker="o"
)
ax.set_xlabel("Jam")
ax.set_ylabel("Kendaraan per jam")
ax.set_xticks(range(24))
ax.grid(True, alpha=0.3)

st.pyplot(fig)

# Grafik per arah
st.subheader("Perbandingan Volume Arah Utara dan Selatan")

pivot = hasil.pivot(
    index="jam",
    columns="arah",
    values="total"
).sort_index()

fig2, ax2 = plt.subplots(figsize=(10, 4))

for arah in ["Utara", "Selatan"]:
    ax2.plot(
        pivot.index,
        pivot[arah],
        marker="o",
        label=arah
    )

ax2.set_xlabel("Jam")
ax2.set_ylabel("Kendaraan per jam")
ax2.set_xticks(range(24))
ax2.grid(True, alpha=0.3)
ax2.legend()

st.pyplot(fig2)

# Unduh data hasil
st.subheader("Unduh Hasil Analisis")

csv_hasil = hasil.to_csv(index=False).encode("utf-8-sig")

st.download_button(
    label="Unduh data lengkap (CSV)",
    data=csv_hasil,
    file_name="data_volume_lalu_lintas.csv",
    mime="text/csv"
)

st.success(
    "Analisis selesai. Data yang ditampilkan berasal dari "
    "program analisis volume lalu lintas."
)
