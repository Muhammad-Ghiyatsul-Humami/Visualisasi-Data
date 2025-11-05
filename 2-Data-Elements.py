#import library
import streamlit as st
import pandas as pd #untuk mengelola data dalam bentuk tabel (data frame)
import numpy as np #untuk membuat data numerik acak
import altair as alt #untuk membuat chart interaktif


st.title("Praktikum 1 - Visualisasi Data")


#st.markdown digunakan untuk menampilkan teks dengan format
st.markdown("**Kelompok 15**")
st.markdown("""
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)

st.caption("Bagian 2: Data Elements")

("------------------------------------------------------------------------------------------------------")

#dataFrame: struktur data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10), 
    columns=('col_no %d' % i for i in range (10))
)

#menampilkan dataframe
st.dataframe(df)

st.subheader("Highligh Minimun Value di DataFrame")


#highlight nilai terkecil disetiap kolom dataframe
#axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))




("------------------------------------------------------------------------------------------------------")

#tabel statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10), 
    columns=('col_no %d' % i for i in range (10))
)


#menampilkan tabel statis
st.table(df)




("------------------------------------------------------------------------------------------------------")

#metrics: komponen tampilan angka penting
st.subheader("Metrics")

#menampilkan metrik tunggal (nilai utama + perubahan nilai)

#metrics tunggal
st.metric(label="Temperature", value="31 C", delta="1.2 C") #kenaikan 1.2 C
("------------------------------------------------------------------------------------------------------")

#metrics sesuai delta_color
#delta_color digunakan untuk memberi warna sesuai arahan perubahan:
#"normal" (default: naik - hijau, turun - merah)
#"inverse": kebalikannya (naik-merah)
#"off": tidak menampilkan warna perubahan

#definisikan variabel metrics
col1, col2, col3 = st.columns(3)

#menampilkan indiator data
col1.metric("Curah Hujan", "100 cm", "10 cm") #naik dan baik
("------------------------------------------------------------------------------------------------------")
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") #naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off") #netral (tidak baik, tidak buruk)
#menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) #kosong #naik baik karena di setting default
st.metric("Trees", "91456", "-1132649") #penurunan