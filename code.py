# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

data = pd.read_csv(path,sep=',')

data.rename(columns={'Total':'Total_Medals'},inplace=True)

data.head(10)
#Code starts here



# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer',np.where(data['Total_Summer'] == data['Total_Winter'],'Both','Winter'))


better_event = data['Better_Event'].value_counts(ascending=False).index[0]

print(better_event)


# --------------
#Code starts here
top_countries= data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries.drop(index=data.index[-1],axis=0,inplace=True)

def top_ten(column):
    country_list = []
    t = top_countries.nlargest(10,column)

    country_list = (t['Country_Name']).tolist()
    return country_list

top_10_summer = top_ten('Total_Summer')
top_10_winter = top_ten('Total_Winter')
top_10 = top_ten('Total_Medals')

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print(common)



# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]

winter_df = data[data['Country_Name'].isin(top_10_winter)]

top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind='bar',x='Country_Name',y='Total_Summer')
plt.xlabel('Top 10 Countries')
plt.ylabel('Summer Olympic Medal Counts')

winter_df.plot(kind='bar',x='Country_Name',y='Total_Winter')
plt.xlabel('Top 10 Countries')
plt.ylabel('Winter Olympic Medal Counts')

top_df.plot(kind='bar',x='Country_Name',y='Total_Medals')
plt.xlabel('Top 10 Countries')
plt.ylabel('Total Olympic Medal Counts')
plt.show()


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']

summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

print(summer_country_gold)
##################
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/summer_df['Total_Winter']

winter_max_ratio = winter_df['Golden_Ratio'].max()

winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

print(winter_country_gold)
###################

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']

top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

print(top_country_gold)
###################



# --------------
#Code starts here

data_1 = data.drop(data.index[-1])


data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + data_1['Bronze_Total']

most_points = data_1['Total_Points'].max()

best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']

print(best_country)


# --------------
#Code starts here

best = data[data['Country_Name'] == best_country][['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)

plt.xlabel('United States')
plt.ylabel('Medals Tally')

plt.xticks(rotation=45)

plt.show()


