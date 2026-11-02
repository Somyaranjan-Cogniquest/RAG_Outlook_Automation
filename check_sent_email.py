import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")

target_subject = "[TEST] Aadhar set - 001"

folders_to_check = {
    "Sent Items": 5,
    "Outbox": 4,
    "Drafts": 16,
}

for folder_name, folder_id in folders_to_check.items():
    print(f"\nChecking {folder_name}...")

    try:
        folder = namespace.GetDefaultFolder(folder_id)
        items = folder.Items
        items.Sort("[CreationTime]", True)

        found = False

        for item in items:
            try:
                if target_subject in str(item.Subject):
                    print("FOUND")
                    print("Subject:", item.Subject)
                    print("To:", item.To)
                    print("Created:", item.CreationTime)
                    print("Folder:", folder_name)
                    found = True
                    break
            except Exception:
                continue

        if not found:
            print("Test email not found.")

    except Exception as error:
        print("Could not check folder:", error)