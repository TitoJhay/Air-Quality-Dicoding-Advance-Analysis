import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime, timedelta

st.set_page_config(page_title="Main Pages", page_icon="📈")

@st.cache_data(persist="disk")
def load_data():
    try:
        df = pd.read_csv('Data/main.csv')
    except FileNotFoundError:
        try:
            df = pd.read_csv('main.csv')
        except FileNotFoundError:
            st.error("Data file not found. Please check the file path.")
            return pd.DataFrame()  # Return an empty DataFrame if file is not found
    
    # Convert 'datetime' column to datetime type
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

@st.cache_data
def sample_data(df, n=10000):
    return df.sample(n=min(n, len(df)))

#Markdown
st.write("# Main Pages📈")

st.write("""This Pages Answering Question: 
- Apakah ketika cuaca hujan mengurangi jumlah polutan kotor dan meningkatkan jumlah polutan bersih?\n
- Bagaimana Peningkatan Frequency Rata-rata PM2.5 di sekitar Sebulan Terakhir, 6 bulan terakhir, 1 tahun terakhir, 5 tahun terakhir\n
- Bagaimana Peningkatan Frequency Rata-rata PM10 di sekitar Sebulan Terakhir, 6 bulan terakhir, 1 tahun terakhir, 5 tahun terakhir\n
- Bulan apa yang memiliki jumlah polutan (SO2,NO2,CO,O3) tertinggi!
""")

# Load data
df_main = load_data()

if df_main.empty:
    st.warning("No data available. Please check the data source.")
