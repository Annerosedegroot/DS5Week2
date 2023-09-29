import pandas as pd

def generate_sales_report(file_path):
    """
    Generates a sales report based on data from an Excel file.

    Args:
        file_path (str): The path to the Excel file.

    Returns:
        pd.DataFrame: The sales report containing total sales and contribution.
    """
    # Read the Excel file
    data = pd.read_excel(file_path)

    # Perform post-processing and calculations
    category_sales = data.groupby('Category')['Sales'].sum()
    total_sales = category_sales.sum()
    category_contributions = category_sales / total_sales * 100

    # Generate the report
    report = pd.DataFrame({'Total Sales': category_sales, 'Contribution (%)': category_contributions})

    return report

# Example usage
file_path = "retail.xlsx"
report = generate_sales_report(file_path)
print(report)
