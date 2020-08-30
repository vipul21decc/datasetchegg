import pandas as pd # importing pandas for dataset
data_set= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv') # link to dataset
print("HERE IS THE LIST OF DATA \n") # printing the statement
print(data_set.head(10)) # printing or displaying the dataset
