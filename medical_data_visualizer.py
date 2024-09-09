import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('medical_examination.csv')
def clean_data(df):
    """
    Clean the data by removing entries with incorrect values.

    Args:
        df (pd.DataFrame): The medical examination data.

    Returns:
        pd.DataFrame: The cleaned data.
    """

    # Filter out entries with diastolic pressure higher than systolic pressure
    df = df[df['ap_lo'] <= df['ap_hi']]

    # Filter out entries with extreme height values
    df = df[df['height'] >= df['height'].quantile(0.025)]
    df = df[df['height'] <= df['height'].quantile(0.975)]

    # Filter out entries with extreme weight values
    df = df[df['weight'] >= df['weight'].quantile(0.025)]
    df = df[df['weight'] <= df['weight'].quantile(0.975)]

    return df


def calculate_overweight(df):
    """
    Calculate a new column 'overweight' based on Body Mass Index (BMI).

    Args:
        df (pd.DataFrame): The medical examination data.

    Returns:
        pd.DataFrame: The data with the new 'overweight' column.
    """

    df['bmi'] = df['weight'] / (df['height'] * df['height'])
    df['overweight'] = (df['bmi'] > 25).astype(int)

    return df


def normalize_data(df):
    """
    Normalize cholesterol and gluc values (0 for good, 1 for bad).

    Args:
        df (pd.DataFrame): The medical examination data.

    Returns:
        pd.DataFrame: The data with normalized cholesterol and gluc values.
    """

    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    return df


def draw_cat_plot(df):
    """
    Draw a categorical plot showing value counts for different features.

    Args:
        df (pd.DataFrame): The medical examination data.

    Returns:
        None
    """

    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
        var_name='variable',
        value_name='value'
    )

    df_cat = df_cat.groupby(['cardio', 'variable'])['value'].count().unstack()
    df_cat.fillna(0, inplace=True)

    fig = sns.catplot(
        x='variable',
        y='value',
        hue='cardio',
        kind='bar',
        data=df_cat
    )
    fig.set_title('Distribution of Features by Cardio Value')
    plt.show()


def draw_heat_map(df):
    """
    Draw a heatmap showing the correlation matrix of the data.

    Args:
        df (pd.DataFrame): The medical examination data.

    Returns:
        None
    """

    df_heat = clean_data(df.copy())
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    plt.figure(figsize=(10, 10))
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix of Medical Examination Data')
    plt.show()

