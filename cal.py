import streamlit as st

st.title = ("BMI calculator")

height = st.slider("Enter your height (in cm):", 100, 250, 175)

weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

bmi = weight / ((height / 100) ** 2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")
st.write("- UnderWeight: Bmi less than 18.5")
st.write("- Normal Weight: Bmi between 18.5 and 24.9")
st.write("- overWeight: Bmi between 25 and 29.9")
st.write("- obesity: Bmi 30 or greator")