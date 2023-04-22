import streamlit as st


st.title("My First WebAPP")

with st.form(key ="my_form"):
    username = st.text_input("Username")
    password = st.text_input("password")
    st.form_submit_button("login")

st.checkbox("Agree")
st.subheader("I love myself")


st.selectbox("gender",["male", "female", "others"])

w = st.sidebar.number_input("how much do you weigh")
h = st.sidebar.number_input("how tall are you in meters")

def bmi_calc(w,h):
    bmi = round(w/(h**2),1)
    return bmi

a1, a2 = st.columns(2)

with a1:
    st.checkbox("Accept")
    st.number_input("how old are you?", step=1)
    st.text_input("what is your name?")
with a2:
        st.checkbox("Reject")
        st.text_area("address")
        st.date_input("date of last visit")

if st.sidebar.button("calculate"):
    st.balloons()
    st.write(bmi_calc(w,h))
    
    



