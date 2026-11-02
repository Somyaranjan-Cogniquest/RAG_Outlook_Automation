import win32com.client

try:
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")

    print("Outlook desktop connection successful!")

    for account in namespace.Accounts:
        print("Account:", account.DisplayName)

except Exception as error:
    print("Could not connect to Outlook desktop.")
    print("Error:", error)
