import pandas as pd
import os

from fine_tune.preprocess import generate_resources, preprocess_dataset



def test_generate_resources():
    # create a sample dataframe
    df = pd.DataFrame({
        'response_txt': ['response 1', 'response 2'],
        'link': ['link 1', 'link 2']
    })

    # call the function
    generate_resources(df)

    # check if the new column is added
    assert 'promp_with_resources' in df.columns

    # check if the new prompt is generated correctly
    assert df.loc[0, 'promp_with_resources'] == 'response 1\n\nAyrıca bu konuyla ilgili daha fazla bilgi için şu videomuza da göz atabilirsiniz:\nlink 1'
    assert df.loc[1, 'promp_with_resources'] == 'response 2\n\nAyrıca bu konuyla ilgili daha fazla bilgi için şu videomuza da göz atabilirsiniz:\nlink 2'


def test_preprocess_dataset():
    # create a sample excel file
    df = pd.DataFrame({
        'link': ['link 1', 'link 2'],
        'sub_prompt': ['prompt 1', 'prompt 2'],
        'response_txt': ['response 1\n\nAyrıca bu konuyla ilgili daha fazla bilgi için şu videomuza da göz atabilirsiniz:\nlink 1', 'response 2\n\nAyrıca bu konuyla ilgili daha fazla bilgi için şu videomuza da göz atabilirsiniz:\nlink 2']
    })
    df.to_excel('test.xlsx', index=False)

    # call the function
    preprocess_dataset('test.xlsx', 'test.csv')

    # check if the csv file is created
    assert os.path.exists('test.csv')

    # check if the csv file has the correct columns
    csv_df = pd.read_csv('test.csv')
    assert set(csv_df.columns) == set(['prompt', 'completion'])

    # check if the csv file has the correct data
    assert csv_df.loc[0, 'prompt'] == 'prompt 1'
    assert csv_df.loc[0, 'completion'] == f"""{df["response_txt"][0]}
    
    Ayrıca bu konuyla ilgili daha fazla bilgi için şu videomuza da göz atabilirsiniz:
    {df["link"][0]}
    """
    assert csv_df.loc[1, 'prompt'] == 'prompt 2'
    assert csv_df.loc[1, 'completion'] == f"""{df["response_txt"][1]}
    
    Ayrıca bu konuyla ilgili daha fazla bilgi için şu videomuza da göz atabilirsiniz:
    {df["link"][0]}
    """

    # delete the test files
    os.remove('test.xlsx')
    os.remove('test.csv')
