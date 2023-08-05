import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email():
    sender_email = "esbpy@hotmail.com"
    sender_password = "mJQLvBRL-kkM!t3" 

    receiver_email = email_entry.get()

    # Construct the message
    subject = "Test Email"
    body = "This is a test email sent from a Python script."
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.office365.com', 587) as server:  
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")
        print(e)

# Create the main GUI window
root = tk.Tk()
root.title("Email Sender")
root.geometry("300x150")

# Add an input field for the email address
email_label = tk.Label(root, text="Enter Email Address:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Add a button to send the email
send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack()

# Start the main event loop
root.mainloop()
