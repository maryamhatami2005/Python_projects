import streamlit as st
from utils.db import DatabaseManager


db = DatabaseManager()


st.title("👤 Profiles")

st.header("Add Profile")

name = st.text_input("Name")
email = st.text_input("Email")
title = st.text_input("Title")
profession = st.text_input("Profession")


if st.button("Add Profile"):

    if not name or not email:
        st.error("Name and Email are required.")

    else:
        db.add_profile(
            name=name,
            email=email,
            title=title,
            profession=profession
        )

        st.success("Profile added successfully.")

        st.rerun()


st.divider()

st.header("Profiles")

profiles = db.get_all_profiles()


if not profiles:
    st.info("No profiles found.")

else:

    for profile in profiles:

        with st.container():

            st.subheader(profile["name"])

            st.write(f"**Email:** {profile['email']}")
            st.write(f"**Title:** {profile['title']}")
            st.write(f"**Profession:** {profile['profession']}")

            if st.button(
                "Delete",
                key=f"delete_{profile.doc_id}"
            ):
                db.delete_profile(profile.doc_id)

                st.success("Profile deleted.")

                st.rerun()

            st.divider()