else:
    # Continue with the rest of your code
    st.markdown('### 1. Apakah ketika hujan mengurangi jumlah polutan kotor dan meningkatkan jumlah polutan bersih?')
    
    # Sample data for correlation and plotting
    df_sample = sample_data(df_main)

    # Calculate correlations
    @st.cache_data
    def calculate_correlations(df):
        return {
            'SO2': df['rain'].corr(df['SO2']),
            'NO2': df['rain'].corr(df['NO2']),
            'CO': df['rain'].corr(df['CO']),
            'O3': df['rain'].corr(df['O3'])
        }

    correlations = calculate_correlations(df_sample)

    # Set up a selectbox for user interaction
    option = st.selectbox(
        'Select pollutant to compare with Rain',
        ('SO2', 'NO2', 'CO', 'O3')
    )

    # Set up a function to display the appropriate plot
    @st.cache_data
    def plot_pollutant_vs_rain(df, pollutant, corr_value):
        scatter = alt.Chart(df).mark_circle(size=60).encode(
            x='rain',
            y=pollutant,    
            tooltip=['rain', pollutant]
        ).properties(
            title=f'Rain vs {pollutant}\nCorrelation: {corr_value:.2f}',
            width=600,
            height=400
        )
        return scatter

    # Plot based on user selection  
    st.altair_chart(plot_pollutant_vs_rain(df_sample, option, correlations[option]))

    st.write(
        """
        Terlihat dari data scatter plot tidak ada hubungannya sama sekali,\n

        - Rain vs SO2 : Bisa dilihat ketika curah hujan tinggi kadang menurunkan, kadang meninggikan dan yang paling mencolok adalah ketika rain tidak hujan tapi SO2 juga bisa mencapai titik terendahnya\n
        - Rain vs CO,NO2,O3 : Juga memiliki argumentasi yang sama seperti Hubungan Rain terhadap SO2
        """
    )

    ### Preparing Function For Question 2 & 3
    # Define the last day
    last_day = pd.Timestamp('2017-02-28 23:00:00')

    # Rename 'PM2.5' to 'PM' in the main DataFrame
    df_main = df_main.rename(columns={"PM2.5": "PM"})

    #Prepare Data For Resampling
    @st.cache_data
    def prepare_pm_data(df):
        df_last_month = df[df['datetime'] >= last_day - pd.DateOffset(months=1)]
        df_last_6_months = df[df['datetime'] >= last_day - pd.DateOffset(months=6)]
        df_last_year = df[df['datetime'] >= last_day - pd.DateOffset(years=1)]
        df_last_5_years = df[df['datetime'] >= last_day - pd.DateOffset(years=5)]

        daily_frequency_df = df_last_month.resample(rule='D', on='datetime').agg({
            "PM": "mean",
            "PM10": "mean"
        }).reset_index()

        weekly_frequency_df = df_last_6_months.resample(rule='W', on='datetime').agg({
            "PM": "mean",
            "PM10": "mean"
        }).reset_index()

        monthly_frequency_df = df_last_year.resample(rule='M', on='datetime').agg({
            "PM": "mean",
            "PM10": "mean"
        }).reset_index()

        yearly_frequency_df = df_last_5_years.resample(rule='Y', on='datetime').agg({
            "PM": "mean",
            "PM10": "mean"
        }).reset_index()

        return daily_frequency_df, weekly_frequency_df, monthly_frequency_df, yearly_frequency_df

    daily_df, weekly_df, monthly_df, yearly_df = prepare_pm_data(df_main)

    ##### Question 2

    #Plot the data
    def plot_pm_data(df, title, x_title):
        chart = alt.Chart(df).mark_line().encode(
            x=alt.X('datetime:T', title=x_title),
            y=alt.Y('PM:Q', title='PM2.5'),
            color=alt.value('blue')
        ).properties(
            title=title,
            width=600,
            height=300  
        )
        return chart

    st.markdown('### 2. Peningkatan Frequency Rata-rata PM2.5')

    st.altair_chart(plot_pm_data(daily_df, 'Last Month (Daily)', 'By Day'))
    st.altair_chart(plot_pm_data(weekly_df, 'Last 6 Months (Weekly)', 'By Week'))
    st.altair_chart(plot_pm_data(monthly_df, 'Last Year (Monthly)', 'By Month'))
    st.altair_chart(plot_pm_data(yearly_df, 'Last 5 Years (Yearly)', 'By Year'))

    st.write(
        """
        Terlihat dari hasil visualisasi analisis, terdapat beberapa hasil yang menarik

        1. Pada data harian di 1 bulan terakhir : tidak nampak pola yang signifikan, namun terlihat **ada 3 kali lonjakan rata-rata nilai PM2.5 diatas 200** nilainya
        2. Pada data mingguan di 6 bulan terakhir : terlihat di data mingguan periode bulan ke-9(September) 2016, terdapat nilai PM2.5 yang dibawah 25, namun setelah itu ada kecenderungan naik, dan puncaknya minggu menjelang awal tahun 2017 ada kenaikan. Lalu turun di minggu kedua bulan januari 2017, **ini menyiratkan kemungkinan polusi berasal dari libur akhir tahun, yang meningkatkan volume penggunaan kereta dan kendaraan lain disekitar stasiun**
        3. Pada data Bulanan di 1 tahun terakhir : terlihat ada nya sedikit pola yang terlihat, yakni mulai dari bulan ke 9 di 2016. Mengonfirmasi visualisasi data sebelumnya di rentang yang sama. **Terlihat ada peningkatan hingga awal tahun lalu melandai kembali**.
        4. Pada data tahunan di 5 tahun terakhir : Terlihat data selama **5 tahun kebelakang tersebar merata** dilihat dari titik terpuncak tahun 2014 hingga titik terendah di tahun 2016 hanya berbeda 12 nilai saja.
        """
    )

    ##### Question 4
    def plot_pm10_data(df, title, x_title):
        chart = alt.Chart(df).mark_line().encode(
            x=alt.X('datetime:T', title=x_title),
            y=alt.Y('PM10:Q', title='PM10'),
            color=alt.value('red')
        ).properties(
            title=title,
            width=600,
            height=300
        )
        return chart

    # Question 3 

    st.markdown('### 3. Peningkatan Frequency Rata-rata PM10')

    st.altair_chart(plot_pm10_data(daily_df, 'Last Month (Daily)', 'By Day'))
    st.altair_chart(plot_pm10_data(weekly_df, 'Last 6 Months (Weekly)', 'By Week'))
    st.altair_chart(plot_pm10_data(monthly_df, 'Last Year (Monthly)', 'By Month'))
    st.altair_chart(plot_pm10_data(yearly_df, 'Last 5 Years (Yearly)', 'By Year'))

    st.write(
        """
        Terlihat dari hasil visualisasi analisis, terdapat beberapa hasil yang cukup identik dari hasil PM2.5.
        Yang paling menarik adalah;

        - pada data bulanan di 1 tahun terakhir terlihat pola yang jelas, bahwa terjadi **siklus naik turun sebanyak 2 kali** dan kondisi titik puncak yang tidak berbeda jauh nilainya.
        """
    )


    # Question 4
    st.markdown('### 4. Bulan dengan jumlah polutan (SO2, NO2, CO, O3) tertinggi')

    @st.cache_data
    def prepare_monthly_data(df):
        df['month'] = df['datetime'].dt.month
        df['month_name'] = df['datetime'].dt.strftime('%B')
        monthly_data = df.groupby('month_name').agg({
            'SO2': 'mean',
            'NO2': 'mean',
            'CO': 'mean',
            'O3': 'mean'
        }).reset_index()
        monthly_data['month_num'] = pd.to_datetime(monthly_data['month_name'], format='%B').dt.month
        monthly_data = monthly_data.sort_values('month_num')
        return monthly_data

    monthly_data = prepare_monthly_data(df_main)

    def plot_monthly_pollutant(data, pollutant):
        chart = alt.Chart(data).mark_bar().encode(
            x=alt.X('month_name:N', title='Month', sort=alt.EncodingSortField(field='month_num')),
            y=alt.Y(f'{pollutant}:Q', title=f'Average {pollutant}'),
            color=alt.Color('month_name:N', legend=None)
        ).properties(
            title=f'Average {pollutant} per Month over 5 Years',
            width=600,
            height=300
        )
        return chart

    pollutants = ['SO2', 'NO2', 'CO', 'O3']


    # Add radio button for pollutant selection
    selected_pollutant = st.radio("Select pollutant:", pollutants)

    # Display chart for the selected pollutant
    st.altair_chart(plot_monthly_pollutant(monthly_data, selected_pollutant))

    st.write(
        """
        Hasil dari visualisasi ini menemukan beberapa fakta baru berdasarkan data yang ada, berikut hasil analisa saya:

        1. Fakta pertama, adalah **3 Polutan(SO2,NO2,CO) sangat memengaruhi O3, terutama hubungan O3 dengan NO2.** Dimana ketika 3 Polutan ini bernilai tinggi, maka O3 berbanding terbalik dengan ketiganya.
        2. Fakta kedua, dalam **periode satu tahun 3 Polutan ini memiliki tren yang sama**, titik terendah di bulan agustus lalu berangsur meningkat pada sekitar bulan Desember - Januari lalu menurun kembali hingga kembali ke agustus.
        3. Fakta ketiga, Untuk **O3 ini terlihat jelas berbanding terbalik dengan ketiganya bahwa titik terendahnya di sekitar bulan November - Desember**, lalu meningkat pada sekitar bulan Juni-Juli
        """
    )

    ### Sidebar
    st.sidebar.caption(
        "Built by [Tito Jhay](https://www.linkedin.com/in/tito-jaya-9b5537201/). Like this? [Hire me!](mailto:mhmmdtjaya@gmail.com)"
    )

    # Define image paths
    linkedin = "https://raw.githubusercontent.com/TitoJhay/Air-Quality-Dicoding-Advance-Analysis/refs/heads/main/img/linkedin.gif"
    dicoding = "https://raw.githubusercontent.com/TitoJhay/Air-Quality-Dicoding-Advance-Analysis/refs/heads/main/img/dicoding.gif"
    email = "https://raw.githubusercontent.com/TitoJhay/Air-Quality-Dicoding-Advance-Analysis/refs/heads/main/img/email.gif"
    share = "https://raw.githubusercontent.com/TitoJhay/Air-Quality-Dicoding-Advance-Analysis/refs/heads/main/img/share.gif"

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