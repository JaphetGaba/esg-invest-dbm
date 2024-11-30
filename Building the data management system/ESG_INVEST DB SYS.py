#################################### INVESTMENT DATASET##############################

import pandas as pd
import random

# Set random seed for reproducibility
random.seed(42)

# Parameters for dataset generation
num_records = 20000
companies = [f"Company_{i}" for i in range(1, 101)]  # 100 companies
financial_instruments = [
    "Swaps", "Commitments", "Mortgages", "Fixed Income", 
    "Equities", "Derivatives", "Bonds", "Commodities", 
    "Options", "Futures"
]
stock_exchanges = [
    "NYSE", "NASDAQ", "LSE", "HKEX", "TSX", "ASX", "BSE", "NSE", 
    "JPX", "SSE"
]
currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CNY", "INR"]


data = []
for _ in range(num_records):
    record = {
        "Company": random.choice(companies),
        "Financial_Instrument": random.choice(financial_instruments),
        "Stock_Exchange": random.choice(stock_exchanges),
        "Investment_Amount": round(random.uniform(1e5, 1e7), 2),  # Random amount between $100k and $10M
        "Currency": random.choice(currencies),
        "Investment_Date": pd.Timestamp(
            year=random.randint(2010, 2023),
            month=random.randint(1, 12),
            day=random.randint(1, 28)
        ).date()
    }
    data.append(record)

# Create DataFrame
df = pd.DataFrame(data)

# Save dataset to CSV for later use
df.to_csv("investment_dataset.csv", index=False)

# Display the first few rows
print(df.head())


############################# ESG DATASET####################################


import pandas as pd
import random

# Set random seed for reproducibility
random.seed(42)

# Parameters for ESG dataset generation
esg_metrics = [
    "Carbon_Emissions_Score", "Water_Usage", "Energy_Efficiency_Score", 
    "Waste_Management_Score", "Diversity_Equity_Inclusion_Score", 
    "Governance_Score", "ESG_Disclosure_Score", "Human_Rights_Score", 
    "Labor_Practices_Score", "Sustainable_Products_Score", 
    "Renewable_Energy_Percentage", "Community_Engagement_Score", 
    "Cybersecurity_Score", "Transparency_Score"
]
num_esg_records = 20000

# Reuse the company list from the investment dataset
companies = [f"Company_{i}" for i in range(1, 101)]

# Generate ESG dataset
esg_data = []
for _ in range(num_esg_records):
    record = {
        "Company": random.choice(companies),
        "Carbon_Emissions_Score": round(random.uniform(50, 100), 2),  # Score out of 100
        "Water_Usage": round(random.uniform(1000, 50000), 2),  # Liters
        "Energy_Efficiency_Score": round(random.uniform(50, 100), 2),
        "Waste_Management_Score": round(random.uniform(50, 100), 2),
        "Diversity_Equity_Inclusion_Score": round(random.uniform(50, 100), 2),
        "Governance_Score": round(random.uniform(50, 100), 2),
        "ESG_Disclosure_Score": round(random.uniform(50, 100), 2),
        "Human_Rights_Score": round(random.uniform(50, 100), 2),
        "Labor_Practices_Score": round(random.uniform(50, 100), 2),
        "Sustainable_Products_Score": round(random.uniform(50, 100), 2),
        "Renewable_Energy_Percentage": round(random.uniform(0, 100), 2),  # Percentage
        "Community_Engagement_Score": round(random.uniform(50, 100), 2),
        "Cybersecurity_Score": round(random.uniform(50, 100), 2),
        "Transparency_Score": round(random.uniform(50, 100), 2)
    }
    esg_data.append(record)

# Create ESG DataFrame
esg_df = pd.DataFrame(esg_data)

# Save ESG dataset to CSV
csv_file = "esg_dataset.csv"
esg_df.to_csv(csv_file, index=False)

print(f"ESG Dataset exported to {csv_file}")

# Display the first few rows
print(esg_df.head())





# STEP TO EXTRACT,LOAD AND TRANSFORM ESG AND INVESTMENT DATA (ETL PROCESS)######
#################################### CONNECTING SQL SERVER, EXTRACTION, LOADING AND TRANSFORMATION ##############################

####################################CONNECTING SQL SERVER #############################
import pandas as pd
import pyodbc

# Database connection details for trusted connection (Windows Authentication)
server = 'localhost\\SQLEXPRESS'  # Change this to your SQL Server instance
database = 'Investment_ESG_DB'  # The database name

