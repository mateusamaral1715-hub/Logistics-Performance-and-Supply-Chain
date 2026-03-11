import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('en_IE')


db_config = {
    "host": "localhost",
    "user": "root",
    "password": "", 
    "database": "irish_supply_chain"
}

try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    

  
    countries = ['Ireland', 'UK', 'Germany', 'USA', 'Netherlands']
    suppliers_data = []
    for _ in range(30):
        suppliers_data.append((
            fake.company(),
            random.choices(countries, weights=[0.3, 0.3, 0.2, 0.1, 0.1])[0],
            round(random.uniform(3.0, 5.0), 2)
        ))
    cursor.executemany("INSERT INTO Dim_Suppliers (Supplier_Name, Country, Supplier_Rating) VALUES (%s, %s, %s)", suppliers_data)
    
    categories = ['Pharma', 'Medical Devices', 'Electronics', 'Packaging']
    products_data = []
    for _ in range(100):
        products_data.append((
            fake.word().capitalize() + " " + random.choice(['Kit', 'System', 'Module', 'Unit']),
            random.choice(categories),
            round(random.uniform(10.0, 5000.0), 2),
            round(random.uniform(0.5, 50.0), 2) # Unit_Weight_kg
        ))
    cursor.executemany("INSERT INTO Dim_Products (Product_Name, Category, Unit_Cost_EUR, Unit_Weight_kg) VALUES (%s, %s, %s, %s)", products_data)

    
    locations = [('Dublin Port', 'D01 X123'), ('Shannon Airport', 'V14 H123'), ('Cork Harbour', 'T12 Y456'), ('Galway Hub', 'H91 Z789')]
    warehouses_data = []
    for loc, eir in locations:
        warehouses_data.append((loc, eir, random.randint(10000, 50000)))
    cursor.executemany("INSERT INTO Dim_Warehouses (Location, Eircode, Capacity_m3) VALUES (%s, %s, %s)", warehouses_data)

    conn.commit()

   
    cursor.execute("SELECT Supplier_ID FROM Dim_Suppliers")
    supplier_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("SELECT Product_ID FROM Dim_Products")
    product_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("SELECT Warehouse_ID FROM Dim_Warehouses")
    warehouse_ids = [row[0] for row in cursor.fetchall()]

    
   
    shipments_data = []
    modes = ['Air', 'Sea', 'Road']
    incoterms = ['EXW', 'FOB', 'CIF', 'DDP', 'DAP']
    statuses = ['Delivered', 'Delivered', 'Delivered', 'Delivered', 'Delayed', 'In Transit', 'Customs Hold']

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2025, 12, 31)
    date_range = (end_date - start_date).days

    for i in range(1, 30001):
        random_days = random.randint(0, date_range)
        order_date = start_date + timedelta(days=random_days)
        lead_time = random.randint(2, 45) 
        arrival_date = order_date + timedelta(days=lead_time)
        
        shipments_data.append((
            f"IE-SHP-{i:06d}",
            order_date.strftime('%Y-%m-%d'),
            arrival_date.strftime('%Y-%m-%d'),
            random.choice(supplier_ids),
            random.choice(product_ids),
            random.choice(warehouse_ids),
            random.randint(10, 1000), 
            random.choice(modes),
            random.choice(incoterms),
            round(random.uniform(150.0, 15000.0), 2), 
            random.choice(statuses)
        ))

   
    batch_size = 5000
    query = """INSERT INTO Fact_Shipments 
               (Shipment_ID, Order_Date, Arrival_Date, Supplier_ID, Product_ID, Warehouse_ID, Quantity, Shipping_Mode, Incoterm, Shipping_Cost_EUR, Status) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    for i in range(0, len(shipments_data), batch_size):
        cursor.executemany(query, shipments_data[i:i+batch_size])
        conn.commit()
     

    

except mysql.connector.Error as err:
    print(f"Database error: {err}")
except Exception as e:
    print(f"Python error: {e}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()