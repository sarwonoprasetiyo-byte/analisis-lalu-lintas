
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Data dari Lembar Kerja Word: 24 jam x 2 arah (48 baris)
data = [{'jam': 0, 'arah': 'Utara', 'sepeda_motor': 204, 'kendaraan_ringan': 82, 'kendaraan_berat': 41}, {'jam': 1, 'arah': 'Utara', 'sepeda_motor': 145, 'kendaraan_ringan': 54, 'kendaraan_berat': 28}, {'jam': 2, 'arah': 'Utara', 'sepeda_motor': 112, 'kendaraan_ringan': 40, 'kendaraan_berat': 36}, {'jam': 3, 'arah': 'Utara', 'sepeda_motor': 109, 'kendaraan_ringan': 43, 'kendaraan_berat': 27}, {'jam': 4, 'arah': 'Utara', 'sepeda_motor': 208, 'kendaraan_ringan': 80, 'kendaraan_berat': 39}, {'jam': 5, 'arah': 'Utara', 'sepeda_motor': 554, 'kendaraan_ringan': 218, 'kendaraan_berat': 40}, {'jam': 6, 'arah': 'Utara', 'sepeda_motor': 1224, 'kendaraan_ringan': 437, 'kendaraan_berat': 58}, {'jam': 7, 'arah': 'Utara', 'sepeda_motor': 1494, 'kendaraan_ringan': 525, 'kendaraan_berat': 76}, {'jam': 8, 'arah': 'Utara', 'sepeda_motor': 1106, 'kendaraan_ringan': 396, 'kendaraan_berat': 62}, {'jam': 9, 'arah': 'Utara', 'sepeda_motor': 871, 'kendaraan_ringan': 351, 'kendaraan_berat': 56}, {'jam': 10, 'arah': 'Utara', 'sepeda_motor': 817, 'kendaraan_ringan': 302, 'kendaraan_berat': 50}, {'jam': 11, 'arah': 'Utara', 'sepeda_motor': 852, 'kendaraan_ringan': 324, 'kendaraan_berat': 49}, {'jam': 12, 'arah': 'Utara', 'sepeda_motor': 903, 'kendaraan_ringan': 341, 'kendaraan_berat': 62}, {'jam': 13, 'arah': 'Utara', 'sepeda_motor': 904, 'kendaraan_ringan': 302, 'kendaraan_berat': 52}, {'jam': 14, 'arah': 'Utara', 'sepeda_motor': 874, 'kendaraan_ringan': 336, 'kendaraan_berat': 58}, {'jam': 15, 'arah': 'Utara', 'sepeda_motor': 1043, 'kendaraan_ringan': 343, 'kendaraan_berat': 51}, {'jam': 16, 'arah': 'Utara', 'sepeda_motor': 1290, 'kendaraan_ringan': 466, 'kendaraan_berat': 53}, {'jam': 17, 'arah': 'Utara', 'sepeda_motor': 1381, 'kendaraan_ringan': 484, 'kendaraan_berat': 57}, {'jam': 18, 'arah': 'Utara', 'sepeda_motor': 1166, 'kendaraan_ringan': 353, 'kendaraan_berat': 48}, {'jam': 19, 'arah': 'Utara', 'sepeda_motor': 859, 'kendaraan_ringan': 303, 'kendaraan_berat': 57}, {'jam': 20, 'arah': 'Utara', 'sepeda_motor': 690, 'kendaraan_ringan': 246, 'kendaraan_berat': 44}, {'jam': 21, 'arah': 'Utara', 'sepeda_motor': 486, 'kendaraan_ringan': 174, 'kendaraan_berat': 44}, {'jam': 22, 'arah': 'Utara', 'sepeda_motor': 375, 'kendaraan_ringan': 153, 'kendaraan_berat': 32}, {'jam': 23, 'arah': 'Utara', 'sepeda_motor': 287, 'kendaraan_ringan': 107, 'kendaraan_berat': 44}, {'jam': 0, 'arah': 'Selatan', 'sepeda_motor': 188, 'kendaraan_ringan': 69, 'kendaraan_berat': 34}, {'jam': 1, 'arah': 'Selatan', 'sepeda_motor': 144, 'kendaraan_ringan': 50, 'kendaraan_berat': 25}, {'jam': 2, 'arah': 'Selatan', 'sepeda_motor': 99, 'kendaraan_ringan': 40, 'kendaraan_berat': 33}, {'jam': 3, 'arah': 'Selatan', 'sepeda_motor': 100, 'kendaraan_ringan': 41, 'kendaraan_berat': 33}, {'jam': 4, 'arah': 'Selatan', 'sepeda_motor': 193, 'kendaraan_ringan': 75, 'kendaraan_berat': 28}, {'jam': 5, 'arah': 'Selatan', 'sepeda_motor': 540, 'kendaraan_ringan': 192, 'kendaraan_berat': 45}, {'jam': 6, 'arah': 'Selatan', 'sepeda_motor': 955, 'kendaraan_ringan': 350, 'kendaraan_berat': 49}, {'jam': 7, 'arah': 'Selatan', 'sepeda_motor': 1178, 'kendaraan_ringan': 428, 'kendaraan_berat': 69}, {'jam': 8, 'arah': 'Selatan', 'sepeda_motor': 914, 'kendaraan_ringan': 334, 'kendaraan_berat': 48}, {'jam': 9, 'arah': 'Selatan', 'sepeda_motor': 791, 'kendaraan_ringan': 281, 'kendaraan_berat': 55}, {'jam': 10, 'arah': 'Selatan', 'sepeda_motor': 735, 'kendaraan_ringan': 261, 'kendaraan_berat': 51}, {'jam': 11, 'arah': 'Selatan', 'sepeda_motor': 770, 'kendaraan_ringan': 272, 'kendaraan_berat': 53}, {'jam': 12, 'arah': 'Selatan', 'sepeda_motor': 947, 'kendaraan_ringan': 288, 'kendaraan_berat': 49}, {'jam': 13, 'arah': 'Selatan', 'sepeda_motor': 766, 'kendaraan_ringan': 289, 'kendaraan_berat': 45}, {'jam': 14, 'arah': 'Selatan', 'sepeda_motor': 755, 'kendaraan_ringan': 311, 'kendaraan_berat': 57}, {'jam': 15, 'arah': 'Selatan', 'sepeda_motor': 1026, 'kendaraan_ringan': 388, 'kendaraan_berat': 48}, {'jam': 16, 'arah': 'Selatan', 'sepeda_motor': 1423, 'kendaraan_ringan': 490, 'kendaraan_berat': 70}, {'jam': 17, 'arah': 'Selatan', 'sepeda_motor': 1303, 'kendaraan_ringan': 509, 'kendaraan_berat': 62}, {'jam': 18, 'arah': 'Selatan', 'sepeda_motor': 1137, 'kendaraan_ringan': 415, 'kendaraan_berat': 57}, {'jam': 19, 'arah': 'Selatan', 'sepeda_motor': 717, 'kendaraan_ringan': 247, 'kendaraan_berat': 47}, {'jam': 20, 'arah': 'Selatan', 'sepeda_motor': 582, 'kendaraan_ringan': 213, 'kendaraan_berat': 42}, {'jam': 21, 'arah': 'Selatan', 'sepeda_motor': 480, 'kendaraan_ringan': 152, 'kendaraan_berat': 33}, {'jam': 22, 'arah': 'Selatan', 'sepeda_motor': 363, 'kendaraan_ringan': 125, 'kendaraan_berat': 34}, {'jam': 23, 'arah': 'Selatan', 'sepeda_motor': 283, 'kendaraan_ringan': 99, 'kendaraan_berat': 38}]
df = pd.DataFrame(data)

