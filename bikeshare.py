import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('Would you like to see data for Chicago, New York, or Washington : ')
    city = city.lower()
    while city not in CITY_DATA:
        city = input('Not Valid City Try again \nWould you like to see data for Chicago, New York, or Washington : ')
        city = city.lower()
        
    # get user input for month (all, january, february, ... , june)
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = input('Select The month from january to june or all : ')
    month = month.lower()
    while not( month in months or month == 'all' ):
         month = input('Not Valid month Try again \nSelect The month from january to june or all : ')
         month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day = input("Select The day or all : ")
    day = day.lower()
    while not (day in days or day == 'all'):
        day = input("Not Valid day Try again \nSelect The day or all : ")
        day = day.lower()

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
    df = pd.read_csv(CITY_DATA[city])

   
    df['Start Time'] = pd.to_datetime(df['Start Time'])

  
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])       
    # display the most common month
    
    the_most_month = df['month'].mode()[0]
    print('the most common month is : ', the_most_month)
    # display the most common day of week
    
    the_most_day = df['day_of_week'].mode()[0]
    print('the most common day : ', the_most_day)
    
    # display the most common start hour
    
    
    the_most_hour = df['hour'].mode()[0]
    print('the most common hour : ', the_most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('The most common Start Station : ',most_start_station)
    # display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('The most common End Station : ',most_end_station)

    # display most frequent combination of start station and end station trip
    most_frequent_trip = (df['Start Station'] + "--" + df['End Station'])
    print('The most common frequent trip : ',most_frequent_trip) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ('the total travel time : ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print ('the mean travel time : ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of user types : ',df['User Type'].value_counts())

    # Display counts of gender
    print('Count of gender : ',df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        the_earliest_birth = int(df['Birth Year'].min())
        print('The earliest birth is : ',the_earliest_birth )
        the_recent_birth = int(df['Birth Year'].max())
        print('The recent birth is : ',the_recent_birth )
        the_most_birth = int(df['Birth Year'].mode()[0])
        print('The most common birth is : ',the_most_birth )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data (df):
    i = 0
    choice = input("If you need to display the first 5 rows? Yes or No").lower()
    pd.set_option('display.max_columns', None)
    while True:
        if choice == 'no':
            break
        print(df[i:i + 5])
        choice = input("If you need to display the second 5 rows? Yes or No").lower()
        i += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
