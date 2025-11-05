#import library yang dibutuhkan
import streamlit as st


#bagian 1

#header - untuk membuat teks elemen
st.header("Ini header")
st.subheader("ini subheader")
st.text("ini teks biasa tanpa format")
st.markdown("**ini teks bold** dan *ini teks italic*")
st.caption("ini caption") #teks kecil dibawah elemen (untuk penjelasan)
st.title("Ini Judul")

("------------------------------------------------------------------------------------")


#tugas mandiri
st.title("Praktikum 1 Visualisasi Data")
st.subheader("Praktikum Text Elements")
st.markdown("**Kelompok 15**")
st.markdown("""
1. Abdu Azzam Alaris - 0110122073
2. M. Ghiyatsul Humami - 0110220108
3. Nurul Aeman - 0110222099
            """)

("---------------------------------------------------------------------")

#bagian 2

#menampilkan rumus (latex)
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') #rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') #rumus kuadrat binomial


("--------------------------------------------------------------------")

#bagian 3

#menampilkan kode program
st.header("Display Code")
st.subheader("Python Code")

#simpan ke variable
code = '''
def hello();
    print("Hello, Streamlit!)
    '''

#st.code() untuk menampilkan potongan kode dengag format rapi dan syntax highlighting
st.code(code, language='python')


st.subheader("Java Code")
st.code("""
    public class GFG {
        public static void main(string arg[]) {
            System.out.printIn("Hello World!):
        }
    }
""", language='java')

#fungsi st.code() bisa digunakan untuk bahasa oemrigraman lain seperti java, javascript, c++, HTML, dll

st.subheader("JavaScript")
st.code("""
<p id="demo"> </p>
<script>
    try {
        addalert("Welcome guest!); // kesalahan ketik (addalert)
        sengaja dibuat untuk menimbulkan error
    }
    catch(err) {
        document.getElementById("demo").innerHTML = err.message; //
        menampilkan pesan error di elemen HTML dengan id 'demo'   
    }
    </sript>

""", language='javascript')