def baca_data(df):
    wajib = ["jam","arah","sepeda_motor","kendaraan_ringan","kendaraan_berat"]
    if df.empty or not set(wajib).issubset(df.columns):
        raise ValueError("Data kosong atau kolom wajib tidak lengkap.")
    if df[wajib].isnull().any().any():
        raise ValueError("Terdapat data kosong.")
    for c in ["jam","sepeda_motor","kendaraan_ringan","kendaraan_berat"]:
        df[c] = pd.to_numeric(df[c], errors="raise")
    if len(df) != 48 or not df.jam.between(0,23).all():
        raise ValueError("Data harus 48 baris dan jam 0–23.")
    if (df[["sepeda_motor","kendaraan_ringan","kendaraan_berat"]] < 0).any().any():
        raise ValueError("Jumlah kendaraan tidak boleh negatif.")
    if set(df.arah) != {"Utara","Selatan"} or df.duplicated(["jam","arah"]).any():
        raise ValueError("Arah tidak sesuai atau ada jam-arah duplikat.")
    return df

def hitung_volume(df):
    hasil=df.copy()
    hasil["total"]=hasil[["sepeda_motor","kendaraan_ringan","kendaraan_berat"]].sum(axis=1)
    return hasil

def rekap_per_arah(df):
    return df.groupby("arah")[["sepeda_motor","kendaraan_ringan","kendaraan_berat","total"]].sum()

