#Standard import of a Excel spreadsheet
#Requires Pandas
#Change sheet_name to the name of the specific sheet you want to import
df = pd.read_excel(r'your-directory\file-name.xls', sheet_name='excel-sheet-name')
