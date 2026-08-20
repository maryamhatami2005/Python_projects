import streamlit as st

from utils.db import DatabaseManager

# Initialize database

db = DatabaseManager()

st.title("📄 Email Templates")

# Add new templ

st.subheader("Add New Template")

with st.form("template_form", clear_on_submit=True):

    template_name = st.text_input(
        "Template Name",
        placeholder="e.g., Job Application",
    )

    template_body = st.text_area(
        "Email Body",
        placeholder="Dear {title} {name},\n\nI am writing to...",
        height=200,
    )

    submit_button = st.form_submit_button("Add Template")

    if submit_button:

        if template_name.strip() and template_body.strip():

            db.add_template(
                template_name.strip(),
                template_body.strip(),
            )

            st.success(
                f"Template '{template_name}' added successfully!",
            )

            st.rerun()

        else:
            st.error(
                "Please provide both a title and a body for the template.",
            )


st.divider()



# Show templs

st.subheader("Existing Templates")

templates = db.get_all_templates()

if not templates:

    st.info(
        "No templates found. Create your first one above!",
    )

else:

    for template in templates:

        template_id = template.doc_id
        template_name = template.get("name", "Untitled")
        template_body = template.get("body", "")

        with st.expander(f"Title: {template_name}"):

            st.text_area(
                "Email Body",
                value=template_body,
                height=200,
                disabled=True,
                key=f"body_{template_id}",
            )

            if st.button(
                "Delete",
                key=f"del_{template_id}",
            ):

                db.delete_template(template_id)

                st.success(
                    f"Template '{template_name}' deleted.",
                )

                st.rerun()
