import streamlit as st
import time
from pygame import mixer  
import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

# Initialize sound mixer
mixer.init()
mixer.music.load("shine-11-268907.mp3")  

# Set page config for title
st.set_page_config(page_title="Unit Converter", page_icon="📏")

# Custom CSS for styling
st.markdown(
    """
    <style>

        /* Set background color and text colors for the main app */
    .stApp {
        background-color: #536878;  
        color: #EAE0C8; 
    }

    /* Style h1 and h2 headings */
    h1 {
        color: #EAE0C8; 
        font-family: 'Arial', sans-serif;
        font-size: 3rem;
        text-align: center;
        animation: fadeIn 2s ease-in-out;
    }
    h2 {
        color: #EAE0C8;  
        font-family: 'Arial', sans-serif;
        font-size: 2rem;
        text-align: center;
        animation: fadeIn 3s ease-in-out;
    }

    /* Style buttons */
    .stButton button {
        background-color: #FF6B6B;  
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #E9FFDB; 
    }

    /* Progress bar styling */
    .stProgress > div > div > div {
        background-image: linear-gradient(to right, #722F37, #EFDFBB); 
    }

    /* Fade-in animation */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: rgba(255, 255, 255, 0.8); 
        color: #EAE0C8; 
    }
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3, .css-1d391kg h4, .css-1d391kg h5, .css-1d391kg h6 {
        color: #EAE0C8; 
    }
    .css-1d391kg .stTextInput input, .css-1d391kg .stSelectbox select {
        background-color: #ffffff;  
        color: #EAE0C8;  
        border: 1px solid #002147;  
    }
    .css-1d391kg .stButton button {
        background-color: #FF6B6B;  
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .css-1d391kg .stButton button:hover {
        background-color: #FF8E8E; 
    }

    /* Style sidebar header */
    .css-1d391kg .stSidebar h2 {
        color: #FF6B6B; 
        font-family: 'Arial', sans-serif;
        font-size: 1.5rem;
        text-align: left;
        margin-bottom: 20px;
    }

    /* Style sidebar select box */
    .css-1d391kg .stSelectbox select {
        background-color: #ffffff;  
        color: #002147; 
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 14px;
        font-weight: bold;
        border: 2px solid #FF6B6B;  
    }
    .css-1d391kg .stSelectbox select:hover {
        border-color: #FF8E8E; 
    }
    .css-1d391kg .stSelectbox select:focus {
        border-color: #FF6B6B;  
        box-shadow: 0 0 5px #FF6B6B; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Length conversion function
def length_converter(value, from_unit, to_unit):
    length_factors = {
        'mm': 1,
        'cm': 10,
        'm': 1000,
        'km': 1000000,
        'inch': 25.4,
        'foot': 304.8,
        'yard': 914.4,
        'mile': 1609344
    }
    value_in_mm = value * length_factors[from_unit]
    converted_value = value_in_mm / length_factors[to_unit]
    return converted_value

# Weight conversion function
def weight_converter(value, from_unit, to_unit):
    weight_factors = {
        'mg': 1,
        'g': 1000,
        'kg': 1000000,
        'ton': 1000000000,
        'ounce': 28349.5,
        'pound': 453592
    }
    value_in_mg = value * weight_factors[from_unit]
    converted_value = value_in_mg / weight_factors[to_unit]
    return converted_value

# Temperature conversion function
def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        else:
            return value
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value

# Main app
def main():
    # Add a fun title with fade-in animation
    st.markdown("<h1>🌟 Unit Converter 📏</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Convert units with passion and style! 🎉</h2>", unsafe_allow_html=True)

    # Add a progress bar for fun
    with st.spinner("Loading your converter... ⏳"):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        st.balloons()  

    # Sidebar for user input
    st.sidebar.header("⚙️ Settings")
    conversion_type = st.sidebar.selectbox(
        "Select Conversion Type",
        ["Length", "Weight", "Temperature"]
    )

    # Main conversion logic
    if conversion_type == "Length":
        st.subheader("📏 Length Converter")
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("Enter value", min_value=0.0, format="%.2f")
            from_unit = st.selectbox("From unit", ["mm", "cm", "m", "km", "inch", "foot", "yard", "mile"])
        with col2:
            to_unit = st.selectbox("To unit", ["mm", "cm", "m", "km", "inch", "foot", "yard", "mile"])
        if st.button("Convert 🚀"):
            with st.spinner("Converting... 🔄"):
                time.sleep(1)  
                result = length_converter(value, from_unit, to_unit)
                mixer.music.play()  
                st.success(f"🎉 {value} {from_unit} = {result:.2f} {to_unit}")
                st.balloons() 
                st.markdown(f"**You're amazing! Keep converting like a pro! 💪**")

    elif conversion_type == "Weight":
        st.subheader("⚖️ Weight Converter")
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("Enter value", min_value=0.0, format="%.2f")
            from_unit = st.selectbox("From unit", ["mg", "g", "kg", "ton", "ounce", "pound"])
        with col2:
            to_unit = st.selectbox("To unit", ["mg", "g", "kg", "ton", "ounce", "pound"])
        if st.button("Convert 🚀"):
            with st.spinner("Converting... 🔄"):
                time.sleep(1)  
                result = weight_converter(value, from_unit, to_unit)
                mixer.music.play()  
                st.success(f"🎉 {value} {from_unit} = {result:.2f} {to_unit}")
                st.balloons() 
                st.markdown(f"**Wow! You're a conversion wizard! 🧙‍♂️**")

    elif conversion_type == "Temperature":
        st.subheader("🌡️ Temperature Converter")
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("Enter value", format="%.2f")
            from_unit = st.selectbox("From unit", ["celsius", "fahrenheit", "kelvin"])
        with col2:
            to_unit = st.selectbox("To unit", ["celsius", "fahrenheit", "kelvin"])
        if st.button("Convert 🚀"):
            with st.spinner("Converting... 🔄"):
                time.sleep(1) 
                result = temperature_converter(value, from_unit, to_unit)
                mixer.music.play()  
                st.success(f"🎉 {value} {from_unit} = {result:.2f} {to_unit}")
                st.balloons() 
                st.markdown(f"**You're on fire! 🔥 Keep it up!**")

    # footer
    st.markdown("---")
    st.markdown("Made with ❤️ by Aeyla Naseer. All rights reserved!")
    st.markdown("🎈 Keep exploring and converting with passion!")

# Run the app
if __name__ == "__main__":
    main()
    
# ------------------------------------------------------THE-END----------------------------------------------------------------