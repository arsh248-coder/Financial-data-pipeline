# Financial Data ELT Pipeline

A modular, automated data engineering pipeline designed to ingest, transform, and store stock market data from Yahoo Finance into a Snowflake cloud data warehouse.

## Project Overview
This project demonstrates an end-to-end ELT (Extract, Load, Transform) workflow. It automates the extraction of historical stock data, loads it into a raw landing zone in Snowflake, and structures it for analytical consumption.

## Tech Stack
* **Language:** Python 3.x
* **Data Handling:** `pandas`, `yfinance`
* **Warehouse:** Snowflake
* **Security:** `python-dotenv` for environment variable management
* **Version Control:** Git/GitHub

## Key Features
* **Modular Ingestion:** Python script handles API calls and batch loading into Snowflake with robust error handling.
* **Security-First Approach:** Uses `.env` and `.gitignore` to ensure sensitive credentials are never exposed in source control.
* **Scalable Architecture:** Designed for easy cloud-based data storage and analysis.

## How to Run
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install pandas yfinance snowflake-connector-python python-dotenv
