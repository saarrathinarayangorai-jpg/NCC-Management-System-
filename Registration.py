import streamlit as st
from datetime import date
from database import cadets
st.set_page_config(
    page_title="Cadet Registration",
    layout="wide"
)

st.title("📝 Cadet Registration Form")

with st.form("registration_form"):

    # -----------------------------
    # Personal Details
    # -----------------------------
    st.subheader("👤 Personal Details")

    name = st.text_input("Full Name")
    dob = st.date_input(
        "Date of Birth",
        value=date(2006, 12, 31),
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )

    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    mobile = st.text_input("Mobile Number")
    aadhar = st.text_input("Aadhar Number")

    gender = st.radio(
        "Gender",
        ["Male", "Female"]
    )

    age = st.slider(
        "Age",
        16,
        30,
        18
    )

    nationality = st.selectbox(
        "Nationality",
        ["Indian", "Nepalese", "Bhutanese"]
    )

    blood_group = st.selectbox(
        "Blood Group",
        [
            "A+","A-",
            "B+","B-",
            "AB+","AB-",
            "O+","O-"
        ]
    )

    address = st.text_area("Address")

    # -----------------------------
    # Family Details
    # -----------------------------
    st.subheader("👨‍👩‍👧 Family Details")

    father_name = st.text_input("Father's Name")
    mother_name = st.text_input("Mother's Name")

    # -----------------------------
    # Education Details
    # -----------------------------
    st.subheader("🏫 Educational Details")

    college = st.text_input("Institution / College Name")

    course = st.selectbox(
        "Course",
        [
            "12th Science",
            "12th Commerce",
            "12th Arts",
            "BSc",
            "BCom",
            "BA"
        ]
    )

    # -----------------------------
    # Documents
    # -----------------------------
    st.subheader("📄 Upload Documents")

    profile_photo = st.file_uploader(
        "Upload Profile Photo",
        type=["jpg", "jpeg", "png"]
    )

    fee_receipt = st.file_uploader(
        "Upload Fee Receipt",
        type=["jpg", "jpeg", "png", "pdf"]
    )

    # -----------------------------
    # Submit Button
    # -----------------------------
    submit = st.form_submit_button("Register")

# -----------------------------
# Save Data
# -----------------------------
if submit:

    if not name or not email or not password:
        st.error("Please fill all required fields.")
    
    else:

        existing = cadets.find_one({
            "email": email
        })

        if existing:
            st.error("Email already registered")

        else:

            cadets.insert_one({
                "name": name,
                "dob": str(dob),
                "email": email,
                "password": password,
                "mobile": mobile,
                "aadhar": aadhar,
                "gender": gender,
                "age": age,
                "nationality": nationality,
                "blood_group": blood_group,
                "address": address,
                "father_name": father_name,
                "mother_name": mother_name,
                "college": college,
                "course": course
            })

            st.success(
                f"✅ Registration Successful! Welcome {name}"
            )