import sheetgetter as sg

def main():
    sheetID = '11hWssHoqyfQSg_LPpymfV6ISUg3Qp6eNjs0qaoD3t3Y'
    sheetName = 'Sheet1'
    
    df = sg.get_sheet(sheetID, sheetName)
    dataList = sg.make_to_list(df)
    
    sort = input('\nWould you like to sort the sheet? Y/N \n')
    if sort.upper() == 'Y':
        how = input('How would you like to sort the sheet?\n')
        df = sg.sorter(how, df)
        
    export = input('\nWould you like to export the sheet? Y/N \n')
    if export.upper() == 'Y':
        sg.make_Json(df)
    
    
    
while True: 
    main()

# 11hWssHoqyfQSg_LPpymfV6ISUg3Qp6eNjs0qaoD3t3Y
# Sheet1

"""



"""