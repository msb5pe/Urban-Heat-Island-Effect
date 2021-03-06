# -*- coding: utf-8 -*-
"""UrbanHeatIsland.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CnocEwqt6rY2x4ScZC486XVBDo6YfGIT
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import matplotlib.pyplot as plt

"""# Data Cleaning"""

df = pd.read_csv('heat_island.csv', encoding = "ISO-8859-1")
df = df.drop('NewCityID', axis=1)
df = df.drop('UrbanID', axis=1)
original_df = df;
df.info()

cols = ['CityTempDay', 'CityBufferDiffDay', 'CityTempNight', 'BufferTempNight', 'CityBufferDiffNight'] 
df[cols] = df[cols].fillna(df.mean().iloc[0])
df.info()

df['CityBufferAvg'] = (df['CityBufferDiffDay'] + df['CityBufferDiffNight'])/2

df_day = df.drop(columns=['Name', 'NameFixed', 'BufferTempDay', 'BufferTempNight', 'CityBufferDiffNight', 'CityBufferAvg'])
corr_matrix = df_day.corr()
corr_matrix['CityBufferDiffDay'].sort_values(ascending=False)

df_night = df.drop(columns=['Name', 'NameFixed', 'BufferTempDay', 'BufferTempNight', 'CityBufferDiffDay', 'CityBufferAvg'])
corr_matrix = df_night.corr()
corr_matrix['CityBufferDiffNight'].sort_values(ascending=False)

df.max().to_frame().T

df.min().to_frame().T

df['CityBufferDiffDay'].nsmallest(10)

smalldayoutliers = df.loc[(df['CityBufferDiffDay'] <= -16.87)]
data = df.loc[(df['CityBufferDiffDay'] > -16.87)]
df['CityBufferDiffDay'].nlargest(10)

largedayoutliers = df.loc[(df['CityBufferDiffDay'] >= 10.99)]
data = data.loc[(data['CityBufferDiffDay'] < 10.99)]
df['CityBufferDiffNight'].nsmallest(10)

smallnightoutliers = df.loc[(df['CityBufferDiffNight'] <= -12.19)]
data = data.loc[(data['CityBufferDiffNight'] > -12.19)]
df['CityBufferDiffNight'].nlargest(10)

largenightoutliers = df.loc[(df['CityBufferDiffNight'] >= 9.54)]
data = data.loc[(data['CityBufferDiffNight'] < 9.54)]
largedayoutliers = largedayoutliers[['Country', 'Name', 'CityBufferDiffDay']]
largedayoutliers.sort_values('CityBufferDiffDay', ascending=False).head(10)

smalldayoutliers = smalldayoutliers[['Country', 'Name', 'CityBufferDiffDay']]
smalldayoutliers.sort_values('CityBufferDiffDay', ascending=True).head(10)

largenightoutliers = largenightoutliers[['Country', 'Name', 'CityBufferDiffNight']]
largenightoutliers.sort_values('CityBufferDiffNight', ascending=False).head(10)

smallnightoutliers = smallnightoutliers[['Country', 'Name', 'CityBufferDiffNight']]
smallnightoutliers.sort_values('CityBufferDiffNight', ascending=True).head(10)

averageoutliers = df[['Country', 'Name', 'CityBufferAvg']]
averageoutliers.sort_values('CityBufferAvg', ascending=False).head(10)

averageoutliers.sort_values('CityBufferAvg', ascending=True).head(10)

"""# Data Visualization"""

# Map of entire world, excluding major outliers in order to show more color differentiation
maxdiff = 10.99
mindiff = -16.87
plt.scatter(x=data["Longitude"], y=data["Latitude"], c=data["CityBufferDiffDay"], cmap = 'jet', alpha=0.2)
cbar = plt.colorbar()
plt.clim(mindiff, maxdiff)
plt.title('City Buffer Difference Day, World', size=12, weight='bold')
plt.xlabel('Latitude', size=10, weight='bold')
plt.ylabel('Longitude', size=10, weight='bold')
plt.show()

# Same color scale is kept in both day and night world overviews
plt.scatter(x=data["Longitude"], y=data["Latitude"], c=data["CityBufferDiffNight"], cmap = 'jet', alpha=0.2)
cbar = plt.colorbar()
plt.clim(mindiff, maxdiff)
plt.title('City Buffer Difference Night, World', size=12, weight='bold')
plt.xlabel('Latitude', size=10, weight='bold')
plt.ylabel('Longitude', size=10, weight='bold')
plt.show()

USA = data.loc[df['Country'] == 'USA']
USA['CityBufferDiffDay'].nlargest(5)

USA['CityBufferDiffDay'].nsmallest(5)

USA['CityBufferDiffNight'].nlargest(5)

USA['CityBufferDiffNight'].nsmallest(5)

mindiff = -9.43
maxdiff = 9.13

plt.scatter(x=USA["Longitude"], y=USA["Latitude"], c=USA["CityBufferDiffDay"], cmap = 'jet', alpha=0.2)
cbar = plt.colorbar()
plt.clim(mindiff, maxdiff)
plt.title('City Buffer Difference Day, USA', size=12, weight='bold')
plt.xlabel('Latitude', size=10, weight='bold')
plt.ylabel('Longitude', size=10, weight='bold')
plt.show()

USA_small = USA.loc[(USA['Latitude'] >= 21) & (USA['Latitude'] <= 50)]
USA_small = USA_small.loc[(USA_small['Longitude'] >= -130)]

