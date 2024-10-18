import pandas as pd

class DataTransforme:
    def __init__(self, df):
        self.df = df

    def convert_to_datetime(self, columns):
        """Convert the specified columns to datetime format."""
        for col in columns:
            self.df[col] = pd.to_datetime(self.df[col], errors='coerce')
        return self.df

    def convert_to_category(self, columns):
        """Convert the specified columns to category format."""
        for col in columns:
            self.df[col] = self.df[col].astype('category')
        return self.df

    def clean_term_column(self, column):
        """Remove excess symbols from the 'term' column and convert to numeric."""
        self.df[column] = self.df[column].str.extract(r'(\d+)').astype(float)
        return self.df

    def clean_employment_length(self, column):
        """Clean employment_length column to retain only numeric values."""
        self.df[column] = self.df[column].str.extract(r'(\d+)').fillna(0).astype(float)
        return self.df
