# 🇮🇪 End-to-End Logistics & Supply Chain Pipeline: Python, SQL & Power BI

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)](https://www.mysql.com/)
[![Power BI](https://img.shields.io/badge/Power_BI-Supply_Chain-yellow.svg)](https://powerbi.microsoft.com/)

## 📌 Executive Summary
This project simulates a high-scale **Irish Logistics Operation**, focusing on the supply chain flow between major hubs: **Dublin Port, Shannon Airport, Galway Hub, and Cork Harbour**.

To mimic a real-world enterprise environment, I bypassed static spreadsheets and built a dynamic pipeline: **Python (Data Generation) ➡️ MySQL (Relational Storage) ➡️ Power BI (Strategic Analytics)**. I engineered over 30,000 shipment records to analyze delivery performance, freight costs, and supplier reliability.

---

## 🚀 Corporate Pipeline & Impact
* **Relational Architecture:** Transitioned from flat-file processing to a structured **MySQL Database** (hosted via WampServer), mimicking a professional data warehouse environment.
* **Logistics Optimization:** Simulated and analyzed key Supply Chain KPIs: **On-Time Delivery (OTD) Rate**, **Freight Cost per KG**, and **Delayed Shipment Trends**.
* **Irish Infrastructure Focus:** Strategic mapping of logistics performance across Ireland's key ports and airports.

---

## 🛠️ The Tech Stack
### 1. Data Engineering (Python & SQL)
* **Synthetic Generation:** Developed a Python script to generate realistic logistics data, including Incoterms, shipping modes (Sea, Road, Air), and weight-based pricing.
 <p align="center">
  <img height="400" alt="Python Script Snippet" src="https://github.com/user-attachments/assets/90993b14-1052-4b32-ac1d-b5420ecfc609" />
</p>

* **Database Integration:** Automated data ingestion into a **MySQL Database**, utilizing SQL scripts to create optimized tables and primary/foreign key relationships.
  <p align="center">
  <img height="400" alt="MySQL Database Integration" src="https://github.com/user-attachments/assets/818d20f2-91a7-49cd-81b5-0b9d01187811" />
</p>

### 2. Data Modeling & Star Schema
* **Fact_Shipments:** Centralized transactional data (~30,000 rows).
* **Dimensions:** Built relational links to `Dim_Suppliers`, `Dim_Products`, and `Dim_Warehouses` for multi-dimensional analysis.

### 3. Business Intelligence (Power BI)
* **Executive Dashboard:** Designed a high-impact interface to monitor delayed shipments and supplier performance.
* **Advanced DAX:** Calculated metrics for **Freight Cost (inc. VAT)** and **On-Time Delivery Rate %**.

---

## 📊 Project Showcase
 👉 **[Click Here to Open the Live Interactive Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNjE3MDdkZjQtOWZmYS00OWM1LTkwOGItYjQ3NDk3MDdiZWExIiwidCI6IjUxYmEzOWRiLWRkYjAtNDQ3YS04MTU0LTgzNGEwYTZmZDJlOCJ9)**

 <p align="center">
  <img height="400" alt="Logistics Dashboard Preview" src="https://github.com/user-attachments/assets/094b8bdf-34cd-438f-841b-26318c4a9cdb" />
</p>

---

## 🏗️ How to Use This Repository
1. **Setup Database:** Ensure MySQL/WampServer is running. Execute the SQL script in `/sql` to create the schema.
2. **Run Python Script:** Execute `generate_logistics_data.py` to populate the DB.
3. **Open Dashboard:** Connect the `.pbix` file to your local MySQL instance.

---

## 👨‍💻 About the Author
**Mateus - Business & Data Analyst**
* **Focus:** SQL Architecture, Supply Chain BI, and Process Automation.
* **Education:** Bachelor of Business Administration (**NFQ Level 8** equivalent).
* **Status:** Ready to relocate to Ireland (Dublin/Cork/Galway) under the **CSEP**.
