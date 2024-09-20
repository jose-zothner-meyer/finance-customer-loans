import yaml
import pandas as pd
from sqlalchemy import create_engine

def load_credentials(config_path="credentials.yaml"):
    '''
    This function loads database credentials from a YAML file.
    
    Parameters:
    config_path (str): The path to the credentials YAML file (default is "credentials.yaml").

    Returns:
    dict: A dictionary containing the database connection details (host, port, user, password, etc.).
    '''
    with open(config_path, "r") as file:
        credentials = yaml.safe_load(file)
    return credentials

class RDSDatabaseConnector:
    '''
    This class manages the connection to the database and provides methods to extract data.

    Attributes:
    host (str): The database host (IP address or domain name).
    port (str): The port number for connecting to the database.
    database (str): The name of the database to connect to.
    user (str): The username for database authentication.
    password (str): The password for database authentication.
    engine: The SQLAlchemy engine used to connect to the database.
    '''

    def __init__(self, credentials):
        '''
        Initialize the RDSDatabaseConnector class with the database credentials.

        Parameters:
        credentials (dict): A dictionary containing the database connection details (host, port, user, password, etc.).
        '''
        self.host = credentials['RDS_HOST']
        self.port = credentials['RDS_PORT']
        self.database = credentials['RDS_DATABASE']
        self.user = credentials['RDS_USER']
        self.password = credentials['RDS_PASSWORD']
        self.engine = self.create_engine()

    def create_engine(self):
        '''
        Create a connection to the database using SQLAlchemy.

        This method creates an SQLAlchemy engine, which is an object that handles the connection to the database.

        Returns:
        engine: The SQLAlchemy engine used for database operations.
        '''
        db_url = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        engine = create_engine(db_url)
        return engine

    def extract_data(self, table_name="loan_payments"):
        '''
        Extract data from a specified table in the database and return it as a Pandas DataFrame.

        This method connects to the database and runs a SQL query to get all the data from the specified table.

        Parameters:
        table_name (str): The name of the table to extract data from (default is "loan_payments").

        Returns:
        pd.DataFrame: A Pandas DataFrame containing the data from the specified table.
        '''
        query = f"SELECT * FROM {table_name}"
        
        # Using the context manager to automatically handle connection closing
        with self.engine.connect() as connection:
            df = pd.read_sql(query, connection)
        return df

def save_to_csv(df, file_path="loan_payments.csv"):
    '''
    Save the data in a Pandas DataFrame to a CSV file.

    This function saves the extracted data to a local CSV file for later use or analysis.

    Parameters:
    df (pd.DataFrame): The Pandas DataFrame containing the data to save.
    file_path (str): The file path where the CSV file should be saved (default is "loan_payments.csv").
    '''
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")