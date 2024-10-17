import pandas as pd

class DataFrameInfo:
    def __init__(self, df):
        """
        Initialize the DataFrameInfo class with a DataFrame.
        
        Args:
        df (pd.DataFrame): The DataFrame to analyze.
        """
        self.df = df

    def describe_columns(self):
        """
        Returns a description of all columns, including data types.
        
        Returns:
        pd.DataFrame: DataFrame with column descriptions.
        """
        return self.df.info()

    def extract_statistics(self):
        """
        Returns the mean, median, and standard deviation for numerical columns.
        
        Returns:
        pd.DataFrame: DataFrame with the mean, median, and standard deviation.
        """
        stats = self.df.describe().T
        stats['median'] = self.df.median()
        stats['mean'] = self.df.mean()
        stats['std'] = self.df.std()
        return stats[['mean', 'median', 'std']]

    def count_distinct_categorical(self):
        """
        Counts distinct values in all categorical columns.
        
        Returns:
        pd.DataFrame: DataFrame with column names and their distinct value counts.
        """
        categorical_columns = self.df.select_dtypes(include='category').columns
        return self.df[categorical_columns].nunique()

    def print_shape(self):
        """
        Prints the shape (rows, columns) of the DataFrame.
        """
        print(f"The DataFrame has {self.df.shape[0]} rows and {self.df.shape[1]} columns.")

    def count_null_values(self, percentage=False):
        """
        Returns the count (or percentage) of NULL values in each column.
        
        Args:
        percentage (bool): If True, return percentage of NULL values. Default is False.
        
        Returns:
        pd.Series: Series with column names and their NULL value counts or percentages.
        """
        if percentage:
            return (self.df.isnull().sum() / len(self.df)) * 100
        else:
            return self.df.isnull().sum()

    def summary(self):
        """
        Prints a quick summary of the DataFrame including shape, null values, and column data types.
        """
        print("---- DataFrame Summary ----")
        self.print_shape()
        print("\nNull Values Count:\n", self.count_null_values())
        print("\nColumn Descriptions:\n")
        self.describe_columns()
