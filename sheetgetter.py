import pandas as pd


def get_sheet(sheetID, sheetName):
    SHEET_ID = sheetID
    SHEET_NAME = sheetName
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
    df = pd.read_csv(url)
    
    return df

def make_to_list(df):
    data = df.columns.values.tolist()
    dataList = []
    for column in data:
        dataList.append(df[column].tolist())
    return dataList
    

def sorter(colName, df):
    return df.sort_values(by=[colName])

def make_Json(df):
    df.to_json(r'/Users/ice/Desktop/Thonny_Files/TestFolder/testSheet.json')
    print('Exported file to Json as /Users/ice/Desktop/Thonny_Files/testSheet.json')