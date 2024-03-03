import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='ticks')

# Load the data
days_df = pd.read_csv("https://raw.githubusercontent.com/mhmmadgiatt/Proyek-analisis-data-bike-sharing/main/dashboard/table_day_clean.csv")
hours_df = pd.read_csv("https://raw.githubusercontent.com/mhmmadgiatt/Proyek-analisis-data-bike-sharing/main/dashboard/table_hour_clean.csv")

# Set up the layout
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded",
    
)

# Membuat dua kolom
col1, col2 = st.columns([1, 2])

# Menambahkan Gambar di kolom pertama
col1.image("https://img3.stockfresh.com/files/a/aiel/m/97/2553267_stock-photo-bike-race.jpg", width=300)

# Menambahkan teks di kolom kedua
col2.write("Let's explore the Bike Sharing dataset!!!")

# Fungsi untuk visualisasi data
def get_total_count_by_hour_df(hour_df):
  hour_count_df =  hour_df.groupby(by="hours").agg({"count_cr": ["sum"]})
  return hour_count_df

def count_by_day_df(day_df):
    day_df_count_2011 = day_df.query(str('dteday >= "2011-01-01" and dteday < "2012-12-31"'))
    return day_df_count_2011

def total_registered_df(day_df):
   reg_df =  day_df.groupby(by="dteday").agg({
      "registered": "sum"
    })
   reg_df = reg_df.reset_index()
   reg_df.rename(columns={
        "registered": "register_sum"
    }, inplace=True)
   return reg_df

def total_casual_df(day_df):
   cas_df =  day_df.groupby(by="dteday").agg({
      "casual": ["sum"]
    })
   cas_df = cas_df.reset_index()
   cas_df.rename(columns={
        "casual": "casual_sum"
    }, inplace=True)
   return cas_df

datetime_columns = ["dteday"]
days_df.sort_values(by="dteday", inplace=True)
days_df.reset_index(inplace=True)   

hours_df.sort_values(by="dteday", inplace=True)
hours_df.reset_index(inplace=True)

for column in datetime_columns:
    days_df[column] = pd.to_datetime(days_df[column])
    hours_df[column] = pd.to_datetime(hours_df[column])

min_date_days = days_df["dteday"].min()
max_date_days = days_df["dteday"].max()

min_date_hour = hours_df["dteday"].min()
max_date_hour = hours_df["dteday"].max()


# Membuat sidebar
with st.sidebar:
    
# Menambahkan gambar
    st.image("https://storage.googleapis.com/narasi-production.appspot.com/production/medium/1695012621865/lanjut-musim-kedua-live-action-one-piece-akan-hadirkan-tony-tony-chopper-medium.webp")

# Menambahkan Deskripsi Dashboard
    st.subheader("Hello, Welcome to Bike Sharing Dashboard! 🚲")
    st.write("This dashboard visualizes Bike Sharing data from 2011 to 2012.")
    st.write(" copyrigth by: mhmmadgiatt")
    st.write("Thank you for using this dashboard. Hope you find it useful!")
   
# Menambahkan rentang waktu
    start_date, end_date = st.date_input(
        label='Pilih rentang waktu:',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days])

  
main_df_days = days_df[(days_df["dteday"] >= str(start_date)) & 
                       (days_df["dteday"] <= str(end_date))]

main_df_hour = hours_df[(hours_df["dteday"] >= str(start_date)) & 
                        (hours_df["dteday"] <= str(end_date))]

