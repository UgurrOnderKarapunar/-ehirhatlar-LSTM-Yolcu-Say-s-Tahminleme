import streamlit as st
from PIL import Image
import pandas as pd
import joblib
import numpy as np
from keras.models import load_model
from datetime import datetime
from sklearn.metrics import mean_squared_error


# Arka plan stili
def add_background(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_path}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Arka plan görselini yükleme (dinamik bir gemi fotoğrafı URL'si)
image_path = "https://sehirhatlari.istanbul/uploads/resim/128-1/sehir-hatlari-kadikoy-vapuru.jpg"  # Buraya gemi fotoğrafınızın URL'sini ekleyin
add_background(image_path)

# Uygulama başlığı ve içerik
st.title("🚢 Yolcu ve Karlılık Tahminleme Modeli 🚢")

# Logo Yükleme
logo_path = r"C:\Users\ugur\Desktop\logo (2).jpg"
try:
    logo = Image.open(logo_path)
    st.sidebar.image(logo, use_column_width=True, caption="Şehirhatları Tahminleme Modeli")
except FileNotFoundError:
    st.sidebar.error("Logo dosyası bulunamadı. Lütfen doğru dosya yolunu kontrol edin.")

# Model ve scaler dosyalarını yükleme
try:
    scaler = joblib.load(r"C:\Users\ugur\PycharmProjects\sehirhatlari\scaler_1000epoch.pkl")
    model = load_model(r"C:\Users\ugur\PycharmProjects\sehirhatlari\best_lstm_model_1000epoch.h5")
    target_scaler = joblib.load(r"C:\Users\ugur\PycharmProjects\sehirhatlari\scaler_target_1000epoch.pkl")
except FileNotFoundError as e:
    st.error(f"Model veya scaler dosyası bulunamadı: {e}")

# Veri seti yükleme
data_path = r"C:\Users\ugur\Desktop\sadece yolcu için.xlsx"
try:
    df = pd.read_excel(data_path)
    df['Sefer Tarihi ve Saati'] = pd.to_datetime(df['Sefer Tarihi ve Saati'], dayfirst=True)
    df.set_index('Sefer Tarihi ve Saati', inplace=True)
except FileNotFoundError:
    st.error("Veri seti dosyası bulunamadı. Lütfen dosya yolunu kontrol edin.")

# Özellikler ve hedefler
features = ['Yakıt Masrafı', 'Saatlik Yolcu Ücreti', "Mil", "Ortalama Kullanılan Yakıt(Lt)",
            "Tek Seferde Kullanılan Toplam Yakıt(Lt)", "Litre Ücreti"]
target = ['Yolcu Sayısı']

# Yan Panel - Hattı Seçimi
st.sidebar.header("🔍 **Filtreler ve Parametreler**")
if 'df' in locals():
    hat_options = df['Hat'].unique()
    selected_hat = st.sidebar.selectbox('Hattı Seçin:', hat_options)

    if selected_hat:
        # Filtrelenmiş veri
        filtered_data = df[df['Hat'] == selected_hat]
        available_dates = filtered_data.index.date
        unique_dates = sorted(pd.Series(available_dates).unique())

        # Tarih girişi
        selected_date = st.sidebar.date_input('Sefer Tarihi:', min_value=min(unique_dates), max_value=max(unique_dates))

        if selected_date:
            daily_data = filtered_data[filtered_data.index.date == selected_date]
            available_times = daily_data.index.time

            # Saat seçimi
            selected_time = st.sidebar.selectbox('Sefer Saati:', sorted(available_times))

            # Kullanıcıdan özelliklerin tamamını alma
            st.sidebar.subheader("⚙️ Özellikler")
            fuel_cost = st.sidebar.number_input('Yakıt Masrafı (₺):', min_value=0.0, key='fuel_cost')
            mileage = st.sidebar.number_input('Mil (km):', min_value=0.0, key='mileage')
            avg_fuel_consumed = st.sidebar.number_input('Ortalama Yakıt (Lt):', min_value=0.0, key='avg_fuel_consumed')
            total_fuel_used = st.sidebar.number_input('Toplam Yakıt (Lt):', min_value=0.0, key='total_fuel_used')
            fuel_cost_per_liter = st.sidebar.number_input('Litre Ücreti (₺):', min_value=0.0, key='fuel_cost_per_liter')
            ticket_price = st.sidebar.number_input('Saatlik Yolcu Ücreti (₺):', min_value=0.0, key='ticket_price')

            # Tahmin Butonu
            if st.sidebar.button('🚀 Tahmin Et'):
                try:
                    # Girdi verilerini birleştir
                    input_data = np.array(
                        [[fuel_cost, ticket_price, mileage, avg_fuel_consumed, total_fuel_used, fuel_cost_per_liter]])
                    input_data = scaler.transform(input_data)
                    input_data = input_data.reshape((1, 1, input_data.shape[1]))

                    # Tahmin yapma
                    predictions = model.predict(input_data)
                    predictions = scaler.inverse_transform(
                        np.concatenate(
                            (predictions, np.zeros((predictions.shape[0], len(features) - predictions.shape[1]))),
                            axis=1)
                    )[:, :2]

                    # Tahmin Sonuçları
                    st.success(f"**Yolcu Sayısı Tahmini:** {predictions[0][0]:.2f}")

                    # RMSE hesaplama
                    real_values = daily_data.loc[daily_data.index.time == selected_time, target].values
                    rmse = np.sqrt(mean_squared_error(real_values, predictions[0]))
                    st.info(f"**RMSE (Hata Payı):** {rmse:.2f}")

                except Exception as e:
                    st.error(f"Bir hata oluştu: {e}")
else:
    st.error("Lütfen veri seti ve model dosyalarını kontrol edin.")
