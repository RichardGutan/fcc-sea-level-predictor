import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', delimiter=',')
    df2 = df[df['Year'] >= 2000]
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, y)
   
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    sr1 = pd.Series([int(i) for i in range(1880, 2050)])
    plt.plot(sr1, intercept + slope*sr1, 'r')

    # Create second line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x2, y2)
    sr2 = pd.Series([int(i) for i in range(2000, 2050)])
    plt.plot(sr2, intercept + slope*sr2, 'r')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()