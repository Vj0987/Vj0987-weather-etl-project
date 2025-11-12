# 🌦️ Weather ETL Project (End-to-End Data Pipeline)

## 📘 Overview  
This project demonstrates a complete **ETL (Extract, Transform, Load)** data pipeline built using **Python** and other open-source tools.  
It collects raw weather data, transforms it for analysis, and loads it into a MySQL database — with real-time data streaming powered by **Apache Pulsar**.

---

## ⚙️ Workflow Summary
1. **Extract** – Collect raw weather data from APIs or JSON files (`extract_weather.py`)  
2. **Transform** – Clean, format, and enrich data (`transform_weather.py`)  
3. **Load** – Store transformed data into a MySQL database (`load_weather_mysql.py`)  
4. **Streaming** – Publish and consume weather updates in real-time using **Apache Pulsar**  
   - `publish_weather_pulsar.py`
   - `consume_weather_pulsar.py`

---

## 🧩 Tools & Technologies Used
| Category | Tool |
|-----------|------|
| Programming | Python |
| Data Streaming | Apache Pulsar |
| Database | MySQL |
| Libraries | `pandas`, `mysql-connector-python`, `pulsar-client` |
| Environment | Docker (for Pulsar), VS Code / PowerShell |

---

## 🗂️ Table of Contents
- [Overview](#-overview)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup Instructions](#-setup-instructions)
- [How It Works](#-how-it-works)
- [Demo / Screenshots](#-demo--screenshots)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

---

## 🚀 How to Run the Project

1️⃣ Clone the Repository
git clone https://github.com/Vj0987/weather-etl-project.git
cd weather-etl-project
2️⃣ Set Up Python Environment
pip install pandas mysql-connector-python pulsar-client

3️⃣ Run ETL Pipeline
python extract_weather.py
python transform_weather.py
python load_weather_mysql.py

4️⃣ Start Apache Pulsar (using Docker)
docker run -it -p 6650:6650 -p 8080:8080 --name pulsar-standalone apachepulsar/pulsar:latest bin/pulsar standalone

5️⃣ Publish and Consume Data
python publish_weather_pulsar.py
python consume_weather_pulsar.py

🧠 Key Learning Outcomes

1.Built a fully functional ETL pipeline
2.Implemented data streaming using Apache Pulsar
3.Practiced data transformation with Pandas
4.Integrated Python with MySQL databases
5.Used Docker to manage real-time data infrastructure

📚 Future Enhancements

1.Add a real-time data visualization dashboard (Power BI / Streamlit)
2.Automate the pipeline using Apache Airflow
3.Deploy ETL workflows to the cloud (AWS / GCP)

👨‍💻 Author

Vinit Joshi
🎓 B.Tech in Electronics and Communication
📍 Shri Ramdeobaba College of Engineering and Management
💼 Aspiring Data Engineer | Skilled in Java, DBMS, CN, Python, MySQL, and ETL
