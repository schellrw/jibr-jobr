import requests
import streamlit as st

headers = {"Authorization": f"Bearer {st.secrets.API_TOKEN}"}
        # [{"Context":"Please summarize this into a job description."}]
API_URL = f"https://api-inference.huggingface.co/models/{st.secrets.MODEL}"

@st.cache_data
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Add title and subtitle to the main interface of the app
st.title("Jibr-Jobr")
st.markdown(":blue[Turn the jibberish into a job description at the click of a button]")

# Add sidebar to the app
st.sidebar.markdown("### :blue[Competitive Intelligence Solutions]")
st.sidebar.markdown("##### :gray[Copyright 2024. Artificial Intelligentsia, LLC.]")
st.sidebar.markdown("##### :gray[All rights reserved.]")

col1, col2 = st.columns(2)
with col1:
    text_input = st.text_area("Paste some job jibberish here...", height=420)
    text_input = text_input + "\n\nPlease summarize that into a formal job description."
with col2:
    submit = st.button("Synthesize")
    if text_input and submit:
        job_desc = query({"inputs": text_input})
        job_desc = st.write(job_desc, height=420, label="GENERATED JOB DESCRIPTION:")
        # st.text_area(job_desc, height=420, label="GENERATED JOB DESCRIPTION:")

        # st.download_button(
        #     label="Download summary",
        #     data=job_desc,
        #     file_name="summary.txt",
        #     mime="text/plain",
        # )
