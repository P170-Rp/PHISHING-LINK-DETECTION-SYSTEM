import sqlite3

def save_scan(sender_email , url, result, score, reasons):
    conn = sqlite3.connect("database/phishing.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
           sender_email TEXT,
            url TEXT,
            result TEXT,
            score INTEGER,
            reasons TEXT,
            scan_time DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        INSERT INTO scans (sender_email, url, result, score, reasons)
        VALUES (?, ?, ?, ?, ?)
    """, (
       sender_email,
        url,
        result,
        score,
        ", ".join(reasons)
    ))

    conn.commit()
    conn.close()
