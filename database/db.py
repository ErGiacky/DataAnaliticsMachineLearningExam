import sqlite3
import pandas as pd

# Percorso del tuo file CSV
csv_path = '/Users/alessiogiachino/Desktop/shopping_trends.csv'

# Leggi il CSV
df = pd.read_csv(csv_path, encoding='utf-8')

# Connessione al database SQLite
conn = sqlite3.connect('database/sqlite/db.sqlite')

# Utilizza il metodo to_sql di pandas per inserire i dati nel database SQLite
df.to_sql('CustomerData', conn, if_exists='replace', index=False)  # 'replace' sostituisce la tabella se esiste

# Chiudi la connessione
conn.close()
