import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '/Users/apple/Downloads/all-project-files/chicago.csv',
              'new york city': '/Users/apple/Downloads/all-project-files/new_york_city.csv',
              'washington': '/Users/apple/Downloads/all-project-files/washington.csv' }

MONTH_DATA = {'january': 1, 'febuary': 2, 'march': 3, 'april ': 4, 'may': 5, 'june': 6, 'all': 7}

DAY_DATA = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7, 'all': 8}  

# this is example

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city do you want to research? ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Your city is unavailable. Please try again!")

    # while True:
    #   city = input("--- ").lower()
    # if city not in CITY_DATA:
    # print("----")
    # continue
    # else: 
    # break      

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month do you want to find out? ").lower()
        if month in MONTH_DATA:
            break
        else:
            print("Your month is unavailable. Please try again!")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day do you want to find out? ").lower()
        if day in DAY_DATA:
            break
        else:
            print("Your day is unavailable. Please try again!")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print("The most common month is ", popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print("The most common day is ", popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print("The most common hour is ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print("The most common start station is ", popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print("The most common end station is ", popular_start_station)

    # display most frequent combination of start station and end station trip
    df['Combination Station'] = df['Start Station'] + " " + df['End Station']
    combination_station = df['Combination Station'].value_counts().idxmax()
    print("The most common combination station is ", combination_station)
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is ", total_travel_time/60, "mins")

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("The average travel time is ", average_travel_time/60 , "mins.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types: ", user_types)

    # Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print("Gender types: ", gender_types)
    except KeyError:
        print(" No data available for this month.")    

    # Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode())
        print("The earliest year of birth is: ", earliest, ".", "The most recent year of birth is: ", most_recent, ".", "The most common year of birth is: ", most_common )
    except KeyError:
        print("No data available for this month.")    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data (df):
    i = 0 
    print("\nDo you want to see the first 5 rows of data?")
    print("\nPlease type yes or no!")
    while (input()!= 'no'):
        i += 5
        print(df.iloc[i:i + 5])
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
