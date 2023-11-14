from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Connessione al database
db_path = 'database/sqlite/db.sqlite'

def connect_db():
    return sqlite3.connect(db_path)

@app.route('/customers', methods=['GET'])
def get_all_customers():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Eseguire la query di selezione
        cursor.execute("SELECT * FROM CustomerData")
        customers = cursor.fetchall()

        # Convertire i risultati in un elenco di dizionari
        customer_list = [{'CustomerID': row[0], 'Age': row[1], 'Gender': row[2], 'ItemPurchased': row[3],
                          'Category': row[4], 'PurchaseAmount': row[5], 'Location': row[6],
                          'Size': row[7], 'Color': row[8], 'Season': row[9], 'ReviewRating': row[10],
                          'SubscriptionStatus': row[11], 'PaymentMethod': row[12], 'ShippingType': row[13],
                          'DiscountApplied': row[14], 'PromoCodeUsed': row[15], 'PreviousPurchases': row[16],
                          'PreferredPaymentMethod': row[17], 'FrequencyOfPurchases': row[18]} for row in customers]

        return jsonify(customer_list)

    except sqlite3.Error as e:
        return jsonify({'error': f'SQLite error: {e}'}), 500

    finally:
        if conn:
            conn.close()

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer_by_id(customer_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Eseguire la query di selezione con un parametro
        cursor.execute("SELECT * FROM CustomerData WHERE CustomerID = ?", (customer_id,))
        customer = cursor.fetchone()

        if customer:
            # Convertire il risultato in un dizionario
            customer_dict = {'CustomerID': customer[0], 'Age': customer[1], 'Gender': customer[2],
                             'ItemPurchased': customer[3], 'Category': customer[4],
                             'PurchaseAmount': customer[5], 'Location': customer[6],
                             'Size': customer[7], 'Color': customer[8], 'Season': customer[9],
                             'ReviewRating': customer[10], 'SubscriptionStatus': customer[11],
                             'PaymentMethod': customer[12], 'ShippingType': customer[13],
                             'DiscountApplied': customer[14], 'PromoCodeUsed': customer[15],
                             'PreviousPurchases': customer[16], 'PreferredPaymentMethod': customer[17],
                             'FrequencyOfPurchases': customer[18]}

            return jsonify(customer_dict)
        else:
            return jsonify({'error': f'Customer with ID {customer_id} not found'}), 404

    except sqlite3.Error as e:
        return jsonify({'error': f'SQLite error: {e}'}), 500

    finally:
        if conn:
            conn.close()

@app.route('/customers', methods=['POST'])
def create_customer():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Estrai i dati dalla richiesta POST
        data = request.json

        # Eseguire la query di inserimento
        cursor.execute("INSERT INTO CustomerData VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (data['CustomerID'], data['Age'], data['Gender'], data['ItemPurchased'],
                        data['Category'], data['PurchaseAmount'], data['Location'], data['Size'],
                        data['Color'], data['Season'], data['ReviewRating'], data['SubscriptionStatus'],
                        data['PaymentMethod'], data['ShippingType'], data['DiscountApplied'],
                        data['PromoCodeUsed'], data['PreviousPurchases'], data['PreferredPaymentMethod'],
                        data['FrequencyOfPurchases']))

        # Commit delle modifiche
        conn.commit()

        return jsonify({'message': 'Customer created successfully'})

    except sqlite3.Error as e:
        return jsonify({'error': f'SQLite error: {e}'}), 500

    finally:
        if conn:
            conn.close()

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Estrai i dati dalla richiesta PUT
        data = request.json

        # Eseguire la query di aggiornamento
        cursor.execute("UPDATE CustomerData SET Age=?, Gender=?, ItemPurchased=?, Category=?, "
                       "PurchaseAmount=?, Location=?, Size=?, Color=?, Season=?, ReviewRating=?, "
                       "SubscriptionStatus=?, PaymentMethod=?, ShippingType=?, DiscountApplied=?, "
                       "PromoCodeUsed=?, PreviousPurchases=?, PreferredPaymentMethod=?, "
                       "FrequencyOfPurchases=? WHERE CustomerID=?",
                       (data['Age'], data['Gender'], data['ItemPurchased'], data['Category'],
                        data['PurchaseAmount'], data['Location'], data['Size'], data['Color'],
                        data['Season'], data['ReviewRating'], data['SubscriptionStatus'],
                        data['PaymentMethod'], data['ShippingType'], data['DiscountApplied'],
                        data['PromoCodeUsed'], data['PreviousPurchases'], data['PreferredPaymentMethod'],
                        data['FrequencyOfPurchases'], customer_id))

        # Commit delle modifiche
        conn.commit()

        return jsonify({'message': f'Customer with ID {customer_id} updated successfully'})

    except sqlite3.Error as e:
        return jsonify({'error': f'SQLite error: {e}'}), 500

    finally:
        if conn:
            conn.close()

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Eseguire la query di eliminazione
        cursor.execute("DELETE FROM CustomerData WHERE CustomerID=?", (customer_id,))

        # Commit delle modifiche
        conn.commit()

        return jsonify({'message': f'Customer with ID {customer_id} deleted successfully'})

    except sqlite3.Error as e:
        return jsonify({'error': f'SQLite error: {e}'}), 500

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
