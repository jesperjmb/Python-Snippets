#Standard import of a comma separated CSV file.
#Requires Pandas
#Change delimiter if needed. Common delimiters are comma, tab, and semi-colon.
#Change encoding as needed
df = pd.read_csv('your-directory\file-name.csv', delimiter=',',encoding='utf-8', header = 0, index_col=None)