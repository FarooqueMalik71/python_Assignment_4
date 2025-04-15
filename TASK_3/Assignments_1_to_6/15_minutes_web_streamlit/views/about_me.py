import streamlit as st 
from forms.contact import contact_form





@st.dialog("Contact Me")
def show_contact_form():
    contact_form()
    
    
    
    
col1 , col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile-pic.png", width=550)
with col2:
      

    st.title("Farooque Malik", anchor=False)
    st.write(
        """I am a student at GIAIC, pursuing a course in Artificial Intelligence, Web 3.0, and the Metaverse. Passionate about technology, I am constantly learning new skills to stay up-to-date with the latest innovations.

    My journey in the tech world is driven by curiosity and a strong desire to create impactful solutions. I have hands-on experience in web development and enjoy exploring emerging fields like blockchain, augmented reality, and machine learning.

    Dedicated to personal growth, I thrive on challenges that push my limits. My goal is to contribute meaningfully to the tech community and make a positive difference through innovation and creativity.
        """
    )
    if st.button("📨 Contact Me"):
        show_contact_form()
    
    
    # Experience
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    -    Bachelor Degree
            2015 - 2016

    -    University of Sindh

    -    Intermediate
            2013 - 2014

    -    Shah Abdul Latif College

    -    Matric
            2012

    -   High School
    
    """
    )

    # Skills
    
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    -    HTML       ****************** 90%
          
    -    CSS        ****************** 85%

    -    JavaScript ****************** 85%
    
    -    TypeScript ****************** 80%

    -    React.js   ****************** 85%

    -    Next.js   ****************** 90%
    
    -    Tailwind   ****************** 95%
    
    -    Node.js   ****************** 95%
    
    -    Python   ****************** 40%
    



    """
    )