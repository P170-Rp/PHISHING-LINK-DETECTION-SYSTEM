import tkinter as tk
from tkinter import messagebox
from main import scan_phishing

def scan():
    url = url_entry.get()
    sender = sender_entry.get()
    message = message_text.get("1.0", tk.END)
    attachment = attachment_entry.get()

    result, score, reasons = scan_phishing(url, sender, message, attachment)

    output.delete("1.0", tk.END)
    output.insert(tk.END, f"Result: {result}\n")
    output.insert(tk.END, f"Score: {score}\n\nReasons:\n")

    for r in reasons:
        output.insert(tk.END, f"- {r}\n")

root = tk.Tk()
root.title("Phishing Link Detection System")
root.geometry("600x550")

tk.Label(root, text="URL").pack()
url_entry = tk.Entry(root, width=70)
url_entry.pack()

tk.Label(root, text="Sender Email").pack()
sender_entry = tk.Entry(root, width=70)
sender_entry.pack()

tk.Label(root, text="Email Message").pack()
message_text = tk.Text(root, height=5, width=70)
message_text.pack()

tk.Label(root, text="Attachment Filename").pack()
attachment_entry = tk.Entry(root, width=70)
attachment_entry.pack()

tk.Button(root, text="Scan Email", command=scan, bg="red", fg="white").pack(pady=10)

output = tk.Text(root, height=10, width=70)
output.pack()

root.mainloop()
