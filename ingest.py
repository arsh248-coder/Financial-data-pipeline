import yfinance as yf
import pandas as pd
import snowflake.connector

# --- 1. CONFIGURATION ---
import os
from dotenv import load_dotenv
load_dotenv()

USER = os.getenv('SNOWFLAKE_USER')
PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
tickers = ['AAPL', 'MSFT', 'TSLA', 'GOOGL']
# --- 2. FETCH DATA ---
try:
    print("Connecting to Snowflake...")
    ctx = snowflake.connector.connect(
        user=USER, password=PASSWORD, account=ACCOUNT,
        warehouse='COMPUTE_WH', database='FINANCIAL_DATA', schema='RAW'
    )
    cs = ctx.cursor()

    # --- 3. LOOP THROUGH TICKERS ---
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        df = yf.download(ticker, period='1mo')
        df = df.reset_index() 
        df['TICKER'] = ticker

        df = df[['TICKER', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
        df.columns = ['TICKER', 'DATE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME']

        print(f"Uploading {ticker} to Snowflake...")
        for _, row in df.iterrows():
            sql = f"""
            INSERT INTO FINANCIAL_DATA.RAW.STOCK_PRICES 
            (TICKER, DATE, OPEN, HIGH, LOW, CLOSE, VOLUME) 
            VALUES ('{row['TICKER']}', '{row['DATE'].date()}', {row['OPEN']}, {row['HIGH']}, {row['LOW']}, {row['CLOSE']}, {row['VOLUME']})
            """
            cs.execute(sql)
        ctx.commit()
    
    print("Success! All data ingested.")

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'cs' in locals(): cs.close()
    if 'ctx' in locals(): ctx.close()