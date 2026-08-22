from datetime import datetime

import streamlit as st
import yagmail

from utils.db import DatabaseManager

st.set_page_config(
    page_title="Send Email",
    page_icon="✉️",
    layout="wide",
)

db = DatabaseManager()


if "selected_profile_id" not in st.session_state:
    st.session_state.selected_profile_id = None

if "selected_template_id" not in st.session_state:
    st.session_state.selected_template_id = None

if "email_body" not in st.session_state:
    st.session_state.email_body = ""

if "email_subject" not in st.session_state:
    st.session_state.email_subject = ""

if "llm_prompt" not in st.session_state:
    st.session_state.llm_prompt = ""


def personalize_template(body, profile):
    """Replace profile placeholders in an email template."""

    if not profile:
        return body

    replacements = {
        "{name}": profile.get("name", ""),
        "{email}": profile.get("email", ""),
        "{title}": profile.get("title", ""),
        "{profession}": profile.get("profession", ""),
    }

    for placeholder, value in replacements.items():
        body = body.replace(placeholder, value)

    return body


def add_signature(body):
    """Add the sender's saved signature."""

    user_profile = db.get_user_profile()

    if not user_profile:
        return body

    signature = user_profile.get("signature", "")

    if not signature:
        return body

    if signature in body:
        return body

    return f"{body.rstrip()}\n\n{signature}"


st.title("✉️ Send Email")


col1, col2, col3, col4 = st.columns([1, 1, 1, 0.8])


with col1:
    profiles = db.get_all_profiles()

    profile_options = {f"{profile['name']} <{profile['email']}>": profile.doc_id for profile in profiles}

    selected_person = st.selectbox(
        "Select People",
        options=[""] + list(profile_options.keys()),
    )

    if selected_person:
        profile_id = profile_options[selected_person]

        if profile_id != st.session_state.selected_profile_id:
            st.session_state.selected_profile_id = profile_id

            if st.session_state.selected_template_id:
                template = db.get_template(
                    st.session_state.selected_template_id,
                )

                profile = db.get_profile(profile_id)

                if template and profile:
                    st.session_state.email_body = personalize_template(
                        template["body"],
                        profile,
                    )


with col2:
    templates = db.get_all_templates()

    template_options = {template["name"]: template.doc_id for template in templates}

    selected_template = st.selectbox(
        "Select Template",
        options=[""] + list(template_options.keys()),
    )

    if selected_template:
        template_id = template_options[selected_template]

        if template_id != st.session_state.selected_template_id:
            st.session_state.selected_template_id = template_id

            template = db.get_template(template_id)

            profile = None

            if st.session_state.selected_profile_id:
                profile = db.get_profile(
                    st.session_state.selected_profile_id,
                )

            if template:
                body = template["body"]

                if profile:
                    body = personalize_template(
                        body,
                        profile,
                    )

                st.session_state.email_body = body

                st.session_state.email_subject = selected_template


with col3:
    st.write("")

    if st.button(
        "Apply LLM for Improvement",
        use_container_width=True,
    ):
        if not st.session_state.email_body.strip():
            st.warning("There is no email to improve.")

        else:
            # LLM implementation will go here.
            st.info("LLM improvement will be connected here.")


with col4:
    st.write("")

    add_signature_enabled = st.toggle(
        "Add Signature",
        value=False,
    )

    if add_signature_enabled:
        signature = db.get_user_profile()

        if signature:
            signature_text = signature.get(
                "signature",
                "",
            )

            if signature_text and signature_text not in st.session_state.email_body:
                st.session_state.email_body = st.session_state.email_body.rstrip() + "\n\n" + signature_text


st.text_area(
    "LLM Prompt",
    placeholder=("Example: Make this email more professional and concise while preserving its meaning."),
    key="llm_prompt",
)


body_col, preview_col = st.columns(2)


with body_col:
    st.subheader("Email Body")

    st.text_input(
        "Subject",
        key="email_subject",
        placeholder="Email subject",
    )

    st.text_area(
        "Body",
        key="email_body",
        height=400,
        placeholder="Your email will appear here...",
        label_visibility="collapsed",
    )



with preview_col:
    st.subheader("Email Preview")

    profile = None

    if st.session_state.selected_profile_id:
        profile = db.get_profile(
            st.session_state.selected_profile_id,
        )

    if profile:
        st.markdown(
            f"**To:** {profile['name']} <{profile['email']}>",
        )

    else:
        st.markdown("**To:** —")

    st.markdown(
        f"**Subject:** {st.session_state.email_subject or '—'}",
    )

    st.divider()

    if st.session_state.email_body:
        st.markdown(
            st.session_state.email_body.replace(
                "\n",
                "  \n",
            ),
        )

    else:
        st.info("Email preview will appear here.")


st.divider()

send_col, schedule_col, reminder_col = st.columns(3)


with send_col:
    if st.button(
        "Send",
        use_container_width=True,
        type="primary",
    ):
        profile = None

        if st.session_state.selected_profile_id:
            profile = db.get_profile(
                st.session_state.selected_profile_id,
            )

        if not profile:
            st.error("Please select a person.")

        elif not st.session_state.email_subject.strip():
            st.error("Please enter an email subject.")

        elif not st.session_state.email_body.strip():
            st.error("Email body cannot be empty.")

        else:
            try:
                # Get the email content
                email_body = st.session_state.email_body.strip()
                email_subject = st.session_state.email_subject.strip()

                # Add signature if enabled
                if add_signature_enabled:
                    email_body = add_signature(email_body)

                # Connect to Gmail
                yag = yagmail.SMTP(
                    user=st.secrets["EMAIL_ADDRESS"],
                    password=st.secrets["EMAIL_APP_PASSWORD"],
                )

                # Send the actual email
                yag.send(
                    to=profile["email"],
                    subject=email_subject,
                    contents=email_body,
                )

                # Save the successfully sent email to TinyDB
                db.add_sent_email(
                    recipients=profile["email"],
                    subject=email_subject,
                    body=email_body,
                    sent_date=datetime.now(),
                )

                st.success(
                    f"Email sent successfully to {profile['email']}.",
                )

            except Exception as e:
                st.error(
                    f"Failed to send email: {e}",
                )


with schedule_col:
    if st.button(
        "Schedule",
        use_container_width=True,
    ):
        st.info("Scheduling will be implemented here.")


with reminder_col:
    if st.button(
        "Add Reminder",
        use_container_width=True,
    ):
        st.info("Reminder functionality will be implemented here.")
