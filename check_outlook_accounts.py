import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application")
session = outlook.Session

print("Outlook accounts:")

for account in session.Accounts:
    print(
        "Name:", account.DisplayName,
        "| Email:", account.SmtpAddress
    )