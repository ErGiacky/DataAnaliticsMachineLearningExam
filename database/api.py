from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI()

# Connessione al database
db_path = os.path.abspath('../database/sqlite/db.sqlite')

def connect_db():
    return sqlite3.connect(db_path)

class Customer(BaseModel):
    Customer_ID: int
    Age: int
    Gender: str
    Item_Purchased: str
    Category: str
    Purchase_Amount: float
    Location: str
    Size: str
    Color: str
    Season: str
    Review_Rating: float
    Subscription_Status: str
    Payment_Method: str
    Shipping_Type: str
    Discount_Applied: str
    Promo_Code_Used: str
    Previous_Purchases: int
    Preferred_Payment_Method: str
    Frequency_of_Purchases: str

#GET 

@app.get('/customers', response_model=list[Customer])
async def get_all_customers():
    conn = None  # Move this line to here

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM CustomerData')
        customers = cursor.fetchall()

        customer_list = [Customer(
            Customer_ID=row[0], Age=row[1], Gender=row[2], Item_Purchased=row[3],
            Category=row[4], Purchase_Amount=row[5], Location=row[6],
            Size=row[7], Color=row[8], Season=row[9], Review_Rating=row[10],
            Subscription_Status=row[11], Payment_Method=row[12], Shipping_Type=row[13],
            Discount_Applied=row[14], Promo_Code_Used=row[15], Previous_Purchases=row[16],
            Preferred_Payment_Method=row[17], Frequency_of_Purchases=row[18]
        ) for row in customers]

        return customer_list

    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f'SQLite error: {e}')

    finally:
        if conn:
            conn.close()

#POST

@app.post('/customers', response_model=Customer)
async def create_customer(customer: Customer):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Assuming CustomerData table structure: (Customer_ID, Age, Gender, ...)
        cursor.execute("""
            INSERT INTO CustomerData
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            customer.Customer_ID, customer.Age, customer.Gender, customer.Item_Purchased,
            customer.Category, customer.Purchase_Amount, customer.Location,
            customer.Size, customer.Color, customer.Season, customer.Review_Rating,
            customer.Subscription_Status, customer.Payment_Method, customer.Shipping_Type,
            customer.Discount_Applied, customer.Promo_Code_Used, customer.Previous_Purchases,
            customer.Preferred_Payment_Method, customer.Frequency_of_Purchases
        ))

        conn.commit()

        return customer

    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f'SQLite error: {e}')

    finally:
        if conn:
            conn.close()

    # PUT 
@app.put('/customers/{customer_id}', response_model=Customer)
async def update_customer(customer_id: int, customer: Customer):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE CustomerData
            SET Age=?, Gender=?, Item_Purchased=?, Category=?, Purchase_Amount=?,
            Location=?, Size=?, Color=?, Season=?, Review_Rating=?, Subscription_Status=?,
            Payment_Method=?, Shipping_Type=?, Discount_Applied=?, Promo_Code_Used=?,
            Previous_Purchases=?, Preferred_Payment_Method=?, Frequency_of_Purchases=?
            WHERE Customer_ID=?
        """, (
            customer.Age, customer.Gender, customer.Item_Purchased,
            customer.Category, customer.Purchase_Amount, customer.Location,
            customer.Size, customer.Color, customer.Season, customer.Review_Rating,
            customer.Subscription_Status, customer.Payment_Method, customer.Shipping_Type,
            customer.Discount_Applied, customer.Promo_Code_Used, customer.Previous_Purchases,
            customer.Preferred_Payment_Method, customer.Frequency_of_Purchases, customer_id
        ))

        conn.commit()

        return customer

    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f'SQLite error: {e}')

    finally:
        if conn:
            conn.close()

# DELETE 
@app.delete('/customers/{customer_id}', response_model=dict)
async def delete_customer(customer_id: int):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Assuming CustomerData table structure: (Customer_ID, Age, Gender, ...)
        cursor.execute("DELETE FROM CustomerData WHERE Customer_ID=?", (customer_id,))
        conn.commit()

        return {"message": f"Customer {customer_id} deleted successfully"}

    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f'SQLite error: {e}')

    finally:
        if conn:
            conn.close()


