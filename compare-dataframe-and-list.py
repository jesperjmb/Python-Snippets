#Compare a pandas dataframe column witn a list
#Requires Pandas

#Creating example DataFrame
df = pd.DataFrame([['panda', 'python'], ['shark', 'panda'], ['crocodile', 'python']], columns=['A', 'B'])

#Creating example list
animal_list = ['panda', 'crocodile']

#Select only values that ARE in the list
df_incl = df[df.isin(animal_list)]

#Select only value that are NOT in the list
df_excl = df[~df.isin(animal_list)]

#Based on a specific column, select all rows that have values that ARE in the list
df_incl = df[df['A'].isin(animal_list)]

#Based on a specific column, select all rows that have values that are NOT in the list
df_excl = df[df['A'].isin(animal_list)]
