# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# Generate a line chart that visualizes the readings in the months

def line_chart(df,period,col):
    """ A line chart that visualizes the readings in the months
    
    This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature based on the periods. Ensure the period labels are properly named.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    period - Period of time over which you want to aggregate the data
    col - Feature of the dataframe
    
    """
    if period == 'day':
        day_series = pd.to_datetime(df['Date/Time']).dt.day
        df['Day'] = day_series
        daily_mean_col = df.groupby('Day')[col].mean()
        daily_mean_col.plot(kind = 'line')

    elif period == 'month':
        month_series = pd.to_datetime(df['Date/Time']).dt.month
        df['Month'] = month_series
        monthly_mean_col = df.groupby('Month')[col].mean()
        monthly_mean_col.plot(kind = 'line')
        plt.xticks(np.arange(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation = 90)

    
# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
    """ Univariate analysis of categorical columns
    
    This function accepts the dataframe df which analyzes all the variable in the data and performs the univariate analysis using bar plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    """
    df['Weather'].value_counts().plot(kind = 'bar')
    
    
# Function to plot continous plots
def plot_cont(df,plt_type):
    """ Univariate analysis of Numerical columns
    
    This function accepts the dataframe df, plt_type(boxplot/distplot) which analyzes all the variable in the data and performs the univariate analysis using boxplot or distplot plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    plt_type - type of plot through which you want to visualize the data
    """ 
    fig, ((ax_1, ax_2), (ax_3, ax_4), (ax_5, ax_6)) = plt.subplots(3, 2)
    if plt_type == 'distplot':
        sns.distplot(df['Temp (C)'], ax = ax_1)
        sns.distplot(df['Dew Point Temp (C)'], ax = ax_2)
        sns.distplot(df['Rel Hum (%)'], ax = ax_3)
        sns.distplot(df['Wind Spd (km/h)'], ax = ax_4)
        sns.distplot(df['Visibility (km)'], ax = ax_5)
        sns.distplot(df['Stn Press (kPa)'], ax = ax_6)
    elif plt_type == 'boxplot':
        sns.boxplot(df['Temp (C)'], ax = ax_1)
        sns.boxplot(df['Dew Point Temp (C)'], ax = ax_2)
        sns.boxplot(df['Rel Hum (%)'], ax = ax_3)
        sns.boxplot(df['Wind Spd (km/h)'], ax = ax_4)
        sns.boxplot(df['Visibility (km)'], ax = ax_5)
        sns.boxplot(df['Stn Press (kPa)'], ax = ax_6)

# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
   
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    col2 - Feature of the dataframe to be plot against grouped data.
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    new_df = df.groupby(col1)[col2].agg(agg1)
    new_df.plot(kind = 'bar', x = col1, y = col2)

# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'
weather_df = pd.read_csv(path, parse_dates = True, index_col = 'Date/Time')

# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.
#line_chart(weather_df, 'month', 'Temp (C)')

# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.
plot_categorical_columns(weather_df)

# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot
plot_cont(weather_df, "distplot")


# Call the function "plot_cont()" with the appropriate parameters to plot boxplot
plot_cont(weather_df, "boxplot")

# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
# Feel free to try on diffrent features and aggregated functions like max, min.
group_values(weather_df, 'Weather', 'mean', 'Visibility (km)')




