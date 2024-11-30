# ESG and Investment Data Management System

**ESG and Investment Data Management System** is a AI and Data management-based solution designed to manage and integrate ESG (Environmental, Social, and Governance) and Investment data. The system 	ports financial institutions and organizations focused on sustainability and compliance.

---

## Key Features

- **Comprehensive ESG and Investment Integration**: Combines ESG metrics with investment data to facilitate informed decision-making.
- **Data Validation and Transformation**: Ensures high-quality, clean, and consistent data.
- **SQL Server Database Integration**: Creates and populates ESG and Investment tables in a secure SQL Server environment.
- **Customizable and Scalable**: Supports expanding datasets and schema modifications.
- **Advanced Analytics Support**: Prepares data for advanced insights, including risk assessments and regulatory reporting.

---

## Getting Started

### Prerequisites
Ensure you have the following:
- Python 3.7+
- Pandas (for data manipulation)
- pyodbc (for database connectivity)
- Microsoft SQL Server (as the target database)

### Setup

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/esg-investment-system.git
   cd esg-investment-system
   ```

2. **Install Dependencies** 

	Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```
	
3. **Configure Database Connection**

	Update the database_config.py file with your SQL Server connection details:
	
	```python
    database_config = {
    "server": "your_server_name",
    "database": "Investment_ESG_DB",
    "username": "your_username",
    "password": "your_password",
    "driver": "ODBC Driver 17 for SQL Server"
	}
    ```

### Usage

## Step 1: Run the ETL Process

	The ETL script automates the following:

	Creates ESG_DATA and Investment_DATA tables in the Investment_ESG_DB database.
	Inserts clean and validated data from CSV files into the database.
	
	Run the script:
	
	```bash
	python etl_script.py
    ```

# Database Schema

## ESG_DATA TABLE
| Column            | Type            | Description                                              |
|--------------------|-----------------|----------------------------------------------------------|
| ESG_ID            | INT (Primary Key) | Unique identifier for ESG records.                      |
| Company           | NVARCHAR(255)   | Name of the company associated with ESG metrics.         |
| ESG_Category      | NVARCHAR(100)   | ESG dimension (e.g., Environmental, Social).             |
| ESG_Score         | DECIMAL(5, 2)   | ESG score indicating performance.                        |
| Evaluation_Date   | DATE            | Date of ESG evaluation.                                  |

## INVESTMENT_DATA TABLE
| Column               | Type            | Description                                              |
|-----------------------|-----------------|----------------------------------------------------------|
| Investment_ID        | INT (Primary Key) | Unique identifier for investment records.               |
| Company              | NVARCHAR(255)   | Name of the company involved in the investment.          |
| Currency             | NVARCHAR(10)    | Currency used for the investment amount.                 |
| Financial_Instrument | NVARCHAR(100)   | Type of financial instrument (e.g., Options).            |
| Investment_Amount    | DECIMAL(18, 2)  | Total investment amount.                                 |
| Investment_Date      | DATE            | Date of the investment.                                  |
| Stock_Exchange       | NVARCHAR(50)    | Stock exchange where the transaction occurred.           |

## How It Works
1. *Extract*: Reads raw ESG and Investment data from CSV files.
2. *Transform*: Cleans and validates the data, including:
   - Handling missing values.
   - Formatting dates and currency values.
   - Converting data to match table schema.
3. *Load*: Inserts the processed data into the respective tables in SQL Server.

## Example Scenarios
- *Sustainability Reporting*: Generate reports integrating ESG and financial metrics to meet compliance standards and enhance transparency.
- *Investment Risk Analysis*: Use combined ESG and financial data to assess climate-related, governance, and social risks, aiding in better decision-making.
- *Data Analytics*: Enable predictive modeling and advanced analytics with a unified data repository to forecast trends and impacts.
- *Climate Resilience*: Model and disclose climate-related risks, helping entities align with U.S. SEC and global climate action goals.
- *Economic Stability*: Promote sustainable investment to enhance financial resilience against resource scarcity and climate change.
- *Equity and Inclusion*: Facilitate investments that address social inequality, environmental justice, and public health disparities.
- *Global ESG Standards*: Contribute to harmonizing global reporting frameworks, enabling international collaboration and investment.
- *Energy Independence*: Identify opportunities for renewable energy development, supporting national security and sustainability goals.
- *Carbon Footprint Reduction*: Provide tools to measure and mitigate emissions, aligning with international climate agreements.
- *Ethical AI in ESG*: Pioneer explainable AI for ESG data analysis, ensuring transparency and accountability in decision-making.
- *Capacity Building*: Share tools and methodologies globally to improve ESG data quality and foster sustainable development, particularly in emerging markets.

## Contributing
We welcome contributions! Please fork the repository and submit a pull request to suggest enhancements or fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.