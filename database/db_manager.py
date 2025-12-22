import sqlite3

def save_scan(url, result, score, reasons):
    conn = sqlite3.connect("database/phishing.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            result TEXT,
            score INTEGER,
            reasons TEXT,
            scan_time DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute("""
        INSERT INTO scans (url, result, score, reasons)
        VALUES (?, ?, ?, ?)
    """, (url, result, score, ", ".join(reasons)))
    conn.commit()
    conn.close()
