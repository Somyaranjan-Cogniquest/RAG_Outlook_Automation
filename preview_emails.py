import csv
from pathlib import Path

# Main folder containing all category folders
ROOT_FOLDER = Path(
    r"C:\Users\ADMIN\Downloads\PAN_2.0_KYC_Doc_set_Synthetic_1300"
    r"\PAN 2.0 KYC Doc set\PAN 2.0 doc sets"
)

# Email details
RECIPIENT = "pan@cogniquest.ai"

# CSV preview will be saved in the project folder
OUTPUT_FILE = Path(__file__).parent / "email_preview.csv"


def generate_preview():
    if not ROOT_FOLDER.exists():
        print(f"ERROR: Folder not found: {ROOT_FOLDER}")
        return

    email_rows = []
    review_required = []

    # Find all category folders
    category_folders = sorted(
        [folder for folder in ROOT_FOLDER.iterdir() if folder.is_dir()]
    )

    for category_folder in category_folders:

        # Find numbered document-set folders
        subfolders = sorted(
            [folder for folder in category_folder.iterdir() if folder.is_dir()]
        )

        for subfolder in subfolders:

            # Find PDF attachments
            pdf_files = sorted(subfolder.glob("*.pdf"))

            # Include only folders containing exactly two PDFs
            if len(pdf_files) != 2:
                review_required.append(str(subfolder))
                continue

            # Email subject: Category name - Document set number
            subject = f"{category_folder.name} - {subfolder.name}"

            # Add email details to the preview
            email_rows.append({
                "category": category_folder.name,
                "subfolder": subfolder.name,
                "recipient": RECIPIENT,
                "subject": subject,
                "attachment1": str(pdf_files[0]),
                "attachment2": str(pdf_files[1]),
                "attachment_count": len(pdf_files),
            })

    # CSV column names
    fieldnames = [
        "category",
        "subfolder",
        "recipient",
        "subject",
        "attachment1",
        "attachment2",
        "attachment_count",
    ]

    # Generate CSV preview
    with OUTPUT_FILE.open(
        "w", newline="", encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(email_rows)

    # Display summary
    print("\n========== EMAIL PREVIEW SUMMARY ==========")
    print(f"Category folders found: {len(category_folders)}")
    print(f"Emails prepared in preview: {len(email_rows)}")
    print(f"Folders requiring review: {len(review_required)}")
    print(f"Preview file: {OUTPUT_FILE}")
    print("\nNO EMAILS HAVE BEEN SENT.")

    # Show folders that need review
    if review_required:
        print("\nFolders requiring review:")
        for folder in review_required:
            print(folder)

    # Display sample subjects
    print("\nSample email subjects:")
    for row in email_rows[:5]:
        print(row["subject"])


if __name__ == "__main__":
    generate_preview()
