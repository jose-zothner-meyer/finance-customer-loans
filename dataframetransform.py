import pandas as pd

class DataFrameTransform:
    def __init__(self, df):
        self.df = df

    def check_nulls(self):
        """Determine the amount of NULLs in each column."""
        null_counts = self.df.isnull().sum()
        null_percentage = (null_counts / len(self.df)) * 100
        return pd.DataFrame({'Null Count': null_counts, 'Null Percentage': null_percentage})

    def drop_columns_with_nulls(self, threshold=50.0):
        """Drop columns with more than a threshold percentage of NULLs."""
        null_percentage = (self.df.isnull().sum() / len(self.df)) * 100
        columns_to_drop = null_percentage[null_percentage > threshold].index
        self.df = self.df.drop(columns=columns_to_drop)
        return self.df

    def impute_missing_values(self):
        """Impute missing values with mean or median based on column type."""
        for column in self.df.columns:
            if self.df[column].dtype in ['float64', 'int64']:
                # Use median if the column is numeric
                median_value = self.df[column].median()
                self.df[column].fillna(median_value, inplace=True)
            elif self.df[column].dtype == 'category' or self.df[column].dtype == 'object':
                # For categorical columns, we can use the most frequent value (mode)
                mode_value = self.df[column].mode()[0]
                self.df[column].fillna(mode_value, inplace=True)
        return self.df

    def save_cleaned_data(self, file_path):
        """Save the cleaned DataFrame."""
        self.df.to_csv(file_path, index=False)
