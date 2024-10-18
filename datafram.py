import pandas as pd

class DataFrameInfoe:
    def __init__(self, df):
        self.df = df

    def describe_columns(self):
        """Describe all columns in the DataFrame, including non-null values."""
        return self.df.describe(include='all')

    def extract_statistics(self):
        """Extract key statistical metrics like mean, median, and standard deviation for numeric columns."""
        return self.df.describe().loc[['mean', '50%', 'std']].rename(index={'50%': 'median'})

    def count_distinct_categorical(self):
        """Count distinct values in categorical columns."""
        categorical_columns = self.df.select_dtypes(include='category').columns
        distinct_counts = {col: self.df[col].nunique() for col in categorical_columns}
        return pd.DataFrame({'Column': distinct_counts.keys(), 'Distinct Count': distinct_counts.values()})

    def print_shape(self):
        """Print the shape of the DataFrame."""
        shape = self.df.shape
        print(f"DataFrame shape: {shape[0]} rows, {shape[1]} columns")
        return shape

    def count_null_values(self, percentage=False):
        """Count NULL (missing) values in each column. Optionally, return percentages."""
        null_counts = self.df.isnull().sum()
        if percentage:
            null_percentage = (null_counts / len(self.df)) * 100
            return pd.DataFrame({'Null Count': null_counts, 'Null Percentage': null_percentage})
        else:
            return pd.DataFrame({'Null Count': null_counts})

    def summary(self):
        """Print a quick summary of the DataFrame."""
        # Print the shape of the DataFrame
        self.print_shape()

        # Display the data types and non-null values
        print("\nData Description:")
        print(self.describe_columns())

        # Display NULL value counts
        print("\nNULL Value Counts:")
        print(self.count_null_values())

        # Display distinct values in categorical columns
        print("\nDistinct values in categorical columns:")
        print(self.count_distinct_categorical())

        # Display statistics for numerical columns
        print("\nKey statistics (mean, median, std):")
        print(self.extract_statistics())
