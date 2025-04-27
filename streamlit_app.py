import streamlit as st

#Mengatur warna latar belakang dan gaya font
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f3e9df;  /* Warna latar belakang baru */
        color: #c99548;             /* Warna teks baru */
        font-size: 18px;            /* Ukuran font tetap */
    }
    .css-1d391kg {
        color: #c99548;             /* Mengatur warna teks untuk elemen tertentu */
    }
    table {
        border: 2px solid #fb8e54;  /* Garis tabel dengan warna baru */
    }
    th {
        background-color: #fb8e54;  /* Warna latar untuk header tabel */
        color: white;               /* Warna teks untuk header tabel */
    }
    td {
        background-color: #f3e9df;  /* Warna latar untuk sel tabel */
        color: black;               /* Warna teks untuk sel tabel */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("CalorieCounting")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
