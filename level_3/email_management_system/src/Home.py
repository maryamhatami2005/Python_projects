import streamlit as st

st.set_page_config(page_title="Email Management System", page_icon="✉️", layout="wide")

st.title("✉️ Email Management System (EMS)")
st.subheader("Welcome to your personal automated email manager dashboard!")

col1, col2, col3 = st.columns(3)
col1.metric(label="Total Contacts", value="12")
col2.metric(label="Saved Templates", value="5")
col3.metric(label="Scheduled Emails", value="3")

st.markdown("---")
st.info("Use the sidebar on the left to navigate between recipient profiles, email templates, sender configuration, and composing/sending emails.")