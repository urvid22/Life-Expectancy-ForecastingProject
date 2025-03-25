# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

# %%
pip install xlrd

# %%
femaledf = pd.read_excel(r'C:\Users\urvi9\Downloads\FemaleDataset.xls', header=3)
femaledf.head()

# %%
maledf = pd.read_excel(r'C:\Users\urvi9\Downloads\MaleDataset.xls', header=3)
maledf.head()

# %%
# Melt the female dataset from wide to long format
female_long = pd.melt(femaledf, 
                      id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], 
                      var_name='Year', 
                      value_name='Life Expectancy Female')

female_long

# %%
male_long = pd.melt(maledf, 
                      id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], 
                      var_name='Year', 
                      value_name='Life Expectancy Male')

male_long

# %%
columns_to_drop = ['Indicator Name', 'Indicator Code']
female_long.drop(columns=columns_to_drop, inplace=True)

columns_to_drop = ['Indicator Name', 'Indicator Code']
male_long.drop(columns=columns_to_drop, inplace=True)


# %%
male_long['Year'] = pd.to_numeric(male_long['Year'], errors='coerce')
male_long.fillna(0, inplace=True)
male_long

# %%
female_long['Year'] = pd.to_numeric(female_long['Year'], errors='coerce')
female_long.fillna(0, inplace=True)
female_long

# %%
female_long.info()

# %%
#Merge the datasets on 'Country Name' and 'Year'
#merged_data = pd.merge(female_long, male_long, on=["Country Name", "Country Code", "Year"])
#merged_data

# %%
tempdf = pd.read_csv(r'C:\Users\urvi9\Downloads\Annual_Surface_Temperature_Change.csv')
tempdf.head()

# %%
tempdf.info()

# %%
tempdf_long = pd.melt(tempdf, 
                     id_vars=['ObjectId', 'Country', 'ISO2', 'ISO3', 'Indicator', 'Unit', 'Source', 
                              'CTS_Code', 'CTS_Name', 'CTS_Full_Descriptor'], 
                     value_vars=[f'F{year}' for year in range(1961, 2023)],  
                     var_name='Year', 
                     value_name='Temperature Change')

# Adjust the 'Year' column to extract just the year number
tempdf_long['Year'] = tempdf_long['Year'].str[1:]  # Remove 'F'
tempdf_long.head()

# %%
columns_to_drop = ['ObjectId', 'ISO2','CTS_Code','CTS_Name','Unit','CTS_Full_Descriptor','Source']
tempdf_long.drop(columns=columns_to_drop, inplace=True)
tempdf_long['Year'] = pd.to_numeric(tempdf_long['Year'], errors='coerce')
tempdf_long.fillna(0, inplace=True)
tempdf_long

# %%
male_long.to_excel('male_long.xlsx', index=False)
female_long.to_excel('female_long.xlsx', index=False)
tempdf_long.to_excel('tempdf_long.xlsx', index=False)



