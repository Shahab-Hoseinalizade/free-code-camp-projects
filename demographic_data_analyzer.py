## Import Packages

import numpy as np
import pandas as pd

## Read data from file

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Free Code Camp - P2/adult.data.csv')
df.info()

## How many people of each race are represented in this dataset?

df['native-country'].value_counts()

## What is the average age of men?

df['sex'].value_counts()

mask = df['sex'] == ' Male'
all_males = df[mask]

average_age_of_men = round(all_males['age'].mean(), 1)
print(f'Average Age of Males : {average_age_of_men}')

## What is the percentage of people who have a Bachelor's degree?

df['education'].value_counts()

mask = df['education'] == ' Bachelors'
all_bachelors = df[mask]

per_of_all_bachelors = round((all_bachelors.shape[0] / df.shape[0]) * 100, 1)
print(f'Percentage of those who have a bachelors degree : {per_of_all_bachelors} %')

## What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?

higher_edu = df.loc[df['education'].isin([' Bachelors', ' Masters', ' Doctorate'])]
higher_edu_rich = higher_edu.loc[higher_edu['income'].isin([' >50K'])]

per_rich_higher_edu = round((higher_edu_rich.shape[0] / higher_edu.shape[0]) * 100, 1)
print(f'Percentage of people with advanced education make more than 50K : {per_rich_higher_edu} %')

## What percentage of people without advanced education make more than 50K?

lower_edu = df.loc[~df['education'].isin([' Bachelors', ' Masters', ' Doctorate'])]
lower_edu_rich = lower_edu.loc[lower_edu['income'].isin([' >50K'])]

per_rich_lower_edu = round((lower_edu_rich.shape[0] / lower_edu.shape[0]) * 100, 1)
print(f'Percentage of people without advanced education make more than 50K : {per_rich_lower_edu} %')

## What is the minimum number of hours a person works per week?

min_work_hours = df['hours-per-week'].min()
print(f'Minimum Work Hours Per Week: {min_work_hours} Hour(s)')

## What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?

num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]
num_min_workers_rich = num_min_workers.loc[num_min_workers['income'] == ' >50K']

rich_group_percentage = round((num_min_workers_rich.shape[0] / num_min_workers.shape[0]) * 100, 1)

print(f'Percentage of Really Rich Group: {rich_group_percentage} %')

## What country has the highest percentage of people that earn >50K and what is that percentage?

highest_income = df.loc[df['income'] == ' >50K']
highest_income_by_country_list = highest_income['native-country'].value_counts()

highest_income_country = highest_income_by_country_list.index[0]
highest_income_country_percentage = round((highest_income_by_country_list[0] / highest_income.shape[0]) * 100, 1)

print(f'Highest Income By native-Country: {highest_income_country}')
print(f'Percentage of Highest Income Country : {highest_income_country_percentage} % ')

## Identify the most popular occupation for those who earn >50K in India

indian = df.loc[df['native-country'].isin([' India'])]
indian_rich = indian.loc[indian['income'].isin([' >50K'])]

indian_rich_occu_list = indian_rich['occupation'].value_counts()
indian_rich_popular_occupation = indian_rich_occu_list.index[0]

print(f'The Most Popular occupation For Indian Richs: {indian_rich_popular_occupation}')
