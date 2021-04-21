#import statements for required packages
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

#COVID Act Now - COVID-19 API Key Parameter
key = #you will need your own API key; get for free by signing up for website

#http GET request for all state data for each day in calendar year 2020
states_url = 'https://api.covidactnow.org/v2/states.timeseries.csv?apiKey='+key
r_states = requests.get(states_url)
print(f'GET requests status code: {r_states.status_code}')

#save the results of that GET request as a csv file
today = datetime.now().date() #return today's date in ISO format
with open(f'all_states_timeseries_{today}.csv', 'xt') as f1:
  for line in r_states.text:
    f1.write(line)
#this csv file contans the metrics for all 50 states for every day in 2020

#http GET requests for all county data for each day in calendar year 2020
counties_url = 'https://api.covidactnow.org/v2/counties.timeseries.csv?apiKey='+key
r_counties = requests.get(counties_url)
print(f'GET requests status code:{r_counties.status_code}')

#save results to CSV file
today = datetime.now().date() #return today's date in ISO format
with open(f'all_counties_timeseries_{today}.csv', 'xt') as f2:
  for line in r_counties.text:
    f2.write(line)
#this csv file contans the metrics for all counties in the US ea day in 2020

#load states csv file into pandas dataframe
state_data = pd.read_csv(f'/content/all_states_timeseries_{today}.csv')
#create a new dataframe for data from state of Virginia
WI_data = state_data[state_data['state'] == 'WI']
#load counties csv files into pandas dataframe
county_data = pd.rea

#visualization of data as a line graph with Seaborn
sns.set_theme(style='darkgrid')
sns.set_palette("flare", 5)
plt.figure(figsize=(18,9))
plot = sns.lineplot(data=caseDensity)
plt.xlabel("Date", size=18)
plt.ylabel("Cases per 100K People", size=18)
plt.title("COVID-19 Cases: Wisconson vs. Dane County", size=24)
#set the limit and ticks of the x-and y-axis
len = caseDensity.shape[0]
plot.set(xticks=list(range(0,(len+30),30)))d_csv(f'/content/all_counties_timeseries_{today}.csv')
#create a new dataframe for data from Arlington County

Dane_data = county_data[county_data['county'] == 'Dane County']
#cut down dataframes to include just data needed for visualization
WI_metrics = WI_data[['date','metrics.caseDensity']]
Dane_metrics = Dane_data[['date','metrics.caseDensity']]

#rename columns to specify whether they are VA or Arlington's metrics
WI_metrics.rename(columns = {'metrics.caseDensity':'WI Case Density'}, inplace=True)
Dane_metrics.rename(columns = {'metrics.caseDensity':'Dane Case Density'}, inplace=True)
#existing index for dataframes is from initial data pull; reset to date
Dane_metrics = Dane_metrics.set_index('date')
WI_metrics = WI_metrics.set_index('date')

df1 = [WI_metrics['WI Case Density'], Dane_metrics['Dane Case Density']]
headers = ['WI Case Density', 'Dane Case Density']
caseDensity = pd.concat(df1, axis=1, keys=headers)
