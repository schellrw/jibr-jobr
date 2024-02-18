"""
LLM to synthesize job descriptions from freeform text.
Uses Salesforce/xgen-7b-8k-inst LLM from Hugging Face.
"""

# ENV variables for config
REPO = "Salesforce/xgen-7b-8k-inst"

# Load packages
import torch
import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load tokenizer and model
@st.cache_data
def load_tokenizer_and_model(repo):
    tokenizer = AutoTokenizer.from_pretrained(
        repo,
        trust_remote_code=True,
    )

    model = AutoModelForCausalLM.from_pretrained(
        repo,
        torch_dtype=torch.bfloat16,
        cache_dir="./.cache/",
        load_in_8bit=True,)
    return tokenizer, model

tokenizer, model = load_tokenizer_and_model(REPO)

# Function to summarize.
@st.cache_data
def summarize(text: str) -> str:
    header = "Application to generate formal job descriptions using Salesforce/xgen LLM for summarization."
    text = header + "### User: Please summarize this into a job description. \n\n" + text + "\n\n###"

    # input_ids = tokenizer(text, return_tensors="pt").input_ids
    inputs = tokenizer(text, return_tensors="pt").input_ids
    outputs = model.generate(
        **inputs, 
        max_length=1024,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True).lstrip()
    # summary = summary.split("### Job Description:")[1]
    # summary = summary.split("<|endoftext|>")[0]

    #synthesis = gr.Textbox(value=summary)
    return summary

# Add title and subtitle to the main interface of the app
st.title("Job Description Synthesis")
st.markdown("#JIBr-JOBr, from Salesforce/xgen LLM")
# st.sidebar.markdown("Email: schell.rw@gmail.com")

st.subheader(":blue[This application takes the messy jibber-jabber and makes it beautiful, with a click of a button.]")
st.subheader(":red[Instanty turn the unedited, free-form, stream-of-consciousness text from a hiring manager into a formal job description that will attract ideal candidates!]")
st.markdown("## Competitive intelligence and easy-to-use technology platforms are just a click away.")

#Add sidebar to the app
st.sidebar.markdown(":blue[Developed at Artificial Intelligentsia, LLC]")
st.sidebar.markdown("## Contact us for Competitive Intelligence Solutions")
st.sidebar.markdown("### https://artificialintelligentsia.com/")
st.sidebar.markdown(":black[This app was built using Python and Streamlit to synthesize job descriptions from freeform text.]")
st.sidebar.markdown(":gray[Developer: Robert W Schell, Data Scientist, Artificial Intelligentsia, LLC]")
st.sidebar.markdown(":gray[Github:    https://github.com/schellrw/]")
st.sidebar.markdown(":gray[LinkedIn:  https://linkedin.com/in/schellr/]")
st.sidebar.markdown(":gray[Special thanks to Salesforce for allowing open source developers to contribute to their LLM model: Salesforce/xgen-7b-8k-inst/ - https://huggingface.co/Salesforce/xgen-7b-8k-inst]")
st.sidebar.markdown(":gray[Proof-of-Concept repository:  https://github.com/schellrw/jibr-jobr]")
st.sidebar.markdown(":gray[Apache 2.0 License, Robert W. Schell, 2024]")
st.sidebar.markdown(":gray[Copyright (c) 2024 Artificial Intelligentsia, LLC]")

#Create two columns
col1, col2 = st.columns(2)

with col1:
    text_input = st.text_area("Paste text here...", height=420)
    submit = st.button("Sythesize")
    if submit:
        job_desc = summarize(text_input)
          
with col2:
    st.write(job_desc)
    st.download_button(
        label="Download summary",
        data=job_desc,
        file_name="job_desc.txt",
        mime="text/plain",
    )

