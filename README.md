# Financial Institution Loan Portfolio EDA

## Overview

<p>This project involves an <i>Exploratory Data Analysis (EDA)</i> on the loan portfolio of a financial institution.<br>The aim is to analyse loan data to identify trends, relationships, and anomalies that could assist in making more informed decisions related to (1) loan approvals, (2) pricing, and (3) risk management. By conducting this EDA, insights into loan performance and risk will be gained, ultimately improving the institution's loan portfolio management.</p>
<br>
**Credits**
<p>The knowledge contained in this repository was primarily taught by <a href='https://www.theaicore.com' > AiCore</a>, and I am immensely grateful to them for their teaching and support in my continous professional development.</p>

## Table of Contents

- [Financial Institution Loan Portfolio EDA](#financial-institution-loan-portfolio-eda)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Project Description](#project-description)
  - [Installation Instructions](#installation-instructions)
  - [Usage](#usage)

## Project Description

This project uses Python to connect to a cloud database, extract loan data, and perform exploratory data analysis (EDA). The project aims to identify key insights from the data that will help the business in decision-making regarding loan approvals, pricing, and risk management. The analysis will involve statistical techniques and data visualizations to uncover patterns in the loan data.

Key Learning Outcomes:
- Understanding loan portfolio structure and associated risks.
- Data extraction and analysis techniques.
- Generating insights using Python's data analysis libraries.

## Installation Instructions

To run this project locally, you need to follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/repository.git
    cd repository
    ```

2. Set up a virtual environment with Conda:
    ```bash
    conda create -n finance_loans python=3.8 pyyaml psycopg2 sqlalchemy pandas
    conda activate finance_loans
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure you have a `credentials.yaml` file with your database credentials in the following format:
    ```yaml
    RDS_HOST: "your_host"
    RDS_PORT: "your_port"
    RDS_DATABASE: "your_database"
    RDS_USER: "your_username"
    RDS_PASSWORD: "your_password"
    ```

5. Run the main script:
    ```bash
    python main.py
    ```

This will connect to your cloud database, extract loan data, and save it as a CSV file.

## Usage

To extract the loan data from the cloud database and save it to a CSV file, simply run:

```bash
python main.py
