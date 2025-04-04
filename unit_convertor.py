import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        "meter_meter": 1,
        "kilometer_kilometer": 1,
        "gram_gram": 1,
        "kilogram_kilogram": 1,
        "celsius_fahrenheit": lambda x: (x * 9 / 5) + 32,
        "fahrenheit_celsius": lambda x: (x - 32) * 5 / 9,
        "celsius_kelvin": lambda x: x + 273.15,
        "kelvin_celsius": lambda x: x - 273.15,
        "fahrenheit_kelvin": lambda x: (x - 32) * 5 / 9 + 273.15,
        "kelvin_fahrenheit": lambda x: (x - 273.15) * 9 / 5 + 32,
    }

    key = f"{unit_from}_{unit_to}"

# logic to check if the conversion is valid

    if key in conversions:
        conversion = conversions[key]
        if callable(conversion):
            return conversion(value)
        return value * conversion
    else:
        return "conversion not supported"

# Streamlit app
st.set_page_config(page_title="Unit Convertor", page_icon=":guardsman:", layout="wide")
st.title("Unit Convertor")

value = st.number_input("Enter the Value to Convert", step=1.0)
unit_from = st.selectbox("convert from" , ["meter", "kilometer", "gram", "kilogram ", "celsius", "fahrenheit", "kelvin"])
unit_to = st.selectbox("convert to" , ["meter", "kilometer", "gram", "kilogram ", "celsius", "fahrenheit", "kelvin"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value {result}")