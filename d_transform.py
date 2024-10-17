import pandas as pd

class DataTransform:
    def __init__(self, df):
        self.df = df

    def convert_to_datetime(self, column_list):
        """
        Converts specified columns to datetime format.
        
        Args:
        column_list (list): List of column names to convert.
        
        Returns:
        None: Updates the DataFrame in place.
        """
        for column in column_list:
            self.df[column] = pd.to_datetime(self.df[column], format='%b-%Y', errors='coerce')

    def clean_term_column(self):
        """
        Converts the 'term' column to an integer by removing the 'months' text.
        
        Returns:
        None: Updates the DataFrame in place.
        """
        self.df['term'] = self.df['term'].str.replace(' months', '', regex=False).astype(float)

    def convert_to_categorical(self, column_list):
        """
        Converts specified columns to categorical data type.
        
        Args:
        column_list (list): List of column names to convert.
        
        Returns:
        None: Updates the DataFrame in place.
        """
        for column in column_list:
            self.df[column] = self.df[column].astype('category')

    def handle_missing_values(self, columns, fill_value=None):
        """
        Handles missing values in specified columns. Optionally fills missing values.
        
        Args:
        columns (list): List of columns to check for missing values.
        fill_value (various): Value to fill missing data with (default: None, keeps NaN).
        
        Returns:
        None: Updates the DataFrame in place.
        """
        for column in columns:
            if fill_value is not None:
                self.df[column] = self.df[column].fillna(fill_value)
            else:
                self.df[column] = self.df[column]  # No action taken, just leaves NaN in place.