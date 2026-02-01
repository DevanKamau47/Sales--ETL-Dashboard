 # Sales Dashboard + ETL Pipeline (BI → Data Engineering)

##  Project Overview
This project demonstrates an end-to-end data workflow: extracting raw sales data, transforming it using Python, loading it into PostgreSQL, and visualizing insights using Power BI.

The goal of this project is to showcase practical skills in:
- Data Analysis & Business Intelligence
- Data Engineering fundamentals
- Python-based ETL pipelines
- SQL & PostgreSQL
- Dashboard design and storytelling

---

##  Architecture
Kaggle CSV
↓
Python (pandas ETL)
↓
PostgreSQL (salesdb)
↓
Power BI Dashboard

-------


## 📊 Dashboard Features
### Page 1: Sales Overview
- **KPI Cards**
  Total sales
  City
  Total orders
  Sales by category

### Page 2: Product & Customer Insights
Haha coming sooooonn!!!!!

---

##  Tech Stack
- **Python**: pandas, SQLAlchemy
- **Database**: PostgreSQL
- **BI Tool**: Power BI
- **Data Source**: Kaggle (CSV)
- **Tools**: VS Code, pgAdmin, GitHub

---

## 🔄 ETL Pipeline

### Extract
- Load raw CSV sales data using pandas.

### Transform
- Standardized column names
- Fixed inconsistent date formats (`dayfirst=True`)
- Removed missing / invalid records
- Ensured correct data types

### Load
- Loaded clean data into PostgreSQL using SQLAlchemy
- Table recreated on each run (`if_exists="replace"`)

---

##  Challenges & Solutions
- **Date parsing errors** → Explicit date parsing logic in pandas
- **PostgreSQL authentication issues** → Corrected credentials and connection string
- **Power BI schema mismatch** after table replacement → Reset Power Query steps and rebind visuals

These issues reflect real-world data workflows and were resolved using best practices.

---

##  Key Skills Demonstrated
- End-to-end ETL design
- Debugging data quality & schema issues
- SQL + Python integration
- BI dashboard design
- Analytical thinking & problem solving

---

##  Future Improvements
- Move database credentials to environment variables
- Add logging to ETL pipeline
- Create SQL views for Power BI
- Automate refresh and scheduling
- Enhance DAX measures

---

## 👤 Author
**Devan Kamau**  

