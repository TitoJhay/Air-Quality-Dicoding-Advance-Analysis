import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Cluster Pages",
    page_icon="📈",
)

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('dashboard/rfm.csv')
    except FileNotFoundError:
        df = pd.read_csv('rfm.csv')
    return df
df_cls = load_data()

st.write("# Cluster Pages📈")

st.write(
    """
    Clustering, bertujuan mengelompokkan data ke dalam grup berdasarkan karakteristik tertentu tanpa menggunakan algoritma machine learning. Berikut adalah beberapa metode clustering yang bisa diterapkan:\n
    - Manual Grouping: Menentukan kriteria pengelompokan berdasarkan aturan bisnis atau pemahaman domain, seperti mengelompokkan pelanggan berdasarkan rentang usia, pendapatan, atau jumlah transaksi.\n
    - Binning: Menggunakan teknik binning untuk membagi data ke dalam interval atau kategori tertentu.
    """
)

st.markdown("### Clustering | Polutan Condition(PM2.5 + PM10) berdasarkan tiap stasiun")
st.markdown("#### Dataframe")

st.dataframe(df_cls)

df_cls = df_cls.sort_values(by="PolutanCondition", ascending=False)

# Create and display the chart using the sorted DataFrame
chart = alt.Chart(df_cls).mark_bar().encode(
    y=alt.Y('station:N', title='Station', sort='-x'),  # Sort stations based on the x-axis values
    x=alt.X('PolutanCondition:Q', title='Polutan Condition of All Time'),
    color=alt.Color('PolutanCondition:Q', scale=alt.Scale(scheme='viridis'))
).properties(
    title='Average Polutan Condition for Each Station',
    width=800,
    height=400
)
st.altair_chart(chart)

st.markdown(
    """
    ### Hasil Analisis Lanjutan
    - Clustering | Polutan Condition berdasarkan tiap stasiun : Terlihat berdasarkan **frequency PolutanCondition di station yang bernilai bad, terbanyak dimiki Gucheng, Wanshouxigong, Dongsi, dst.** artinya adalah **di stasiun tersebut bisa dikatakan sering terjadi polusi tingkat tinggi, yang mana merupakan jumlah dari banyaknya PM2.5 dan PM10**
    """
)

### Sidebar
st.sidebar.caption(
    "Built by [Tito Jhay](https://www.linkedin.com/in/tito-jaya-9b5537201/). Like this? [Hire me!](https://www.instagram.com/jhaymedias)"
)

# Define image paths
linkedin = "img/linkedin.gif"
dicoding = "img/dicoding.gif"
email = "img/email.gif"
share = "img/share.gif"

# Create columns for the images
col1, col2, col3, col4 = st.sidebar.columns(4)

# Display images in columns
with col1:
    st.image(linkedin, width=35)
    st.markdown("[LinkedIn](https://www.linkedin.com/in/tito-jaya-9b5537201/)")

with col2:
    st.image(dicoding, width=32)
    st.markdown("[Dicoding](https://www.dicoding.com/users/titojayaaaa/academies)")

with col3:
    st.image(email, width=28)
    st.markdown("[Email](mailto:mhmmdtjaya@gmail.com)")

with col4:
    st.image(share, width=28)
    st.markdown("[Kaggle](https://www.kaggle.com/jhayyy)")


