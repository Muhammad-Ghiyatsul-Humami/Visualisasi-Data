# Import library
import streamlit as st
import datetime # Diperlukan untuk st.date_input

# WAJIB: Menampilkan identitas kelompok
st.title("Praktikum 1 - Visualisasi Data")
st.markdown("**Kelompok 15**")
st.markdown("""
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
""")
st.caption("Bagian 5: Forms")
st.markdown("---")

# --- Implementasi Forms ---
st.header("Contoh Penggunaan st.form")
st.subheader("Formulir Pendaftaran")

# 'with st.form(...)' memulai blok formulir.
# Semua elemen input di dalamnya akan dikelompokkan.
with st.form(key="form_pendaftaran"):
    
    # Elemen input untuk Nama (sesuai instruksi)
    nama = st.text_input(label="Masukkan Nama Anda")
    
    # Elemen input untuk Angka (sesuai instruksi)
    usia = st.number_input(label="Masukkan Usia", min_value=0, max_value=100, step=1)
    
    # Elemen input untuk Tanggal (sesuai instruksi)
    tanggal = st.date_input(label="Pilih Tanggal Pendaftaran", value=datetime.date(2025, 1, 1))

    # Elemen input untuk File (sesuai instruksi)
    file = st.file_uploader(label="Upload Berkas (opsional)", type=['pdf', 'docx'])

    # Tombol Submit Form
    # Tombol ini WAJIB ada di dalam 'st.form'
    submit_button = st.form_submit_button(label='Kirim')

# Logika ini akan dieksekusi HANYA JIKA tombol 'submit_button' ditekan.
if submit_button:
    st.success("Formulir Berhasil Dikirim!")
    st.subheader("Data yang Anda Masukkan:")
    st.write(f"**Nama:** {nama}")
    st.write(f"**Usia:** {usia} tahun")
    st.write(f"**Tanggal Pendaftaran:** {tanggal}")
    
    if file is not None:
        st.write(f"**Nama File:** {file.name}")
    else:
        st.write("**Berkas:** Tidak diunggah")