import requests
import streamlit as st

headers = {"Authorization": f"Bearer {st.secrets.API_TOKEN}"}
API_URL = f"https://api-inference.huggingface.co/models/{st.secrets.MODEL}"

@st.cache_data
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Add title and subtitle to the main interface of the app
# st.title("Jibr-Jobr: turn the jibberish into a job description, and more!")
st.title("Jibr-Jobr")
st.subheader(":blue[Job Description Synthesis, at the Click of a Button.]")
st.subheader(":orange[Instanty turn the jibberish into a job description that will attract ideal candidates!]")

#st.markdown("## Competitive intelligence and easy-to-use technology platforms are just a click away.")

# Add sidebar to the app
st.sidebar.markdown("### Contact us for Competitive Intelligence Solutions")
st.sidebar.markdown("#### https://artificialintelligentsia.com/")
st.sidebar.markdown(":blue[Developed at Artificial Intelligentsia, LLC]")
st.sidebar.markdown(":gray[Copyright 2024. Artificial Intelligentsia, LLC.  All rights reserved.]")

col1, col2 = st.columns(2)
with col1:
    text_input = st.text_area("Paste jibberish here...", height=112)
with col2:
    submit = st.button("Sythesize")
    if submit:
        job_desc = query({"inputs": text_input})
        st.write(job_desc)
        st.download_button(
            label="Download summary",
            data=job_desc,
            file_name="summary.txt",
            mime="text/plain",
        )
