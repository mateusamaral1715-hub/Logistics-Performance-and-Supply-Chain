# 🚛 Logistics & Supply Chain Performance: End-to-End Data Pipeline

This repository showcases a complete Data Analytics workflow designed for executive-level decision-making. The project focuses on identifying bottlenecks by shipping mode, warehouse location, and supplier performance to reduce delays in a complex supply chain.

## 🎯 Business Problem
How to optimize operations and reduce delays in a supply chain handling **30,000+ yearly shipments**? This dashboard provides actionable insights to track efficiency and improve overall delivery performance.

---

## ⚙️ Part 1: Data Engineering & Pipeline (Python & SQL)
To simulate a real-world enterprise architecture, I bypassed static spreadsheets completely and built a direct database connection.

* **Data Generation:** Developed a Python script to generate over 30,000 rows of synthetic logistics data.

<p align="center">
  <img height="400" alt="Python Script Snippet" src="https://github.com/user-attachments/assets/90993b14-1052-4b32-ac1d-b5420ecfc609" />
</p>

* **Database Integration:** Ingested the generated data directly into a **MySQL database** (hosted locally via **WampServer**).

<p align="center">
  <img height="400" alt="MySQL Database Integration" src="https://github.com/user-attachments/assets/818d20f2-91a7-49cd-81b5-0b9d01187811" />
</p>

* **Corporate Pipeline:** Connected Power BI directly to this SQL server, mimicking a true corporate data environment.

---

## 💡 Part 2: Business Intelligence & UI/UX (Power BI)
The SQL data was transformed into a highly interactive, senior-level dashboard:

* **Advanced Data Modeling:** Implemented a **Star Schema** architecture with a custom Calendar table to handle specific business logic (including bank holidays).
* **DAX Mastery:** Created complex measures, including moving averages for trend analysis and dynamic KPI tracking like the **On-Time Delivery (OTD) Rate %**.
* **Senior UI/UX Design:** Engineered using the **"Z-Pattern"** for visual hierarchy, ensuring minimal cognitive load (utilizing off-black typography and strategic negative space), alongside impactful Conditional Formatting.
* **Advanced Interactivity:** Features cross-filtering across all visuals, Custom Dropdown Slicers (Year/Incoterm), and a dynamic **"Clear Filters"** button engineered using Power BI Bookmarks.

---

## 🛠️ Tech Stack
* **Languages:** Python, SQL, DAX
* **Tools & Infrastructure:** Power BI, MySQL Workbench, WampServer

---

## 🚀 How to Use This Repository

1. **Setup the Database:** Ensure WampServer (or your preferred local server) is running with MySQL.
2. **Run the Python Script:** Execute the data generation script to populate the MySQL database with the 30,000+ shipment records.
3. **Open the Dashboard:** Open the `.pbix` file in Power BI Desktop and refresh the data connections to your local SQL server.
4. **Interact with the Project:**
   * 👉 **[Click Here to Open the Live Interactive Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNjE3MDdkZjQtOWZmYS00OWM1LTkwOGItYjQ3NDk3MDdiZWExIiwidCI6IjUxYmEzOWRiLWRkYjAtNDQ3YS04MTU0LTgzNGEwYTZmZDJlOCJ9)**

<p align="center">
  <img height="400" alt="Logistics Dashboard Preview" src="https://github.com/user-attachments/assets/094b8bdf-34cd-438f-841b-26318c4a9cdb" />
</p>

---

## 📫 Professional Contact

**Mateus Amaral da Costa**
* **Role:** Business Intelligence Analyst | Business Administrator
* **Location:** Catalão, Brazil (Available for Relocation/Remote roles in Ireland)
* **LinkedIn:** [Connect with me on LinkedIn](https://www.linkedin.com/in/mateus-amaral-895392293)
* **Email:** [mateus.amaral1715@gmail.com](mailto:mateus.amaral1715@gmail.com)
