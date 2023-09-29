import pandas as pd
def missing_and_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform checks on the given data.

    Parameters:
    - data (list): The input data as a dataframe.

    Returns:
    - pd.DataFrame: The cleaned DataFrame.

    """
     # Check for missing values
    if df.isnull().values.any():
        print("Warning: The data contains missing values.")
    else:
        print("No missing values found")
        
    # Check for duplicate rows
    if df.duplicated().any():
        # Remove duplicate rows
        #df.drop_duplicates()
        print("Warning: The data contains duplicate rows.")
    else:
        print("No duplicates found")
        
    return df
def seperate_categories(df: pd.DataFrame) -> pd.DataFrame:
    """This function seperates all the categories in the listed_in column. For each unique category, a column is appended where the value 
    is 1 if the movie was listed in that category and 0 otherwise. 

    Args:
        df (pd.DataFrame): The dataframe with listed_in column

    Returns:
        pd.DataFrame: the dataframe without listed_in column and all categories as columns
    """
    # find all unique categories in the column listed in
    categories = []
    listed_in = df.listed_in.str.split(', ') # per entry: splits all values at ', ' and puts each item in a list 
    for cats in listed_in: # sadly, I have not found a way to do this without a double for-loop
        for elem in cats:
            if elem not in categories:
                categories.append(elem)

    # we make a new column for every category. This column is 1 if the movie or show was listed in that category and 0 otherwise.        
    df_categories = df.iloc[:, :-1]
    df_categories.loc[:, categories] = 0

    for i in listed_in.index: 
        cats = listed_in.loc[i]
        # for each entry in listed_in we put a 1 in the column of all categories
        df_categories.loc[i, cats] = 1
    
    return df_categories # type: ignore # It says that you cannot convert a series to a dataframe

def seperate_movies_tvshows(df: pd.DataFrame) -> tuple:
    """Seperates the dataset into a movies and tvshows dataset.

    Args:
        df (pd.DataFrame): original data frame with both data about movies and tv shows

    Returns:
        tuple: movies and tv shows dataframe
    """
    movies = df[df.type == 'Movie']
    tvshows = df[df.type == 'TV Show']
    
    #method 2: we do the same thing, but use the build in string functions from pandas. This is much faster!
    movies.loc[:, 'duration'] = movies.loc[:, 'duration'].str[:-4].astype(int)
    
    # We also use method 2 for the tvshows
    tvshows.loc[:, 'duration'] = tvshows.loc[:, 'duration'].str[:-7].astype(int)
    
    return (movies, tvshows)
    


def clean(filename: str = 'netflix1.csv') -> pd.DataFrame:
    """This function cleans a dataset in the format of netflix1.csv. This function can be used if a new iteration of this dataset needs to be cleaned.

    Args:
        filename (str, optional): filename of netflix dataset that needs to be cleaned. Defaults to 'netflix1.csv'.

    Returns:
        pd.DataFrame: cleaned dataset
    """
    df = pd.read_csv(filename)
    df= missing_and_duplicates(df)
    df = seperate_categories(df)
    return df
    
def convert_dates_to_datetime(date_series, date_format = '%m/%d/%Y'):
    return pd.to_datetime(date_series, format = date_format)

