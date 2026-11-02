import csv
from pathlib import Path
import win32com.client

# Project folder
PROJECT_FOLDER = Path(__file__).parent
PREVIEW_FILE = PROJECT_FOLDER / "email_preview.csv"

# Recipient email address
RECIPIENT = "pan@cogniquest.ai"


def send_test_email():
    # Check preview file
    if not PREVIEW_FILE.exists():
        print("ERROR: email_preview.csv not found.")
        return

    # Read the first document set
    with PREVIEW_FILE.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:
        reader = csv.DictReader(file)
        row = next(reader, None)

    if row is None:
        print("ERROR: No email records found.")
        return

    # Email subject
    subject = f"[TEST] {row['subject']}"

    # PDF attachments
    attachments = [
        Path(row["attachment1"]),
        Path(row["attachment2"]),
    ]

    # Validate attachments
    for attachment in attachments:
        if not attachment.is_file():
            print(f"ERROR: Attachment not found: {attachment}")
            return

    # Connect to Outlook
    outlook = win32com.client.Dispatch("Outlook.Application")

    # Create email
    mail = outlook.CreateItem(0)
    mail.To = RECIPIENT
    mail.Subject = subject

    # Document owner's name
    document_owner = "Anjali Patil"

    # Email body
    mail.Body = (
        "Hello,\n\n"
        "Please find attached the documents for your review and processing.\n\n"
        "Kindly verify the attached documents and confirm once they have "
        "been received and processed successfully.\n\n"
        "Regards,\n"
        f"{document_owner}"
    )

    # Attach both PDFs
    for attachment in attachments:
        mail.Attachments.Add(str(attachment))

    # Display email details
    print("\n========== TEST EMAIL ==========")
    print(f"To: {mail.To}")
    print(f"Subject: {mail.Subject}")
    print("Attachments:")

    for attachment in attachments:
        print(f"- {attachment.name}")

    # Require confirmation
    confirmation = input(
        "\nType SEND to send this test email, "
        "or anything else to cancel: "
    )

    if confirmation.strip() == "SEND":
        mail.Send()
        print("\nTest email submitted to Outlook.")
    else:
        mail.Close(1)
        print("\nEmail cancelled. Nothing was sent.")


if __name__ == "__main__":
    send_test_email()


#RUN Code
#python send_test_email.py
