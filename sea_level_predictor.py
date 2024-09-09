import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def sea_level_prediction(csv_file):
    """
    Plots a scatter plot and two lines of best fit to predict sea level rise.

    Args:
        csv_file (str): The path to the CSV file containing the sea level data.

    Returns:
        matplotlib.figure.Figure: The created figure.
    """

    # Load the data
    df = pd.read_csv(csv_file)

    # Create a scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data points')

    # Calculate the line of best fit for the entire dataset
    slope_all, intercept_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])[:2]
    x_all = df['Year'].min() - 10, 2050
    y_all = slope_all * x_all + intercept_all
    plt.plot(x_all, y_all, color='red', label='Trend since 1880')

    # Calculate the line of best fit for the data after 2000
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])[:2]
    x_recent = df_recent['Year'].min() - 10, 2050
    y_recent = slope_recent * x_recent + intercept_recent
    plt.plot(x_recent, y_recent, color='green', label='Trend since 2000')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add a legend
    plt.legend()

    # Save and return the plot
    plt.savefig('sea_level_plot.png')
    return plt.gcf()


