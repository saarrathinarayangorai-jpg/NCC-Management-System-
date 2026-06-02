import streamlit as st
from database import cadets

st.set_page_config(
    page_title="Cadet Profile",
    layout="wide"
)

st.title("👤 Cadet Profile")

# -----------------------------
# Search Cadet
# -----------------------------
email = st.text_input(
    "Enter Registered Email"
)

if st.button("Load Profile"):

    cadet = cadets.find_one({
        "email": email
    })

    if cadet:
        st.session_state.cadet = cadet
    else:
        st.error("Cadet not found")

# -----------------------------
# Display Profile
# -----------------------------
if "cadet" in st.session_state:

    cadet = st.session_state.cadet

    st.subheader("👤 Personal Details")

    name = st.text_input(
        "Full Name",
        value=cadet.get("name", "")
    )

    mobile = st.text_input(
        "Mobile Number",
        value=cadet.get("mobile", "")
    )

    aadhar = st.text_input(
        "Aadhar Number",
        value=cadet.get("aadhar", "")
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
        index=0 if cadet.get("gender", "Male") == "Male" else 1
    )

    age = st.number_input(
        "Age",
        min_value=16,
        max_value=30,
        value=int(cadet.get("age", 18))
    )

    nationality = st.selectbox(
        "Nationality",
        ["Indian", "Nepalese", "Bhutanese"],
        index=["Indian", "Nepalese", "Bhutanese"].index(
            cadet.get("nationality", "Indian")
        )
    )

    blood_group = st.selectbox(
        "Blood Group",
        ["A+","A-","B+","B-","AB+","AB-","O+","O-"],
        index=["A+","A-","B+","B-","AB+","AB-","O+","O-"].index(
            cadet.get("blood_group", "A+")
        )
    )

    address = st.text_area(
        "Address",
        value=cadet.get("address", "")
    )

    st.subheader("👨‍👩‍👧 Family Details")

    father_name = st.text_input(
        "Father's Name",
        value=cadet.get("father_name", "")
    )

    mother_name = st.text_input(
        "Mother's Name",
        value=cadet.get("mother_name", "")
    )

    st.subheader("🏫 Educational Details")

    college = st.text_input(
        "Institution / College",
        value=cadet.get("college", "")
    )

    course = st.selectbox(
        "Course",
        [
            "12th Science",
            "12th Commerce",
            "12th Arts",
            "BSc",
            "BCom",
            "BA"
        ],
        index=[
            "12th Science",
            "12th Commerce",
            "12th Arts",
            "BSc",
            "BCom",
            "BA"
        ].index(
            cadet.get("course", "BSc")
        )
    )

    # -----------------------------
    # Update Button
    # -----------------------------
    if st.button("💾 Update Profile"):

        cadets.update_one(
            {
                "email": cadet["email"]
            },
            {
                "$set": {
                    "name": name,
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
                }
            }
        )

        st.success(
            "✅ Profile Updated Successfully"
        )

        # Reload latest data
        st.session_state.cadet = cadets.find_one(
            {"email": cadet["email"]}
        )