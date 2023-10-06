import pandas as pd
import numpy as np

def calculate_percentage_sales(data_frame, group_by_column, value_column):
    """
    Calculate percentage sales for a specific column grouped by another column.
    
    Parameters:
        data_frame (DataFrame): The DataFrame containing the data.
        group_by_column (str): The column to group by.
        value_column (str): The column for which to calculate percentage sales.
    
    Returns:
        DataFrame: A DataFrame with group-wise percentage sales.
    """
    group_sales = data_frame.groupby(group_by_column)[value_column].sum().reset_index()
    total_sales = group_sales[value_column].sum()
    group_sales['Percentage Sales'] = (group_sales[value_column] / total_sales) * 100
    return group_sales

def write_to_excel(data_frame, sheet_name, excel_writer):
    """
    Write a DataFrame to an Excel sheet.
    
    Parameters:
        data_frame (DataFrame): The DataFrame to be written.
        sheet_name (str): The name of the Excel sheet.
        excel_writer (ExcelWriter): The Excel writer object.
    """
    data_frame.to_excel(excel_writer, sheet_name=sheet_name, index=False)

# Read the Excel file into a DataFrame
df = pd.read_excel('detailedRetail.xlsx')

# Calculate category sales and percentages
category_sales = calculate_percentage_sales(df, 'Category', 'Sales')

# Calculate monthly sales and percentages
month_sales = calculate_percentage_sales(df, 'Month', 'Sales')

# Calculate manager sales and percentages
manager_sales = calculate_percentage_sales(df, 'Sales Manager', 'Sales')

# Create an Excel writer object
with pd.ExcelWriter('reportRetail.xlsx') as writer:
    # Write category sales data to the first sheet
    write_to_excel(category_sales, 'Category Sales', writer)

    # Write monthly sales data to the second sheet
    write_to_excel(month_sales, 'Monthly Sales', writer)

    # Write sales manager data to the third sheet
    write_to_excel(manager_sales, 'Sales Manager Sales', writer)
