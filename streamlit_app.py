import streamlit as st

#Mengatur warna latar belakang dan gaya font
page_bg_color_str = """
<style>
body {
background-color: #f0f2f6; /* Warna latar belakang default */
}

.stApp {
    background-image: linear-gradient(to bottom right, #6a1b9a, #4a148c); /* Contoh gradien */
    background-size: cover;
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(page_bg_color_str, unsafe_allow_html=True)

st.title("CalorieCounting")
st.write("Selamat datang!")

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
