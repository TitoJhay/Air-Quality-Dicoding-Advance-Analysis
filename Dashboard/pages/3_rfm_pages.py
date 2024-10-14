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

df_rfm = load_data()

st.write("# RFM Analysis Pages📈")

st.write(
    """
    RFM Analysis, bertujuan mengelompokkan pelanggan berdasarkan perilaku pembelian mereka dengan memperhatikan tiga faktor utama:
    - Recency: Menghitung jumlah hari sejak terakhir kali pelanggan melakukan pembelian.
    - Frequency: Menghitung jumlah total transaksi yang dilakukan oleh pelanggan dalam periode tertentu.
    - Monetary: Menghitung total pengeluaran pelanggan dalam periode tersebut.
    Anda dapat melihat contoh implementasi kodenya pada submodul Latihan Membuat Visualisasi Data.
    """
)

st.markdown("### RFM Analysis | Parameter yang dipakai adalah **SO2**")
st.markdown(
    """
    Parameter yang dipakai.
    - Recency: parameter yang digunakan untuk melihat kapan terakhir *station* bernilai danger terhadap SO2.
    - Frequency: parameter ini digunakan untuk mengidentifikasi seberapa sering station kedapatan bernilai danger terhadap SO2.
    - Monetary: parameter terakhir ini digunakan untuk mengidentifikasi seberapa besar jumlah SO2 yang berasal dari *station* tersebut.
    """
    )

st.markdown("#### Dataframe")

st.dataframe(df_rfm)

st.markdown("#### RFM Visualizations")

# Recency Chart
recency_chart = alt.Chart(df_rfm).mark_bar().encode(
    x=alt.X('station:N', sort='-y'),
    y=alt.Y('recency:Q'),
    color=alt.Color('recency:Q', scale=alt.Scale(scheme='viridis'))
).properties(
    title='By Recency (hours)',
    width=600,
    height=300
)

st.altair_chart(recency_chart, use_container_width=True)

# Frequency Chart
frequency_chart = alt.Chart(df_rfm).mark_bar().encode(
    x=alt.X('station:N', sort='-y'),
    y='frequency:Q',
    color=alt.Color('frequency:Q', scale=alt.Scale(scheme='viridis'))
).properties(
    title='By Frequency',
    width=600,
    height=300
)

st.altair_chart(frequency_chart, use_container_width=True)

# Monetary Chart
monetary_chart = alt.Chart(df_rfm).mark_bar().encode(
    x=alt.X('station:N', sort='-y'),
    y='monetary:Q',
    color=alt.Color('monetary:Q', scale=alt.Scale(scheme='viridis'))
).properties(
    title='By Monetary',
    width=600,
    height=300
)

st.altair_chart(monetary_chart, use_container_width=True)

st.write("""
RFM Analysis :
    -Recency: parameter yang digunakan untuk melihat kapan terakhir station bernilai danger terhadap SO2.
    -Frequency: parameter ini digunakan untuk mengidentifikasi seberapa sering station kedapatan bernilai danger terhadap SO2.
    -Monetary: parameter terakhir ini digunakan untuk mengidentifikasi seberapa besar jumlah SO2 yang berasal dari station tersebut.

    1. Berdasarkan urutan Pertama terjadi(recency) polutan SO2 bernilai danger, **adalah shunyi sebagai yang pertama, Lalu Wanshouxigong & Guanyuan sebagai yang terakhir terjadi keadaan danger beda 30 jam sebelumnya.**
    2. Berdasarkan *frequency* banyak kejadian SO2 bernilai danger ditempati **pada stasiun Dongsi, Wanliu, Nongzhangguan sebagai stasiun yang terbanyak mendekati 14000 kali situasi SO2 benilai danger.**
    3. Berdasarkan Jumlah(monetary) menghasilkan polusi SO2 bernilai danger tertinggi terjadi **di stasiun Dongsi dimana sebanyak diatas 400000 polutan SO2 bernilai danger yang dihasilkan**
    """)


### Sidebar
st.sidebar.caption(
    "Built by [Tito Jhay](https://www.linkedin.com/in/tito-jaya-9b5537201/). Like this? [Hire me!](https://www.instagram.com/jhaymedias)"
)

# Define image paths
linkedin = "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/linkedin.gif"
dicoding = "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/topmate.gif"
email = "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/email.gif"
share = "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/share.gif"

st.sidebar.caption(
    f"""
    <div style='display: flex; align-items: center;'>
        <a href='https://www.linkedin.com/in/tito-jaya-9b5537201/'><img src='{linkedin}' style='width: 35px; height: 35px; margin-right: 25px;'></a>
        <a href='https://www.dicoding.com/users/titojayaaaa/academies'><img src='{dicoding}' style='width: 32px; height: 32px; margin-right: 25px;'></a>
        <a href='mailto:mhmmdtjaya@gmail.com'><img src='{email}' style='width: 28px; height: 28px; margin-right: 25px;'></a>
        <a href='https://www.kaggle.com/jhayyy'><img src='{share}' style='width: 28px; height: 28px; margin-right: 25px;'></a>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.caption(
    "Thanks For your support!"
)
