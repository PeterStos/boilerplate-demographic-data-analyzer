import pandas as pd

#test commit

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    race_count = race_count.squeeze()

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = percentage_bachelors = round((df['education'].value_counts(normalize=True).Bachelors * 100), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?  
    higher_education = df.loc[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | 
                             (df['education'] == 'Doctorate'))].shape[0]
    higher_rich = df.loc[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | 
                             (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')].shape[0] 
    
    # What percentage of people without advanced education make more than 50K?
    lower_education = df.loc[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | 
                             (df['education'] == 'Doctorate'))].shape[0]

    lower_rich = df.loc[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | 
                             (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')].shape[0]

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | 
                             (df['education'] == 'Doctorate'))].shape[0]
    lower_education = df.loc[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | 
                             (df['education'] == 'Doctorate'))].shape[0]

    # percentage with salary >50K
    higher_education_rich = higher_education_rich = round((higher_rich / higher_education * 100), 1)
    lower_education_rich = round((lower_rich / lower_education * 100), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours].shape[0]
    rich_percentage = round((df.loc[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0] / num_min_workers * 100), 1)

    # What country has the highest percentage of people that earn >50K?
    dataset_richest_by_country = ((df[df['salary']=='>50K']).groupby('native-country').count()['age'])
    total_by_country = df['native-country'].value_counts().sort_index()
    highest_earning_country = (dataset_richest_by_country / total_by_country).idxmax()

    highest_earning_country_percentage = round(((dataset_richest_by_country / total_by_country).max() * 100), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_top_IN_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = df_top_IN_occupation.groupby('occupation').count().idxmax()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
