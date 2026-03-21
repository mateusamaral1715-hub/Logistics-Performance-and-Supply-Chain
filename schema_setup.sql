CREATE SCHEMA irish_supply_chain;
USE irish_supply_chain;
CREATE TABLE Dim_Suppliers (
    Supplier_ID INT PRIMARY KEY AUTO_INCREMENT,
    Supplier_Name VARCHAR(100),
    Country VARCHAR(50), 
    Supplier_Rating DECIMAL(3,2)
);

CREATE TABLE Dim_Products (
    Product_ID INT PRIMARY KEY AUTO_INCREMENT,
    Product_Name VARCHAR(100),
    Category VARCHAR(50), 
    Unit_Cost_EUR DECIMAL(10,2),
    Unit_Weight_kg DECIMAL(10,2)
    );
    
    CREATE TABLE Dim_Warehouses (
    Warehouse_ID INT PRIMARY KEY AUTO_INCREMENT,
    Location VARCHAR(50), 
    Eircode VARCHAR(10),
    Capacity_m3 INT
);CREATE TABLE Fact_Shipments (
    Shipment_ID VARCHAR(20) PRIMARY KEY,
    Order_Date DATE,
    Arrival_Date DATE,
    Supplier_ID INT,
    Product_ID INT,
    Warehouse_ID INT,
    Quantity INT,
    Shipping_Mode VARCHAR(20), 
    Incoterm VARCHAR(3), 
    Shipping_Cost_EUR DECIMAL(10,2),
    Status VARCHAR(20), 
    FOREIGN KEY (Supplier_ID) REFERENCES Dim_Suppliers(Supplier_ID),
    FOREIGN KEY (Product_ID) REFERENCES Dim_Products(Product_ID),
    FOREIGN KEY (Warehouse_ID) REFERENCES Dim_Warehouses(Warehouse_ID)
);

SELECT * FROM Fact_Shipments;
