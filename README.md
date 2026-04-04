# 🇮🇪 Supply Chain FinOps & Cost Observability Pipeline

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)](https://www.mysql.com/)
[![Power BI](https://img.shields.io/badge/Power_BI-Executive_Dashboard-yellow.svg)](https://powerbi.microsoft.com/)
[![Focus](https://img.shields.io/badge/Focus-FinOps_&_Unit_Economics-gold)]()

## 📌 Executive Summary
In complex logistics networks, operational bottlenecks directly translate to **revenue leakage**. This project demonstrates a **FinOps-driven approach** to supply chain observability across major Irish hubs (Dublin Port, Shannon Airport, Cork Harbour). 

By engineering an end-to-end data pipeline (Python ➡️ MySQL ➡️ Power BI), I transformed 30,000+ raw shipment records into a strategic framework that empowers CFOs and Operations Managers to track Unit Economics, optimize freight spend, and mitigate the financial impact of SLA breaches.

---

## 🚀 Strategic FinOps Impact
This architecture maps directly to the core principles of Financial Operations:

* **Inform (Cost Allocation):** Transitioned from flat-file silos to a robust relational architecture (MySQL), establishing a "Single Source of Truth" for precise cost auditing and vendor management.
* **Optimize (Unit Economics):** Simulated and analyzed freight costs inclusive of **Irish VAT (23%)**, tracking cost-per-KG variances across different shipping modes (Sea, Road, Air).
* **Operate (Risk Mitigation):** Correlated On-Time Delivery (OTD) rates with supply chain health, quantifying how logistical delays impact overarching financial performance and customer lifetime value (LTV).

---

## 🛠️ AI-Ready Data Infrastructure
To deploy reasoning agents (like Nexus-AI), a company first needs pristine data architecture. This project serves as that foundation.

### 1. Data Engineering (Python & SQL)
* **Synthetic Ingestion:** Developed a Python script to generate high-fidelity enterprise data, simulating realistic Incoterms, fluctuating freight rates, and volumetric pricing.
 <p align="center">
  <img height="400" alt="Python Script Snippet" src="https://github.com/user-attachments/assets/90993b14-1052-4b32-ac1d-b5420ecfc609" />
</p>

* **Relational Database:** Automated data ingestion into a **MySQL Database**, establishing strict primary/foreign key relationships to prevent data anomalies.
  <p align="center">
  <img height="400" alt="MySQL Database Integration" src="https://github.com/user-attachments/assets/818d20f2-91a7-49cd-81b5-0b9d01187811" />
</p>

### 2. FinOps Data Modeling (Star Schema)
Designed for high-performance analytical queries and executive reporting:

* **fact_shipments:** The core financial ledger containing ~30,000 transactions, tracking arrival dates, Incoterm liabilities, and freight costs.
* **dim_suppliers:** Vendor risk and cost-efficiency scoring.
* **dim_warehouses:** Strategic mapping of Irish logistics hubs, including **Eircodes** and capacity limits.
* **_Measures:** Centralized DAX repository housing advanced executive calculations like **VAT-inclusive Unit Costs** and **OTD Revenue Risk %**.
  
### 3. Executive Observability (Power BI)
* **CFO-Level Dashboard:** Designed a high-contrast interface focusing on the metrics that impact the bottom line: delayed shipments, vendor efficiency, and total freight spend.

---

## 📊 Project Showcase (Live PoC)
 👉 **[Click Here to Open the Live Interactive Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNjE3MDdkZjQtOWZmYS00OWM1LTkwOGItYjQ3NDk3MDdiZWExIiwidCI6IjUxYmEzOWRiLWRkYjAtNDQ3YS04MTU0LTgzNGEwYTZmZDJlOCJ9)**

 <p align="center">
  <img height="400" alt="Logistics Dashboard Preview" src="https://github.com/user-attachments/assets/094b8bdf-34cd-438f-841b-26318c4a9cdb" />
</p>

---

## 🏗️ How to Use This Repository

1. **Setup Database:** Ensure MySQL/WampServer is running. Execute the SQL script in `/sql` to create the schema.
2. **Run Python Script:** Execute `generate_logistics_data.py` to populate the DB with synthetic logistics data.
3. **Open Dashboard:** Connect the `.pbix` file to your local MySQL instance.

---

## 🇮🇪 Ireland Critical Skills (CSEP) Alignment

* **Business Partnering:** Translating operational logistics data into financial insights.
* **Data Infrastructure:** Building reliable SQL/Python pipelines necessary for modern Analytics & AI teams.
* **Local Compliance:** Applied integration of Irish VAT (23%) and Eircode systems.

---
**Engineered by [Mateus Amaral](https://www.linkedin.com/in/mateus-amaral-895392293)** • *Business Analyst | FinOps & AI Specialist | Relocating to Ireland 🇮🇪*
