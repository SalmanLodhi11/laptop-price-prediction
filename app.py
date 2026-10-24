
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("laptop_price_model.joblib")

st.set_page_config(
    page_title="Laptop Price Prediction",
    page_icon="💻",
    layout="centered"
)

st.title("💻 Laptop Price Prediction System")

st.write(
    "Enter the specifications of your laptop "
    "to estimate its price in euros."
)

# Laptop details form
with st.form("laptop_form"):

    company = st.selectbox(
        "Company",
        ["Apple", "HP", "Dell", "Lenovo", "Asus",
         "Acer", "MSI", "Toshiba", "Samsung", "Other"]
    )

    product = st.text_input(
        "Product / Model",
        value="MacBook Pro"
    )

    typename = st.selectbox(
        "Laptop Type",
        ["Notebook", "Ultrabook", "Gaming",
         "2 in 1 Convertible", "Workstation", "Other"]
    )

    inches = st.number_input(
        "Screen Size (inches)",
        min_value=10.0,
        max_value=20.0,
        value=15.6,
        step=0.1
    )

    screen_resolution = st.text_input(
        "Screen Resolution",
        value="Full HD 1920x1080"
    )

    cpu = st.text_input(
        "CPU",
        value="Intel Core i5 7200U 2.5GHz"
    )

    ram = st.selectbox(
        "RAM",
        ["4GB", "8GB", "12GB", "16GB", "24GB", "32GB", "64GB"]
    )

    memory = st.text_input(
        "Storage",
        value="256GB SSD"
    )

    gpu = st.text_input(
        "GPU",
        value="Intel HD Graphics 620"
    )

    opsys = st.selectbox(
        "Operating System",
        ["Windows 10", "Windows 11", "macOS",
         "Mac OS X", "Linux", "No OS", "Other"]
    )

    weight = st.text_input(
        "Weight",
        value="1.86kg"
    )

    submitted = st.form_submit_button("Predict Laptop Price")

if submitted:

    # Use the exact feature names used during training
    input_data = pd.DataFrame([{
        "Company": company,
        "Product": product,
        "TypeName": typename,
        "Inches": inches,
        "ScreenResolution": screen_resolution,
        "Cpu": cpu,
        "Ram": ram,
        "Memory": memory,
        "Gpu": gpu,
        "OpSys": opsys,
        "Weight": weight
    }])

    try:
        prediction = model.predict(input_data)[0]

        st.success(
            f"Estimated Laptop Price: €{prediction:,.2f}"
        )

        st.caption(
            "This is a machine learning estimate, "
            "not a guaranteed market price."
        )

    except Exception as error:
        st.error(f"Prediction failed: {error}")
