import base64

import streamlit as st
import os
import time
# -----------------------------
# Page Configuration
# -------------
st.set_page_config(page_title="2 Jharkhand air ncc Manager",layout="wide")
# -----------------------------
# Loading Animation
# -----------------------------
def load_gif(gif_file):
    with open(gif_file, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return data
if os.path.exists("assets/loading.gif"):
    gif = load_gif("assets/loading.gif")
    gif_placeholder = st.empty()
    gif_placeholder.markdown(
        f"""
        <div style="
            display:flex;
            justify-content:center;
            align-items:center;
            height:70vh;
        ">
            <img src="data:image/gif;base64,{gif}" width="350">
        </div>
        """,
        unsafe_allow_html=True
    )
    p = st.progress(0, text="NCC Page Loading...")
    for i in range(100):
        time.sleep(0.10)
        p.progress(i + 1, text="NCC Page Loading...")
    p.empty()
    gif_placeholder.empty()
# -----------------------------
# Banner
# -----------------------------
import os

if os.path.exists("assets/banner.png"):
    st.image(
        "assets/banner.png",
        use_container_width=True
    )
else:
    st.error(
        "assets/banner.png not found"
    )
# -----------------------------
# Title
# -----------------------------
st.markdown(
    """
    <h1 style='text-align:center;color:#0A4D68;'>
2 Jharkhand air ncc Manager    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='text-align:center;color:gray;'>
    National Cadet Corps Digital Management Portal
    </h4>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Welcome Section
# -----------------------------
st.markdown("""
### 🎖 Welcome

The NCC Management System is designed to manage:

- 👨‍🎓 Cadet Records
- 📅 Attendance Management
- 🏕 Camp Information
- 🏢 Battalion Information
- 📄 Certificate Generation
- 📊 Reports and Statistics

This platform helps NCC Units digitize their daily operations.
""")

st.divider()

# -----------------------------
# Statistics Section
# -----------------------------
st.subheader("📊 Quick Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Cadets",
        "250"
    )

with col2:
    st.metric(
        "Registrations",
        "200"   
    )

with col3:
    st.metric(
        "Camps Explored",
        "9"
    )

with col4:
    st.metric(
        "Attendance",
        "92%"
    )

st.divider()

# -----------------------------
# Features Section
# -----------------------------
st.subheader("🚀 System Features")

col1, col2 = st.columns(2)

with col1:

    st.success("""
    👨‍🎓 Cadet Management

    Add, Update and Manage Cadet Records
    """)

    st.success("""
    📅 Attendance Management

    Mark and Track Daily Attendance
    """)

    st.success("""
    🏢 Battalion Management

    Manage Battalion Information
    """)

with col2:

    st.info("""
    🏕 Camp Explorer

    Explore RDC, VSC, NIC and other camps
    """)

    st.info("""
    📄 Certificate Generator

    Generate NCC Certificates
    """)

    st.info("""
    📊 Reports & Analytics

    Attendance and Cadet Reports
    """)

st.divider()

# -----------------------------
# Quick Access
# -----------------------------
st.subheader("⚡ Quick Access")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.page_link(
        "pages/cadets.py",
        label="👨‍🎓 Cadets"
    )

with col2:
    st.page_link(
        "pages/attendance.py",
        label="📅 Attendance"
    )

with col3:
    st.page_link(
        "pages/Registration.py",
        label="📝 Registrations"
    )

with col4:
    st.page_link(
        "pages/CampExplorer.py",
        label="🏕 Camps"
    )

st.divider()

# -----------------------------
# NCC Motto
# -----------------------------
st.markdown(
    """
    ## 🎖 NCC Motto

    ### "Unity and Discipline"

    The National Cadet Corps aims at developing
    character, leadership, discipline,
    secular outlook, spirit of adventure
    and ideals of selfless service among youth.
    """
)

st.divider()

# -----------------------------
# About NCC
# -----------------------------
st.subheader("🇮🇳 About NCC")

st.write("""
The National Cadet Corps (NCC) is the youth wing of the
Indian Armed Forces with its headquarters in New Delhi.

NCC provides opportunities to the nation's youth for
their all-round development with a sense of duty,
commitment, dedication, discipline and moral values.
""")

st.divider()

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <div style='text-align:center;color:gray;'>

    © 2026 NCC Management System

    Developed using Streamlit + MongoDB

    </div>
    """,
    unsafe_allow_html=True
)