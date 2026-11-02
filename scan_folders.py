from pathlib import Path

# Main folder containing the 13 document categories
ROOT_FOLDER = Path(
    r"C:\Users\ADMIN\Downloads\PAN_2.0_KYC_Doc_set_Synthetic_1300"
    r"\PAN 2.0 KYC Doc set\PAN 2.0 doc sets"
)

def main():
    if not ROOT_FOLDER.exists():
        print(f"ERROR: Folder not found:\n{ROOT_FOLDER}")
        return

    categories = sorted(
        folder for folder in ROOT_FOLDER.iterdir()
        if folder.is_dir()
    )

    total_subfolders = 0
    valid_subfolders = 0
    missing_or_extra_pdfs = []
    unexpected_files = []

    print(f"Main folder: {ROOT_FOLDER}\n")
    print(f"Category folders found: {len(categories)}\n")

    for category in categories:
        print(f"\nCategory: {category.name}")

        subfolders = sorted(
            folder for folder in category.iterdir()
            if folder.is_dir()
        )

        print(f"  Subfolders: {len(subfolders)}")

        for subfolder in subfolders:
            total_subfolders += 1

            pdf_files = [
                file for file in subfolder.iterdir()
                if file.is_file() and file.suffix.lower() == ".pdf"
            ]

            other_files = [
                file for file in subfolder.iterdir()
                if file.is_file() and file.suffix.lower() != ".pdf"
            ]

            if len(pdf_files) == 2 and not other_files:
                valid_subfolders += 1
            else:
                missing_or_extra_pdfs.append(
                    (category.name, subfolder.name, len(pdf_files))
                )

            if other_files:
                unexpected_files.append(
                    (category.name, subfolder.name,
                     [file.name for file in other_files])
                )

    print("\n========== SCAN SUMMARY ==========")
    print(f"Category folders: {len(categories)}")
    print(f"Total subfolders: {total_subfolders}")
    print(f"Subfolders with exactly 2 PDFs and no other files: {valid_subfolders}")
    print(f"Subfolders needing review: {len(missing_or_extra_pdfs)}")
    print(f"Subfolders containing other files: {len(unexpected_files)}")

    if missing_or_extra_pdfs:
        print("\nSubfolders needing review (category, folder, PDF count):")
        for item in missing_or_extra_pdfs:
            print(f"  {item}")

    if unexpected_files:
        print("\nSubfolders containing other files:")
        for item in unexpected_files:
            print(f"  {item}")

if __name__ == "__main__":
    main()
