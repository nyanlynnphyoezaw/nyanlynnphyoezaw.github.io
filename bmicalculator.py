import streamlit as st
st.title("BMI Calculator")
weight = st.number_input("Enter your weight in KG")
selected_option = st.radio('', ['m', 'cm', 'feet'])
if selected_option == 'm':
    height = st.number_input("Enter your height")
    height=height
    try:
        bmi = weight / (height * height)
    except:
        st.write('')

elif selected_option == 'cm':
    height = st.number_input("Enter your height")
    height=height/100
    try:
        bmi = weight / (height * height)
    except:
        st.write('')

elif selected_option == 'feet':
    height = st.number_input("Enter your height")
    height=height*.3048
    try:
        bmi = weight / (height * height)
    except:
        st.write('')

if (st.button('Calculate')):
    st.write("Your BMI is",bmi)

    if bmi < 18.5:
        st.text("Underweight")
    elif bmi < 24.9:
        st.text("Normal Weight")
    elif bmi < 29.9:
        st.text("Overweight")
    elif bmi < 34.9:
        st.text("Obesity class 1")
    elif bmi < 39.9:
        st.text("Obesity Class 2")



import streamlit as st
# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

