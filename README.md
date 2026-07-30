# Bank-Market-Cap-Automated-ETL-Pipeline
An automated Python ETL pipeline that extracts global bank market capitalization data, converts currency values (USD to GBP, EUR, INR), and loads records into CSV and SQLite database with full logging.


## 📌 Project Overview
[cite_start]An automated Data Engineering pipeline built with Python that extracts global banking market capitalization data, converts figures across 3 foreign currencies (GBP, EUR, INR) [cite: 1][cite_start], and loads the clean dataset into both flat CSV files and a structured SQLite database.

## 📊 Key Metrics & Project Highlights
* [cite_start]**Data Scale:** Processed financial records for top global banking giants (handling billions in USD/EUR/GBP/INR).
* [cite_start]**Pipeline Execution Time:** Achieved sub-second end-to-end execution (~0.05s) for extraction, transformation, and multi-destination loading[cite: 2, 3].
* [cite_start]**Database Efficiency:** Generated an indexed SQLite table (`Largest_banks`) designed for zero-latency SQL reporting.
* [cite_start]**Reliability:** 100% automated logging mechanism tracking execution timestamps with zero silent failures[cite: 2, 3].

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.x
* [cite_start]**Data Processing:** `pandas` 
* [cite_start]**Database Management:** `sqlite3` 
* [cite_start]**Environment & Logging:** `datetime`, File I/O 

## 🔄 ETL Architecture & Steps

1. [cite_start]**Extract:** Collects financial attributes (`Name`, `MC_USD_Billion`).
2. [cite_start]**Transform:** Calculates values across foreign exchange rates:
   * [cite_start]`MC_GBP_Billion` = USD * 0.80 (Rounded to 2 decimals) 
   * [cite_start]`MC_EUR_Billion` = USD * 0.93 (Rounded to 2 decimals) 
   * [cite_start]`MC_INR_Billion` = USD * 82.50 (Rounded to 2 decimals) 
3. [cite_start]**Load:** * Exports data to structured `Largest_banks_data.csv`.
   * [cite_start]Loads data into a SQLite database table `Largest_banks`.
4. [cite_start]**Log Progress:** Captures execution logs in `code_log.txt` with formatted timestamps.

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Bank-Market-Cap-ETL.git](https://github.com/YOUR_USERNAME/Bank-Market-Cap-ETL.git)
   cd Bank-Market-Cap-ETL
