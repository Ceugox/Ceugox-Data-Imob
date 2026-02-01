# RCP Data Imob: Real Estate Analytics Pipeline

This project is an end-to-end data solution designed to optimize residential relocation decisions in Rio de Janeiro. It bridges the gap between raw real estate listings and socio-economic urban data.

## 🛠️ Tech Stack
* **Language:** Python (Selenium)
* **Database:** PostgreSQL (Neon Cloud)
* **ETL:** SQL (Views/Triggers) & Power Query
* **Design & BI:** Figma & Power BI

## 🏗️ Project Architecture
1. **Ingestion:** Automated scraping of local real estate agencies using **Selenium**.
2. **Pipeline:** A cloud-native **PostgreSQL** setup on Neon using **Views and Triggers** for automated data cleaning and lightweight Power BI integration.
3. **Enrichment:** Integration with **ITBI Rio** (historical transaction data) and **Data_Rio** (median household income) to calculate fair market value and neighborhood well-being.

## 💡 Strategic Insight
The project identifies a "Downtown Anomaly": a high-value real estate hub with a low-income residential profile, indicating a commuter-driven economy. The dashboard highlights regions where current prices are below historical averages, pinpointing specific investment opportunities.

---
*Inspired by Database I (IME) and technical guidance from José Nilton Gonçalves de Andrade.*
