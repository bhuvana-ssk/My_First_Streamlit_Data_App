import base64
import streamlit as st
st.title('Hello, EveryOne!')
st.title('Welcome to My Data App! :smile:')
st.snow()
st.header("I am Bhuvana Senthilkumar :sunglasses:")
st.subheader("MSEC'24 | Aritificial Intelligence and Data Science | Data Science Intern @ Innomatics Research Lab")

def displayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="900" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
btn_click = st.button("Click to know about Me!")

if btn_click == True:
    displayPDF("Bhuvana_Resume.pdf")