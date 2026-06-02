import streamlit as st
from database import cadets

st.title("NCC Dashboard")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Cadets",cadets.count_documents({}))
with col2:
    st.metric("Total Registered Cadets", cadets.count_documents({"is_registered": True}))
