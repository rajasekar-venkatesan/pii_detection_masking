"""
Streamlit frontend for PDM model
"""

# Imports
import streamlit as st
from pdm import pdm_model, ENTITIES_OF_INTEREST


# Main
"""
# PDM - PII Detection and Masking

## PII Entities
"""
text = "My name is Rajasekar Venkatesan and my phone number is +6597720584. I live in Singapore but I am from Tamil Nadu, India. I'm an Indian and Hindu. My GPU machine's local address is 192.162.18.9 and my email address is rajasekar_venkatesan@singaporeair.com.sg. I'm working on a search project for www.singaporeair.com.sg for about 2 months 12 days and 6 hours as of 04:30 PM today. My credit card number is 4119-1101-0319-4913 and my FIN number is G1162042N. Model is intelligent enough to not recognize fake credit card number like 4123-4567-8901-2345."
entities_of_interest = st.multiselect("Select the entities to be detected: ", ENTITIES_OF_INTEREST, ENTITIES_OF_INTEREST)
text = st.text_area("Enter text: ", text)
result = pdm_model.predict(text, entities_of_interest)
st.write(f'Time to Analyze text: {result["time_to_analyze"]}')
st.write(f'Time to Anonymize text: {result["time_to_anonymize"]}')
st.header('Anonymized Text')
st.write(result["anonymized_text"])
