import streamlit as st
from utils.db import DatabaseManager


db = DatabaseManager()

st.title("User Profile")


# Get existing profile
profile = db.get_user_profile()

if profile:
    default_name = profile.get("name", "")
    default_job = profile.get("job", "")
    default_position = profile.get("position", "")
    default_place = profile.get("place", "")
    default_social_media = profile.get("social_media", "")
    default_signature = profile.get("signature", "")
else:
    default_name = ""
    default_job = ""
    default_position = ""
    default_place = ""
    default_social_media = ""
    default_signature = ""


with st.form("user_profile_form"):

    name = st.text_input(
        "Name",
        value=default_name,
        placeholder="e.g. Mary"
    )

    role = st.text_input(
        "Role",
        value=default_job,
        placeholder="e.g. Student, Engineer, Teacher"
    )

    position = st.text_input(
        "Position",
        value=default_position,
        placeholder="e.g. Computer Science Student"
    )

    organization = st.text_input(
        "Organization",
        value=default_place,
        placeholder="e.g. University of Tehran"
    )

    social_media = st.text_area(
    "Social Media",
    value=default_social_media,
    placeholder=(
        "LinkedIn: https://linkedin.com/in/yourname\n"
        "GitHub: https://github.com/yourname"
    )
)

    signature = st.text_area(
        "Signature",
        value=default_signature,
        placeholder="Enter your email signature"
    )

    submitted = st.form_submit_button("Save Profile")


if submitted:

    if not name.strip():
        st.error("Name is required.")

    elif not role.strip():
        st.error("Role is required.")

    elif not position.strip():
        st.error("Position is required.")

    elif not organization.strip():
        st.error("Organization of study/work is required.")

    else:
        db.update_user_profile(
            name=name.strip(),
            role=role.strip(),
            position=position.strip(),
            organization=organization.strip(),
            social_media=social_media.strip(),
            signature=signature.strip(),
        )

        st.success("Profile saved successfully.")