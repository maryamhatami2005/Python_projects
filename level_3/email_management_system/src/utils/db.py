
from tinydb import Query, TinyDB


class DatabaseManager:
    def __init__(self, db_path="email_manager.json"):
        self.db = TinyDB(db_path)
        self.profiles = self.db.table("profiles")
        self.templates = self.db.table("templates")
        self.sent_emails = self.db.table("sent_emails")
        self.reminders = self.db.table("reminders")
        self.schedules = self.db.table("schedules")
        self.user_profile = self.db.table("user_profile")

    # Profile management
    def add_profile(self, name, email, title, profession):
        return self.profiles.insert({
            "name": name,
            "email": email,
            "title": title,
            "profession": profession,
        })

    def get_profile(self, profile_id):
        return self.profiles.get(doc_id=profile_id)

    def update_profile(self, profile_id, name, email, title, profession):
        self.profiles.update({
            "name": name,
            "email": email,
            "title": title,
            "profession": profession,
        }, doc_ids=profile_id)

    def delete_profile(self, profile_id):
        self.profiles.remove(doc_ids=[profile_id])

    def get_all_profiles(self):
        return self.profiles.all()

    # Email template management
    def add_template(self, name, body):
        return self.templates.insert({
            "name": name,
            "body": body,
        })

    def get_template(self, template_id):
        return self.templates.get(doc_id=template_id)

    def update_template(self, template_id, name, body):
        self.templates.update({
            "name": name,
            "body": body,
        }, doc_ids=[template_id])

    def delete_template(self, template_id):
        self.templates.remove(doc_ids=[template_id])

    def get_all_templates(self):
        return self.templates.all()

    # Sent email management
    def add_sent_email(self, recipients, subject, body, sent_date):
        return self.sent_emails.insert({
            "recipients": recipients,
            "subject": subject,
            "body": body,
            "sent_date": sent_date.isoformat(),
        })

    # Reminder management

    def get_reminder(self, reminder_id):
        return self.reminders.get(doc_id = reminder_id)

    def update_reminder(self, reminder_id, reminder_date):
        self.reminders.update({
            "reminder_date" : reminder_date.isoformat(),
        }, doc_ids=[reminder_id])

    def delete_reminder(self, reminder_id):
        self.reminders.remove(doc_ids=[reminder_id])

    def get_all_reminders(self):
        return self.reminders.all()

    # Schedule management
    def add_schedule(self, email_id, scheduled_date):
        return self.schedules.insert({
            "email_id": email_id,
            "scheduled_date": scheduled_date.isoformat(),
        })

    def get_schedule(self, schedule_id):
        return self.schedules.get(doc_id=schedule_id)

    def update_schedule(self, schedule_id, scheduled_date):
        self.schedules.update({
            "scheduled_date": scheduled_date.isoformat(),
        }, doc_ids=[schedule_id])

    def delete_schedule(self, schedule_id):
        self.schedules.remove(doc_ids=[schedule_id])

    def get_all_schedules(self):
        return self.schedules.all()


    # User profile management
    def get_user_profile(self):
        profiles = self.user_profile.all()
        return profiles[0] if profiles else None

    def update_user_profile(
        self,
        name,
        role,
        position,
        organization,
        social_media,
        signature
    ):
        data = {
            "name": name,
            "role": role,
            "position": position,
            "organization": organization,
            "social_media": social_media,
            "signature": signature,
        }

        profiles = self.user_profile.all()

        if profiles:
            self.user_profile.update(
                data,
                doc_ids=[profiles[0].doc_id]
            )
        else:
            self.user_profile.insert(data)

    def set_user_profile(
        self,
        name,
        role,
        position,
        organization,
        social_media,
        signature
    ):
        self.user_profile.truncate()

        return self.user_profile.insert({
            "name": name,
            "role": role,
            "position": position,
            "organization": organization,
            "social_media": social_media,
            "signature": signature,
        })

    # Search functionality
    def search_sent_email(self, query):
        Email = Query()
        return self.sent_emails.search(
           (Email.recipients.search(query))
           |(Email.subject.search(query))
            |(Email.body.search(query)),
        )
