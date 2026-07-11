import streamlit as st
import pickle
try:
    with open("weather_model.pkl", "rb") as f:
    model = pickle.load(f)
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()
st.set_page_config(
    page_title="Smart Weather Predictor",
    page_icon="🌦️",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#5BC0EB,#3A86FF);
}
</style>
""", unsafe_allow_html=True)

st.title("🌦️ Smart Weather Predictor")
st.write("Enter current weather details and get predictions & recommendations.")
col1,col2 = st.columns(2)
with col1:
    precipitation = st.number_input("Precipitation (mm)", min_value=0.0, value=0.0)

with col2:
    wind_speed = st.number_input(
        "Wind Speed (km/h)",
        value=10.0
    )
    col3, col4 = st.columns(2)

with col3:
   temp_max = st.number_input("Maximum Temperature (°C)", value=25.0)
with col4:
    temp_min = st.number_input("Minimum Temperature (°C)", value=15.0)
    
predict = st.button("🔮 Predict Weather")
if predict:
    prediction = model.predict([[precipitation, temp_max, temp_min, wind_speed]])
    weather = prediction[0]

    st.write("Prediction:", weather)

    if weather == "sun":
        st.markdown("""
        <div style="background:#FFD54F;padding:40px;border-radius:20px;text-align:center;color:black;">
            <h1>☀️</h1>
            <h2>Sunny</h2>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("🎒 What to Carry")
        st.write("""
        - 🕶️ Sunglasses
        - 🧴 Sunscreen
        - 💧 Water Bottle
        - 🧢 Cap or Hat
✔️ Apply sunscreen.
        ✔️ Avoid direct sunlight in the afternoon.
        """)

    elif weather == "rain":
        st.markdown("""
        <div style="background:#90CAF9;padding:40px;border-radius:20px;text-align:center;color:black;">
            <h1>🌦️</h1>
            <h2>Rainy</h2>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("🎒 What to Carry")
        st.write("""
        - ☂️ Umbrella
        - 🧥 Light Jacket
        """)

        st.subheader("🏥 Health Update")
        st.success("""
        ✔️ Weather is pleasant.
        ✔️ Keep an umbrella if needed.
        """)

    elif weather == "drizzle":
        st.markdown("""
        <div style="background:#87CEFA;padding:40px;border-radius:20px;text-align:center;color:black;">
            <h1>🌦️</h1>
            <h2>Drizzle</h2>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("🎒 What to Carry")
        st.write("""
        - ☂️ Umbrella
        - 🧥 Light Jacket
        """)

        st.subheader("🏥 Health Update")
        st.success("""
        ✔️ Roads may be slippery.
        ✔️ Keep yourself dry.
        """)
