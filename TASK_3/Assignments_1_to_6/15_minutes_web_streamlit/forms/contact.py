import streamlit as st 


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_input("Your Message")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            st.success("Your message has been sent!")
            # Here you can add code to send the message to your email or store it in a database.
            
            st.balloons()
            
            