def rekap_per_jam(df):
    return df.groupby("jam")[["sepeda_motor","kendaraan_ringan","kendaraan_berat","total"]].sum().reset_index()

def hitung_persentase(df):
    jumlah=df[["sepeda_motor","kendaraan_ringan","kendaraan_berat"]].sum()
    return (jumlah/jumlah.sum()*100).round(2)

def buat_grafik(jam, hasil, folder):
    plt.figure(figsize=(10,5))
    plt.plot(jam.jam,jam.total,marker="o")
    plt.xticks(range(24)); plt.xlabel("Jam"); plt.ylabel("Kendaraan/jam")
    plt.title("Volume Lalu Lintas Gabungan per Jam"); plt.grid(True,alpha=.3)
    plt.tight_layout(); plt.savefig(folder/"grafik_volume_per_jam.png",dpi=300); plt.show()
    p=hasil.pivot(index="jam",columns="arah",values="total").sort_index()
    plt.figure(figsize=(10,5))
    for a in ["Utara","Selatan"]: plt.plot(p.index,p[a],marker="o",label=a)
    plt.xticks(range(24)); plt.xlabel("Jam"); plt.ylabel("Kendaraan/jam")
    plt.title("Perbandingan Volume Arah"); plt.grid(True,alpha=.3); plt.legend()
    plt.tight_layout(); plt.savefig(folder/"grafik_perbandingan_arah.png",dpi=300); plt.show()

def main():
    valid=baca_data(df)
    hasil=hitung_volume(valid)
    arah=rekap_per_arah(hasil)
    jam=rekap_per_jam(hasil)
    persen=hitung_persentase(hasil)
    puncak=jam.loc[jam.total.idxmax()]
    puncak_arah=hasil.loc[hasil.groupby("arah").total.idxmax(),["arah","jam","total"]]
    lima=jam.nlargest(5,"total")
    print("REKAP PER ARAH"); print(arah)
    print("\\nREKAP PER JAM"); print(jam.to_string(index=False))
    print("\\nPERSENTASE (%):"); print(persen)
    print(f"\\nJam puncak gabungan: {int(puncak.jam):02d}.00–{int(puncak.jam):02d}.59 = {int(puncak.total):,} kendaraan/jam")
    print("\\nJam puncak tiap arah:"); print(puncak_arah.to_string(index=False))
    print("\\nLima jam tertinggi:"); print(lima.to_string(index=False))
    # Uji manual sesuai dokumen Word
    assert int(hasil.query("jam==0 and arah=='Utara'").total.iloc[0])==327
    assert int(hasil.query("jam==0 and arah=='Selatan'").total.iloc[0])==291
    assert int(jam.query("jam==0").total.iloc[0])==618
    assert int(jam.query("jam==17").total.iloc[0])==3796
    print("\\nValidasi manual: BERHASIL")
    folder=Path("hasil_analisis_lalu_lintas"); folder.mkdir(exist_ok=True)
    hasil.to_csv(folder/"data_dengan_total.csv",index=False,encoding="utf-8-sig")
    arah.to_csv(folder/"rekap_per_arah.csv",encoding="utf-8-sig")
    jam.to_csv(folder/"rekap_per_jam.csv",index=False,encoding="utf-8-sig")
    persen.to_csv(folder/"persentase_jenis_kendaraan.csv",encoding="utf-8-sig")
    lima.to_csv(folder/"lima_jam_tertinggi.csv",index=False,encoding="utf-8-sig")
    buat_grafik(jam,hasil,folder)
    kesimpulan=f"Total {int(hasil.total.sum()):,}; Utara {int(arah.loc['Utara','total']):,}; Selatan {int(arah.loc['Selatan','total']):,}; jam puncak {int(puncak.jam):02d}.00–{int(puncak.jam):02d}.59 ({int(puncak.total):,} kendaraan/jam)."
    (folder/"kesimpulan.txt").write_text(kesimpulan,encoding="utf-8")
    print("\\nKESIMPULAN:",kesimpulan)
    print("Hasil disimpan di",folder.resolve())

if __name__=="__main__":
    main()
