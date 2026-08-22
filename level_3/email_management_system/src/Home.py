
from pathlib import Path

import streamlit as st

from utils.db import DatabaseManager

st.set_page_config(
    page_title="Email Management System",
    page_icon="✉️",
    layout="wide",
)


db = DatabaseManager()



banner = "/home/mary/project_based_python/projects/level_3/email_management_system/src/utils/banner.jpg"
st.image(
    str(banner),
    use_container_width=True,
)

st.title("✉️ Email Management System (EMS)")

st.subheader(
    "Welcome to your personal automated email manager dashboard!"
)


# Live statistics from TinyDB
total_contacts = len(db.get_all_profiles())
saved_templates = len(db.get_all_templates())
sent_emails = len(db.sent_emails)
scheduled_emails = len(db.get_all_schedules())


# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Total Contacts",
    value=total_contacts,
)

col2.metric(
    label="Saved Templates",
    value=saved_templates,
)

col3.metric(
    label="Sent Emails",
    value=sent_emails,
)

col4.metric(
    label="Scheduled Emails",
    value=scheduled_emails,
)


st.markdown("---")

st.info(
    "Use the sidebar on the left to navigate between recipient "
    "profiles, email templates, sender configuration, and "
    "composing/sending emails."
)
