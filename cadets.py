import streamlit as st
import pandas as pd
from database import cadets
st.title("Cadet Management")
st.subheader("Add New Cadet")
name = st.text_input("Cadet Name")
rank = st.text_input("Rank")
battalion = st.text_input("Battalion")
if st.button("Save Cadet"):
    cadets.insert_one({
        "name": name,
        "rank": rank,
        "battalion": battalion
    })
st.subheader("Search Cadet")
search_name = st.text_input("Enter Cadet Name")
if search_name:
    results = list(cadets.find(
            {"name":
            {
                "$regex": search_name,"$options": "i"
            }
            }
        )
    )

    if results:
        df = pd.DataFrame(results)
        if "_id" in df.columns:
            df = df.drop("_id", axis=1)
        st.dataframe(df)
    else:
        st.warning("No Cadet Found")
st.subheader("Delete Cadet")

delete_name = st.text_input("Cadet Name To Delete")

if st.button("Delete Cadet"):
    result = cadets.delete_one(
        {"name": delete_name}
    )

    if result.deleted_count:
        st.success("Cadet Deleted Successfully")
    else:
        st.error("Cadet Not Found")
st.success("Cadet Added Successfully!")
st.subheader("All Cadets")
data = list(cadets.find())
if data:
    df = pd.DataFrame(data)
    if "_id" in df.columns:
        df = df.drop("_id", axis=1)
    st.dataframe(df)
else:
    st.info("No Cadets Available")
