import streamlit as st

st.set_page_config(page_title="NCC Camp Explorer",layout="wide")

# -----------------------------
# Banner
# -----------------------------

try:
    st.image("assets/camp_banner.jpg", use_container_width=True)
except:
    pass

st.title("🏕 NCC Air Wing Camp Explorer")

st.markdown("""
Explore Air Wing NCC camps, eligibility,
selection procedures, benefits, achievements,
and opportunities available for cadets.
""")

# -----------------------------
# Statistics
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Camps", 9)

with col2:
    st.metric("National Camps", 4)

with col3:
    st.metric("Adventure Camps", 2)

# -----------------------------
# Search
# -----------------------------

search = st.text_input(
    "🔍 Search Camp"
)

# -----------------------------
# Camp Data
# -----------------------------

camp_data = {

    "RDC": {
        "image": "assets/rdc.jpg",
        "title": "Republic Day Camp (RDC)",
        "location": "New Delhi",
        "duration": "30 Days",
        "eligibility": "Best Senior Division/Senior Wing Cadets",
        "selection": "Battalion → Group → Directorate → RDC",
        "benefits": "PM Rally, Republic Day Parade, National Recognition",
        "description": """
Republic Day Camp is the most prestigious NCC camp.
Cadets from across India participate after several
selection stages and represent their directorates.
""",
        "achievements": [
            "PM Rally Participation",
            "Republic Day Parade",
            "Best Cadet Competition",
            "Cultural Events"
        ]
    },

    "VSC": {
        "image": "assets/vsc.jpg",
        "title": "Vayu Sainik Camp",
        "location": "Air Force Station",
        "duration": "12 Days",
        "eligibility": "Air Wing Cadets",
        "selection": "Unit → Group → Directorate",
        "benefits": "Air Force Exposure",
        "description": "National level Air Wing camp.",
        "achievements": [
            "Flying Subjects",
            "Aircraft Recognition",
            "Drill Competition"
        ]
    },

    "NIC": {
        "image": "assets/nic.jpg",
        "title": "National Integration Camp",
        "location": "Various States",
        "duration": "10 Days",
        "eligibility": "All NCC Cadets",
        "selection": "Unit Recommendation",
        "benefits": "Cultural Exchange",
        "description": "Promotes national unity and cultural understanding.",
        "achievements": [
            "Cultural Exchange",
            "Leadership Development"
        ]
    },

    "EBSB": {
        "image": "assets/ebsb.jpg",
        "title": "Ek Bharat Shreshtha Bharat",
        "location": "Different States",
        "duration": "10 Days",
        "eligibility": "All NCC Cadets",
        "selection": "Directorate Selection",
        "benefits": "Inter-State Exposure",
        "description": "Promotes cultural integration between states.",
        "achievements": [
            "State Exchange",
            "Cultural Programs"
        ]
    },

    "AFAC": {
        "image": "assets/afac.jpg",
        "title": "Air Force Attachment Camp",
        "location": "Air Force Stations",
        "duration": "7 Days",
        "eligibility": "Air Wing Cadets",
        "selection": "Unit Selection",
        "benefits": "Military Aviation Exposure",
        "description": "Hands-on exposure to Air Force operations.",
        "achievements": [
            "Aircraft Visit",
            "Technical Knowledge"
        ]
    },

    "CATC": {
        "image": "assets/catc.jpg",
        "title": "Combined Annual Training Camp",
        "location": "Camp Ground",
        "duration": "10 Days",
        "eligibility": "All NCC Cadets",
        "selection": "Unit Selection",
        "benefits": "Military Training",
        "description": "Combined training for cadets.",
        "achievements": [
            "Weapon Training",
            "Leadership Training"
        ]
    },

    "ATC": {
        "image": "assets/atc.jpg",
        "title": "Annual Training Camp",
        "location": "Training Area",
        "duration": "10 Days",
        "eligibility": "All NCC Cadets",
        "selection": "Unit Selection",
        "benefits": "Basic NCC Training",
        "description": "Foundation training camp for cadets.",
        "achievements": [
            "Drill",
            "Field Craft"
        ]
    },

    "Aero Modelling": {
        "image": "assets/aeromodelling.jpg",
        "title": "Aero Modelling Camp",
        "location": "Training Centre",
        "duration": "7 Days",
        "eligibility": "Air Wing Cadets",
        "selection": "Unit Recommendation",
        "benefits": "Aircraft Design Knowledge",
        "description": "Learn principles of aircraft design and flight.",
        "achievements": [
            "Model Aircraft Building",
            "Flying Models"
        ]
    },

    "Para Sailing": {
        "image": "assets/parasailing.jpg",
        "title": "Para Sailing Camp",
        "location": "Adventure Camp",
        "duration": "5 Days",
        "eligibility": "Physically Fit Cadets",
        "selection": "Unit Recommendation",
        "benefits": "Adventure Experience",
        "description": "Exciting air adventure activity.",
        "achievements": [
            "Parasailing Experience",
            "Confidence Building"
        ]
    }
}

# -----------------------------
# Camp Buttons
# -----------------------------

st.subheader("Select a Camp")

cols = st.columns(3)

camp_names = list(camp_data.keys())

for i, camp in enumerate(camp_names):
    with cols[i % 3]:
        if st.button(camp, use_container_width=True):
            st.session_state.selected_camp = camp

# Search Logic

if search:
    for camp in camp_data:
        if search.lower() in camp.lower():
            st.session_state.selected_camp = camp

# -----------------------------
# Show Details
# -----------------------------

if "selected_camp" in st.session_state:

    camp = camp_data[st.session_state.selected_camp]

    st.divider()

    st.header(camp["title"])

    try:
        st.image(camp["image"], use_container_width=True)
    except:
        st.warning("Camp image not found.")

    st.subheader("📍 Location")
    st.write(camp["location"])

    st.subheader("⏳ Duration")
    st.write(camp["duration"])

    st.subheader("✅ Eligibility")
    st.write(camp["eligibility"])

    st.subheader("🎯 Selection Process")
    st.write(camp["selection"])

    st.subheader("🏆 Benefits")
    st.write(camp["benefits"])

    st.subheader("📖 About Camp")
    st.write(camp["description"])

    st.subheader("🌟 Achievements")

    for item in camp["achievements"]:
        st.write("✔", item)