import tkinter as tk
from tkinter import ttk, messagebox
from main import scan_phishing


class PhishingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing Link Detection System v1.0")
        self.root.geometry("1000x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f6f9")

#Left PANEL
        left = tk.Frame(root, bg="#0f172a", width=260)
        left.pack(side="left", fill="y")

        tk.Label(
            left,
            text="    🛡️\nPHISHING\nDETECTION",
            fg="white",
            bg="#0f172a",
            font=("Segoe UI", 18, "bold"),
            justify="center"
        ).pack(pady=40)

        tk.Label(
            left,
            text="• URL Analysis\n• Sender Analysis\n• Content Check\n• Attachment Scan",
            fg="#cbd5e1",
            bg="#0f172a",
            font=("Segoe UI", 11),
            justify="left"
        ).pack(pady=10)

        tk.Label(
            left,
            text="Final Yea\nv1.0",
            fg="#94a3b8",
            bg="#0f172a",
            font=("Segoe UI", 10)
        ).pack(side="bottom", pady=20)

#RIGHT PANEL
        right = tk.Frame(root, bg="#f4f6f9")
        right.pack(side="right", fill="both", expand=True)

        tk.Label(
            right,
            text="Phishing Link Detection System",
            font=("Segoe UI", 22, "bold"),
            bg="#f4f6f9"
        ).pack(pady=20)

#INPUT CARD
        card = tk.Frame(
            right, bg="white", bd=1, relief="solid"
        )
        card.pack(padx=30, pady=10, fill="x")

        self.url = self.input_row(card, "URL")
        self.sender = self.input_row(card, "Sender Email")
        self.content = self.input_row(card, "Email Content", multiline=True)
        self.attachment = self.input_row(card, "Attachment Filename")

        ttk.Button(
            right,
            text="🔍 Scan Email",
            command=self.scan,
            width=30
        ).pack(pady=15)

#RESULT CARD
        result_card = tk.Frame(
            right, bg="white", bd=1, relief="solid"
        )
        result_card.pack(padx=30, pady=10, fill="both", expand=True)

        self.result_label = tk.Label(
            result_card,
            text="RESULT",
            font=("Segoe UI", 16, "bold"),
            bg="white"
        )
        self.result_label.pack(anchor="w", padx=15, pady=5)

        self.result_box = tk.Text(
            result_card,
            height=10,
            font=("Consolas", 11),
            bg="#f8fafc",
            bd=0
        )
        self.result_box.pack(padx=15, pady=5, fill="both", expand=True)

    def input_row(self, parent, label, multiline=False):
        frame = tk.Frame(parent, bg="white")
        frame.pack(fill="x", padx=20, pady=8)

        tk.Label(
            frame,
            text=label,
            width=18,
            anchor="w",
            bg="white",
            font=("Segoe UI", 11)
        ).pack(side="left")

        if multiline:
            widget = tk.Text(
                frame, height=4, width=60,
                bg="#f8fafc", relief="solid", bd=1
            )
        else:
            widget = tk.Entry(
                frame, width=62,
                bg="#f8fafc", relief="solid", bd=1
            )

        widget.pack(side="left")
        return widget

    def scan(self):
        url = self.url.get()
        sender = self.sender.get()
        content = self.content.get("1.0", tk.END)
        attachment = self.attachment.get()

        if not url or not sender:
            messagebox.showerror("Error", "URL and Sender Email are required")
            return

        result, score, reasons = scan_phishing(
            url, sender, content, attachment
        )

        self.result_box.delete("1.0", tk.END)

        color = "green" if result == "SAFE" else "red"

        self.result_box.insert(
            tk.END,
            f"STATUS : {result}\n",
        )
        self.result_box.tag_add("status", "1.0", "1.end")
        self.result_box.tag_config("status", foreground=color, font=("Consolas", 12, "bold"))

        self.result_box.insert(
            tk.END,
            f"Score  : {score}\n\nReasons:\n"
        )

        for r in reasons:
            self.result_box.insert(tk.END, f"• {r}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = PhishingGUI(root)
    root.mainloop()