# United States City - Buffer during the day
plt.scatter(x=USA_small["Longitude"], y=USA_small["Latitude"], c=USA_small["CityBufferDiffDay"], cmap = 'jet', alpha=0.2)
cbar = plt.colorbar()
plt.clim(mindiff, maxdiff)
plt.title('City Buffer Difference Day, USA', size=12, weight='bold')
plt.xlabel('Latitude', size=10, weight='bold')
plt.ylabel('Longitude', size=10, weight='bold')
plt.show()

# United States City - Buffer average during the night
plt.scatter(x=USA_small["Longitude"], y=USA_small["Latitude"], c=USA_small["CityBufferDiffNight"], cmap = 'jet', alpha=0.2)
cbar = plt.colorbar()
plt.clim(mindiff, maxdiff)
plt.title('City Buffer Difference Night, USA', size=12, weight='bold')
plt.xlabel('Latitude', size=10, weight='bold')
plt.ylabel('Longitude', size=10, weight='bold')
plt.show()

# United States city - buffer averaged between day and night

plt.scatter(x=USA_small["Longitude"], y=USA_small["Latitude"], c=USA_small["CityBufferAvg"], cmap = 'jet', alpha=0.2)
cbar = plt.colorbar()
plt.clim(mindiff, maxdiff)
plt.title('City Buffer Difference Average, USA', size=12, weight='bold')
plt.xlabel('Latitude', size=10, weight='bold')
plt.ylabel('Longitude', size=10, weight='bold')
plt.show()

# Changed color bar to see more difference
plt.scatter(x=USA_small["Longitude"], y=USA_small["Latitude"], c=USA_small["CityBufferAvg"], cmap = 'jet', alpha=0.2)
cbar = plt.colorbar()
# plt.clim(mindiff, maxdiff)
plt.title('City Buffer Difference Average, USA', size=12, weight='bold')
plt.xlabel('Latitude', size=10, weight='bold')
plt.ylabel('Longitude', size=10, weight='bold')
plt.show()

averages = USA.sort_values('CityBufferDiffDay', ascending=True)
averages = averages[['Country', 'Name', 'CityBufferDiffDay']]
averages.head()

averages = USA.sort_values('CityBufferDiffNight', ascending=True)
averages = averages[['Country', 'Name', 'CityBufferDiffNight']]
averages.head()

# Outliers, high is greater than 2.5 degrees C city/buffer difference
USA_high = USA_small.loc[(USA_small['CityBufferDiffNight'] >= 2.5)]
USA_low = USA_small.loc[(USA_small['CityBufferDiffNight'] < 2.5)]
USA_high = USA_high.sort_values('CityBufferDiffNight', ascending=False)
USA_high.head()

USA_high.shape

df['Country'].value_counts().nlargest(10)

large_cities = df.loc[(df['Pop2000'] >= 50000)]
country_groups_day = large_cities.groupby('Country').mean().sort_values('CityBufferDiffDay', ascending=False)
country_groups_day.head(10)

country_groups_night = large_cities.groupby('Country').mean().sort_values('CityBufferDiffNight', ascending=False)
country_groups_night.head(10)

"""# Predicting a city's city-buffer average difference based on population, city size, city location, and city temperatures during the day and night

Day first
"""

df_day = pd.get_dummies(df_day, columns=['Country'])
df_day.head()

# from sklearn.model_selection import train_test_split
# 
# train, test = train_test_split(df_day, test_size=0.2)
# train_X = train.drop('CityBufferDiffDay', axis=1)
# train_y = train['CityBufferDiffDay']
# test_X = test.drop('CityBufferDiffDay', axis=1)
# test_y = test['CityBufferDiffDay']

X_day = df_day.drop('CityBufferDiffDay', axis=1)
y_day = df_day['CityBufferDiffDay']

from sklearn.ensemble import RandomForestRegressor

forest_reg = RandomForestRegressor(random_state=42)
forest_reg.fit(X_day, y_day)

X_sample = X_day.iloc[:5]
y_sample = y_day.iloc[:5]
print("Predictions: ", forest_reg.predict(X_sample))

print("Actual: ", list(y_sample))

from sklearn.model_selection import cross_val_score
import numpy as np

forest_scores = cross_val_score(forest_reg, X_day, y_day,
                               scoring="neg_mean_squared_error", cv=10)
forest_rmse_scores = np.sqrt(-forest_scores)

def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())

display_scores(forest_rmse_scores)

"""Off by 1.7 degrees C, not terrible, but could be better"""

from sklearn.model_selection import GridSearchCV

param_grid = [
#     Try 12 (3x4) combinations of hyperparameters
    {'n_estimators': [3, 10, 10], 'max_features': [2,4,6,8]},
#     Then try 6 (2x3) combinations with bootstrap set as false
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2,3,4]},
]

forest_reg = RandomForestRegressor(random_state=42)
grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                          scoring='neg_mean_squared_error', return_train_score=True)
grid_search.fit(X_day, y_day)

cvres = grid_search.cv_results_
for mean_score, params in zip(cvres['mean_test_score'], cvres['params']):
  print(np.sqrt(-mean_score), params)

grid_search.best_params_

forest_best = grid_search.best_estimator_
forest_best.fit(X_day, y_day)

forest_best = RandomForestRegressor(bootstrap=False, criterion='mse', max_depth=None,
           max_features=3, min_impurity_decrease=0.0, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           n_estimators=10, oob_score=False, random_state=42,
           verbose=0, warm_start=False)

forest_best.fit(X_day, y_day)

forest_scores2 = cross_val_score(forest_best, X_day, y_day,
                               scoring="neg_mean_squared_error", cv=10)
forest_rmse_scores2 = np.sqrt(-forest_scores2)

display_scores(forest_rmse_scores2)

"""# Best forest didnt work, need to fix

Back to the original random forest regressor!
"""

