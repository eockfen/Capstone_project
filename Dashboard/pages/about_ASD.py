import streamlit as st
import utils as ut

# load default style settings
ut.default_style()

# sidebar menu
ut.create_menu()

st.title("About ASD")
st.markdown("---")

# Introduction to ASD
st.write("""
Autism Spectrum Disorder (ASD) is a complex neurodevelopmental condition characterized by challenges in social interaction, communication, and repetitive behaviors. ASD encompasses a spectrum of symptoms and severity levels, hence the term "spectrum."

Individuals with ASD may exhibit a wide range of strengths and difficulties. Some may excel in specific areas such as mathematics or music, while others may struggle with everyday tasks that involve social interaction or sensory processing.
""")




# Use expander to create collapsible text

# Gaze Patterns in Eye-Tracking Studies
st.write("""
### **Gaze Patterns in Eye-Tracking Studies** ###

Eye-tracking studies have provided valuable insights into understanding the unique gaze patterns of individuals with ASD. These studies involve monitoring and analyzing where individuals look (gaze) and for how long, using specialized equipment that tracks eye movements.
""")


with st.expander("**Atypical Gaze Behavior**"):
    st.write("""
        Individuals with ASD often exhibit atypical gaze behavior compared to neurotypical individuals. This includes differences in how they distribute their gaze across social and nonsocial stimuli.
    """)
st.text("")
with st.expander("**Reduced Eye Contact**"):
    st.write("""
        One of the hallmark characteristics of ASD is reduced eye contact. Individuals with ASD may avoid or have difficulty maintaining eye contact during social interactions, which can impact communication and social bonding.
    """)
st.text("")
with st.expander("**Preference for Nonsocial Stimuli**"):
    st.write("""
        Eye-tracking studies have shown that individuals with ASD may demonstrate a preference for nonsocial stimuli, such as objects or patterns, over social stimuli like faces or facial expressions. This preference may contribute to challenges in social communication and interaction.
    """)
st.text("")
with st.expander("**Focus on Specific Features**"):
    st.write("""
        When individuals with ASD do engage with social stimuli, they may focus more on specific features rather than the whole picture. For example, they may focus on the mouth rather than the eyes when looking at faces, which can affect their ability to interpret social cues accurately.
    """)
st.text("")
with st.expander("**Variability Across Individuals**"):
    st.write("""
        It's important to note that gaze patterns can vary widely among individuals with ASD. Factors such as age, cognitive abilities, and co-occurring conditions can influence gaze behavior, leading to a diverse range of responses in eye-tracking studies.
    """)
st.text("")
st.write('Understanding the gaze patterns of individuals with ASD can aid researchers and clinicians in developing tailored interventions and support strategies to enhance social communication skills and improve quality of life.')
# """)