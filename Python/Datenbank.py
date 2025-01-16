import sqlite3

def create_database(db_name):
    """Erstellt eine neue SQLite-Datenbank und eine Tabelle."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Tabelle erstellen
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """)
    conn.commit()
    conn.close()
    print(f"Datenbank '{db_name}' erstellt (falls nicht vorhanden).")

def insert_data(db_name, name, email):
    """Fügt einen neuen Datensatz in die Tabelle ein."""
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(f"Benutzer '{name}' hinzugefügt.")
    except sqlite3.IntegrityError:
        print(f"Fehler: Die E-Mail '{email}' existiert bereits.")
    finally:
        conn.close()

def fetch_data(db_name):
    """Liest alle Datensätze aus der Tabelle aus."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    # Datenbankname
    db_name = "example.db"
    
    # Datenbank erstellen und Tabelle vorbereiten
    create_database(db_name)
    
    # Beispiel-Daten hinzufügen
    insert_data(db_name, "Alice", "alice@example.com")
    insert_data(db_name, "Bob", "bob@example.com")
    
    # Daten abrufen
    users = fetch_data(db_name)
    print("Benutzer in der Datenbank:")
    for user in users:
        print(user)
