## load libraries
import sys
import numpy as np
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    '''
    load data function

    Args:
      messages_filepath : location of messages csv file
      categories_filepath : location of categories csv file
    
    Returns:
      df : Pandas DataFrame containing loaded data
    '''
    message = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(message, categories, on='id')

    return df

def clean_data(df):
    '''
    clean data function

    Args:
      df : pandas DataFrame containing raw data
    
    Returns:
      df: cleaned dataset in pandas DataFrame
    '''

    # create a dataframe of the 36 individual category columns
    categories = df.categories.str.split(pat=';',expand=True)
    
    # select the first row of the categories dataframe
    row1 = categories.iloc[0,:]
    
    # use this row to extract a list of new column names for categories
    category_colnames = row1.apply(lambda x:x[:-2])
    
    # rename the columns of 'categories'
    categories.columns = category_colnames
    
    # convert category values to just numbers 0 or 1
    for column in categories:
        categories[column] = categories[column].str[-1]
        categories[column] = categories[column].astype(np.int)

    # drop the original categories column from 'df'
    df = df.drop('categories',axis=1)

    #concatenate the original dataframe with the new 'categories' dataframe
    df = pd.concat([df,categories],axis=1)
    
    # remove duplicates
    df = df.drop_duplicates()
    
    return df

def save_data(df, database_filename):
    pass  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()