# Create a connection to SQL Server using Trusted Connection
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes'
)

cursor = conn.cursor()


#################################### EXTRACTION; LOADING AND TRANSFORMATION ##############################
import pandas as pd
import pyodbc

# Database connection details
server = 'localhost\\SQLEXPRESS'  # Change this to your SQL Server instance
database = 'Investment_ESG_DB'    # Your database name

# Create a connection to SQL Server using Trusted Connection
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes'
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# --- Step 1: Create ESG_DATA Table if it doesn't exist ---
create_esg_table_sql = '''
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'ESG_DATA' AND xtype = 'U')
BEGIN
    CREATE TABLE ESG_DATA (
        Company VARCHAR(255),
        Carbon_Emissions_Score FLOAT,
        Water_Usage FLOAT,
        Energy_Efficiency_Score FLOAT,
        Waste_Management_Score FLOAT,
        Diversity_Equity_Inclusion_Score FLOAT,
        Governance_Score FLOAT,
        ESG_Disclosure_Score FLOAT,
        Human_Rights_Score FLOAT,
        Labor_Practices_Score FLOAT,
        Sustainable_Products_Score FLOAT,
        Renewable_Energy_Percentage FLOAT,
        Community_Engagement_Score FLOAT,
        Cybersecurity_Score FLOAT,
        Transparency_Score FLOAT
    )
END
'''

cursor.execute(create_esg_table_sql)
conn.commit()

# --- Step 2: Create Investment_DATA Table if it doesn't exist ---
create_investment_table_sql = '''
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = 'Investment_DATA' AND xtype = 'U')
BEGIN
    CREATE TABLE Investment_DATA (
        Company VARCHAR(255),
        Currency VARCHAR(10),
        Financial_Instrument VARCHAR(255),
        Investment_Amount DECIMAL(18, 2),
        Investment_Date DATE,
        Stock_Exchange VARCHAR(50)
    )
END
'''

cursor.execute(create_investment_table_sql)
conn.commit()

# --- Step 3: Load and Clean ESG Data ---
# Load ESG data from CSV
esg_file_path = r'C:\Users\thierry\Desktop\Project Folder Investment and ESG\esg_dataset.csv'
esg_df = pd.read_csv(esg_file_path)

# Clean ESG data: Handle missing or incorrect data
# You can apply additional transformations here based on your specific dataset
esg_df = esg_df.fillna(0)  # Replace missing values with 0

# Insert ESG data into ESG_DATA table
for index, row in esg_df.iterrows():
    insert_esg_sql = '''
    INSERT INTO ESG_DATA (
        Company, Carbon_Emissions_Score, Water_Usage, Energy_Efficiency_Score, 
        Waste_Management_Score, Diversity_Equity_Inclusion_Score, Governance_Score, 
        ESG_Disclosure_Score, Human_Rights_Score, Labor_Practices_Score, 
        Sustainable_Products_Score, Renewable_Energy_Percentage, 
        Community_Engagement_Score, Cybersecurity_Score, Transparency_Score
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_esg_sql, tuple(row))
    conn.commit()

print("ESG data inserted successfully.")

# --- Step 4: Load and Clean Investment Data ---
# Load Investment data from CSV
investment_file_path = r'C:\Users\thierry\Desktop\Project Folder Investment and ESG\investment_dataset.csv'
investment_df = pd.read_csv(investment_file_path)

# Clean Investment data: Ensure 'Investment_Amount' is numeric and handle missing values
investment_df['Investment_Amount'] = pd.to_numeric(investment_df['Investment_Amount'], errors='coerce')
investment_df = investment_df.dropna(subset=['Investment_Amount'])

# Convert 'Investment_Date' to datetime format
investment_df['Investment_Date'] = pd.to_datetime(investment_df['Investment_Date'], errors='coerce')
investment_df = investment_df.dropna(subset=['Investment_Date'])

# Insert Investment data into Investment_DATA table
for index, row in investment_df.iterrows():
    insert_investment_sql = '''
    INSERT INTO Investment_DATA (
        Company, Currency, Financial_Instrument, Investment_Amount, Investment_Date, Stock_Exchange
    ) VALUES (?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_investment_sql, tuple(row))
    conn.commit()

print("Investment data inserted successfully.")

# Close the connection
cursor.close()
conn.close()

