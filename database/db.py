import sqlite3
import os 

# Connessione al database
db_path = 'database/sqlite/db.sqlite'

# Creazione di un cursore per eseguire comandi SQL
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Comando per creare la tabella CustomerData
cursor.execute('''
CREATE TABLE CustomerData (
    CustomerID INT PRIMARY KEY,
    Age INT,
    Gender VARCHAR(10),
    ItemPurchased VARCHAR(50),
    Category VARCHAR(50),
    PurchaseAmount DECIMAL(10, 2),
    Location VARCHAR(50),
    Size VARCHAR(5),
    Color VARCHAR(20),
    Season VARCHAR(20),
    ReviewRating DECIMAL(3, 1),
    SubscriptionStatus VARCHAR(3),
    PaymentMethod VARCHAR(20),
    ShippingType VARCHAR(20),
    DiscountApplied VARCHAR(3),
    PromoCodeUsed VARCHAR(3),
    PreviousPurchases INT,
    PreferredPaymentMethod VARCHAR(20),
    FrequencyOfPurchases VARCHAR(20)
)
''')

conn.commit()


# Chiudo della connessione
conn.close()
