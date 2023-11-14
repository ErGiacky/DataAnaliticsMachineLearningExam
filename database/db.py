import sqlite3
import pandas as pd
import requests
from io import StringIO

# URL del tuo dataset CSV
csv_url = 'https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/shopping_trends.csv'

# Scarica il file CSV dal tuo URL
response = requests.get(csv_url)
data = StringIO(response.text)

# Connessione al database
conn = sqlite3.connect('database/sqlite/db.sqlite')

# Creazione di un cursore per eseguire comandi SQL
cursor = conn.cursor()

# Comando per creare la tabella CustomerData
cursor.execute('''
CREATE TABLE IF NOT EXISTS CustomerData (
    CustomerID INTEGER PRIMARY KEY,
    Age INTEGER,
    Gender TEXT,
    ItemPurchased TEXT,
    Category TEXT,
    PurchaseAmount REAL,
    Location TEXT,
    Size TEXT,
    Color TEXT,
    Season TEXT,
    ReviewRating REAL,
    SubscriptionStatus TEXT,
    PaymentMethod TEXT,
    ShippingType TEXT,
    DiscountApplied TEXT,
    PromoCodeUsed TEXT,
    PreviousPurchases INTEGER,
    PreferredPaymentMethod TEXT,
    FrequencyOfPurchases TEXT
)
''')

# Commit delle modifiche
conn.commit()

# Leggi il CSV e inserisci i dati nel database
df = pd.read_csv(data)

# Utilizza il metodo to_sql di pandas per inserire i dati nel database SQLite
df.to_sql('CustomerData', conn, if_exists='replace', index=False)

# Commit delle modifiche
conn.commit()

# Chiudo della connessione
conn.close()
