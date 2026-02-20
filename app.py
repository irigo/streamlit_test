import streamlit as st

st.title("📁 File Uploader")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.success(f"✅ File uploaded: **{uploaded_file.name}**")
    st.write(f"- **Type:** {uploaded_file.type}")
    st.write(f"- **Size:** {uploaded_file.size} bytes")