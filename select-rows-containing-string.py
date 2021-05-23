#Select rows in a Pandas DataFrame based on a specific column which contains a specific string
df[df['column_name'].str.contains("your string")] #Add "na=False" to ignore NaN values