hour_count_df = get_total_count_by_hour_df(main_df_hour)
day_df_count_2011 = count_by_day_df(main_df_days)
reg_df = total_registered_df(main_df_days)
cas_df = total_casual_df(main_df_days)
rentals_by_day_2011 = pd.Series([10, 15, 20, 25, 30], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
rentals_by_day_2012 = pd.Series([10, 15, 20, 25, 30], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
rentals_by_category = pd.Series({'weekend': 921834.0, 'weekdays': 2370845.0})
rentals_by_month_2011 = pd.Series([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65], index=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
rentals_by_month_2012 = pd.Series([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65], index=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
table_day_df = pd.read_csv("https://raw.githubusercontent.com/mhmmadgiatt/Proyek-analisis-data-bike-sharing/main/dashboard/table_day_clean.csv")

# Membuat Visualisasi data pada dashboard
st.header('Dashboard Dataset Bike Sharing 🚲')

st.subheader('Daily Sharing')
col1, col2, col3 = st.columns(3)
 
with col1:
    total_orders = day_df_count_2011.count_cr.sum()
    st.metric("Total Sharing Bike", value=total_orders)

with col2:
    total_sum = reg_df.register_sum.sum()
    st.metric("Total Registered", value=total_sum)

with col3:
    total_sum = cas_df.casual_sum.sum()
    st.metric("Total Casual", value=total_sum)
    
# Visualisasi Pertanyaan 1
st.subheader("Data Pelanggan terbanyak dalam skala harian pada tahun 2011 dan 2012")
# Buatlah kolom untuk menampilkan visualisasi data
col1, col2 = st.columns(2)

# Memvisualisasikan data tahun 2011 menggunakan barplot dalam kolom pertama
with col1:
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=rentals_by_day_2011.index, y=rentals_by_day_2011.values, color='lightblue')
    ax.set_xlabel('Hari dalam Seminggu')
    ax.set_ylabel('Banyak Pelanggan')
    ax.set_title('Banyak Pelanggan pada Tahun 2011')
    st.pyplot(fig)

# Memvisualisasikan data tahun 2012 menggunakan barplot dalam kolom kedua
with col2:
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=rentals_by_day_2012.index, y=rentals_by_day_2012.values, color='darkblue')
    ax.set_xlabel('Hari dalam Seminggu')
    ax.set_ylabel('Banyak Pelanggan')
    ax.set_title('Banyak Pelanggan pada Tahun 2012')
    st.pyplot(fig)


# Visualisasi Pertanyaan 2
st.subheader("Persentase rata-rata pelanggan perminggunya saat weekdays dan weekend pada tahun 2011 dan 2012")

# Memvisualisasikan data menggunakan pie chart dengan ukuran yang lebih kecil
fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.pie(rentals_by_category, labels=rentals_by_category.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', '#f3797e'])
ax.set_title('Persentase Pelanggan Sepeda Perminggu')
st.pyplot(fig)

# Visualisasi Pertanyaan 3
st.subheader("Pelanggan paling banyak dalam skala bulan pada tahun 2011 dan 2012")

# Buatlah kolom untuk menampilkan visualisasi data
col1, col2 = st.columns(2)

# Memvisualisasikan data pelanggan terbanyak pada tahun 2011
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.barplot(x=rentals_by_month_2011.index, y=rentals_by_month_2011.values, color='lightblue', ax=ax1)
ax1.set_xlabel('Bulan')
ax1.set_ylabel('Jumlah Pelanggan')
ax1.set_title('Banyak Pelanggan pada Tahun 2011')
col1.pyplot(fig1)

# Memvisualisasikan data pelanggan terbanyak pada tahun 2012
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.barplot(x=rentals_by_month_2012.index, y=rentals_by_month_2012.values, color='darkblue', ax=ax2)
ax2.set_xlabel('Bulan')
ax2.set_ylabel('Jumlah Pelanggan')
ax2.set_title('Banyak Pelanggan pada Tahun 2012')
col2.pyplot(fig2)

# Visualisasi Pertanyaan 4
st.subheader(" Rata-rata Temperatur pada saat weekdays dan weekend pada tahun 2011 dan 2012")
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=table_day_df['category_days'], y=table_day_df['temp'], palette='coolwarm')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Rata-rata Temperatur')
plt.title('Rata-rata Temperatur pada Weekdays dan Weekends')
st.pyplot(fig)





