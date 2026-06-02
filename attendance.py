import streamlit as st
import pandas as pd
from datetime import date
from database import attendance

st.set_page_config(
    page_title="Attendance Management",
    layout="wide"
)

st.title("📅 NCC Attendance Management")

# -----------------------------
# Select Date
# -----------------------------
attendance_date = st.date_input(
    "Select Attendance Date",
    date.today()
)

# -----------------------------
# Upload Excel File
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Cadet Excel File",
    type=["xlsx"]
)

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    st.success("Cadet List Loaded Successfully")

    st.subheader("Mark Attendance")

    present_cadets = []

    for index, row in df.iterrows():

        cadet_name = row["Cadet Name"]
        regimental_No = row["Regimental No"]

        is_present = st.checkbox(
            f"{cadet_name} ({regimental_No})",
            key=f"cadet_{index}"
        )

        if is_present:
            present_cadets.append(f"{cadet_name} ({regimental_No})")

    if st.button("Save Attendance"):

        for index, row in df.iterrows():

            cadet_name = row["Cadet Name"]
            regimental_No = row["Regimental No"]

            status = (
                "Present"
                if f"{cadet_name} ({regimental_No})" in present_cadets
                else "Absent"
            )

            attendance.insert_one({
                "cadet_name": cadet_name,
                "regimental_No": regimental_No,
                "date": str(attendance_date),
                "status": status
            })

        st.success(
            "Attendance Saved Successfully"
        )

# -----------------------------
# View Attendance Records
# -----------------------------
st.divider()

st.subheader("Attendance Records")

records = list(attendance.find())

if records:

    attendance_df = pd.DataFrame(records)

    if "_id" in attendance_df.columns:
        attendance_df.drop(
            "_id",
            axis=1,
            inplace=True
        )

    st.dataframe(
        attendance_df,
        use_container_width=True
    )
# -----------------------------
# View Attendance by Date
# -----------------------------

st.divider()

st.subheader("📅 View Attendance by Date")

search_date = st.date_input(
    "Select Date to View Attendance",
    key="search_date"
)

if st.button("Show Attendance"):

    result = list(
        attendance.find({
            "date": str(search_date)
        })
    )

    if result:

        df = pd.DataFrame(result)

        if "_id" in df.columns:
            df = df.drop("_id", axis=1)

        st.success(
            f"Attendance Records for {search_date}"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        # Statistics
        present_count = len(
            [x for x in result if x["status"] == "Present"]
        )

        absent_count = len(
            [x for x in result if x["status"] == "Absent"]
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Present",
                present_count
            )

        with col2:
            st.metric(
                "Absent",
                absent_count
            )

    else:

        st.warning(
            "No Attendance Records Found For This Date"
        )