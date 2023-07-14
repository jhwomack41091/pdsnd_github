import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv', 'new york': 'new_york_city.csv', 'washington': 'washington.csv'}
months = {'jan': {'full': 'January', 'num':1}, 'feb': {'full': 'February', 'num': 2}, 'mar': {'full': 'March', 'num':3}, 'apr': {'full': 'April', 'num': 4}, 'may': {'full': 'May', 'num': 5}, 'jun': {'full': 'June', 'num': 6}}
days = {'sun':'Sunday', 'mon':'Monday', 'tue':'Tuesday', 'wed':'Wednesday','thr':'Thursday','fri':'Friday', 'sat':'Saturday'}

def get_filters():
    """This function is used to get the data file the user wishes to view, and filters for the month and/or day based on user input."""
    while True:
        try:
            city = input('\nEnter the name of the city you would like to analyze: (Chicago, New York, or Washington).\n').lower()
            if city in CITY_DATA:
                break
            else:
                print('\nCity not found, please select \'Chicago\', \'New York\', or \'Washington\'.\n')
        except KeyError:
            print('\nCity not found, please select \'Chicago\', \'New York\', or \'Washington\'.\n')

    while True:
        filt_type = input('Would you like to filter data by month, day, both, or not at all? Type \'none\' for no filter.\n').lower()
        try:
            if filt_type == 'month':
                while True:
                    try:
                        monthx = input('Which month would you like to filter by? Or type \'all\' for all months. (Jan, Feb, Mar, Apr, May, Jun)\n').lower()
                        if monthx in months:
                            month = monthx
                            day = 'none'
                            break
                        elif monthx == 'all':
                            month = 'none'
                            day = 'none'
                            break
                        else:
                            print('\nInvalid month, please choose from the list of valid months.\n')
                    except:
                           print('\nNot a valid input. Please try again.\n')
                break
            elif filt_type == 'day':
                while True:
                    try:
                        dayx = input('Which day? Or type \'all\' for all days. (Sun, Mon, Tue, Wed, Thr, Fri, Sat)\n').lower()
                        if dayx in days:
                            day = days.get(dayx)
                            month = 'none'
                            break
                        elif dayx =='all':
                            day='none'
                            month = 'none'
                            break
                        else:
                            print('\nNot a valid input. Please enter one of the valid days from the list.\n')
                    except:
                           print('\nNot a valid input. Please try again.\n')
                break
            elif filt_type == 'both':
                while True:
                    try:
                        monthx = input('Which month would you like to filter by? Or type \'all\' for all months. (Jan, Feb, Mar, Apr, May, Jun)\n').lower()
                        if monthx in months:
                            month = monthx
                            break
                        elif monthx == 'all':
                            month = 'none'
                            break
                        else:
                            print('\nInvalid month, please choose from the list of valid months.\n')
                    except:
                           print('\nNot a valid input. Please try again.\n')
                while True:
                    try:
                        dayx = input('Which day? Or type \'all\' for all days. (Sun, Mon, Tue, Wed, Thr, Fri, Sat)\n').lower()
                        if dayx in days:
                            day = days.get(dayx)
                            break
                        elif dayx =='all':
                            day='none'
                            break
                        else:
                            print('\nNot a valid input. Please enter a valid day from the above days.\n')
                    except:
                           print('\nNot a valid input. Please try again.\n')
                break
            elif filt_type == 'none':
                month = 'none'
                day = 'none'
                break
            else:
                print('\nInvalid input.\n')
        except:
            print('\nInvalid input.\n')

    print('\nHello! Let\'s explore some US bikeshare data for {}!'.format(city.title()))

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """This function loads the data into a data frame for calculations based on the filters the user selected."""
    #Loads data for the specified city and filters by month and day if applicable.
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #Filter by month if applicable
    if month != 'none':
        month_filter = months[month]['num']
        #New dataframe using the month_filter
        df = df[df['month'] == month_filter]
    if day != 'none':
        #New dataframe using the day filter
        df = df[df['day_of_week'] == day]
    return df

def time_stats(df, month, day):
    """This function calculates time statistics if the user has selected to view them from the main."""
    print('\nCalculating the most frequent times of travel...\n')
    start_time = time.time()
    if month == 'none':
        #Display the most common month
        pop_month_num = df['month'].mode()[0]
        # Function derived from (https://www.learnbyexample.org/python-nested-dictionary/)
        for id, info in months.items():
            for key in info:
                if info[key] == pop_month_num:
                    pop_month_name = months[id]['full']
        print('\nThe most common month for usage is: {}'.format(pop_month_name))
    
    if day == 'none':
        #Display the most common day of week
        pop_dayofweek = df['day_of_week'].mode()[0]
        print('\nThe most common day of the week for usage is: {}'.format(pop_dayofweek))

    #Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    pop_hr = df['hour'].mode()[0]
    if pop_hr > 12:
        pop_hr -= 10
        print('\nThe most common start hour for trips is: {} PM'.format(pop_hr))
    else:
        print('\nThe most common start hour for trips is: {} AM'.format(pop_hr))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """This function calculates station statistics if the user has selected to view them from the main."""
    #Displays statistics on the most popular stations and trips.
    print('\nCalculating the most popular stations and trip...\n')
    start_time = time.time()

    #Display the most commonly used start station
    com_start_sta = df['Start Station'].mode()[0]
    print('\nThe most commonly used starting station is: {}'.format(com_start_sta))

    #Display the most commonly used end station
    com_end_sta = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is: {}'.format(com_end_sta))

    #Display most frequent combination of start and end station
    freq_combo_sta = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(1)
    print('\nThe most frequently traveled trip is:\n{}'.format(freq_combo_sta))

    # Used for reference to find the least common value (https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nsmallest.html) & (https://www.appsloveworld.com/pandas/100/33/pandas-least-frequent-value-in-column)
    
    #Display the least commonly used start station
    lcom_start_sta = df['Start Station'].value_counts()
    print('\nThe least commonly used starting station is: {}'.format(lcom_start_sta.index[-1]))

    #Display the least commonly used end station
    lcom_end_sta = df['End Station'].value_counts()
    print('\nThe least commonly used end station is: {}'.format(lcom_end_sta.index[-1]))

    #Display least frequent combination of start and end station
    lfreq_combo_sta = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nsmallest(1)
    print('\nThe least frequently traveled trip is:\n{}'.format(lfreq_combo_sta))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """This function calculates trip duration statistics if the user has selected to view them from the main."""
     #Uses mathematics to calulate hrs, min, secs from total time in seconds (https://www.studytonight.com/python-howtos/how-to-convert-seconds-to-hours-minutes-and-seconds-in-python)

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time=df['Trip Duration'].sum()
    total_days = total_time // (24 * 3600)
    total_seconds = total_time % (24 * 3600)
    total_hr = total_seconds // 3600
    total_seconds %= 3600
    total_min = total_seconds // 60
    total_seconds //= 60
    if total_days > 0:
        print('\nThe total travel time logged is: {}days, {}hrs, {}mins, {}secs'.format(total_days, total_hr, total_min, total_seconds))
    else:
        print('\nThe total travel time logged is: {}hrs, {}mins, {}secs'.format(total_hr, total_min, total_seconds))

    # display mean travel time
    avg_time=df['Trip Duration'].mean()
    avg_days = avg_time // (24 * 3600)
    avg_seconds = avg_time % (24 * 3600)
    avg_hr = avg_seconds // 3600
    avg_seconds %= 3600
    avg_min = avg_seconds // 60
    avg_seconds //= 60
    if avg_days > 0:
        print('\nThe average trip time for all trips is: {}days, {}hrs, {}mins, {}secs'.format(avg_days, avg_hr, avg_min, avg_seconds))
    else:
        print('\nThe average trip time for all trips is: {}hrs, {}mins, {}secs'.format(avg_hr, avg_min, avg_seconds))

    #Display the longest trip
    max_time=df['Trip Duration'].max()
    max_seconds = max_time % (24 * 3600)
    max_hr = max_seconds // 3600
    max_seconds %= 3600
    max_min = max_seconds // 60
    max_seconds //= 60
    print('\nThe longest trip time for all trips is: {}hrs, {}mins, {}secs'.format(max_hr, max_min, max_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """This function calculates user statistics if the user has selected to view them from the main."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count=df['User Type'].value_counts()
    print('\nThe count of user types is:\n{}'.format(user_count))

    # Display counts of gender, if not Washington
    if city != 'washington':
        gender_count=df['Gender'].value_counts()
        print('\nThe count of users by gender is:\n{}'.format(gender_count))
        
        # Display earliest, most recent, and most common year of birth
        birth_year=df['Birth Year']
        birth_year_min=birth_year.min()
        birth_year_recent=birth_year.max()
        birth_year_common=birth_year.mode()[0]
        print('\nThe earliest birthyear in this data set is: {}'.format(birth_year_min))
        print('\nThe most recent birth year is: {}'.format(birth_year_recent))
        print('\nThe most common year of birth is: {}'.format(birth_year_common))
    else:
        print('\nNo information on User Gender or Year of birth exists for this city!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_raw_data(df, i, x):
    """This function determines if the current row of raw data is greater than the max number of rows. Will display five rows of raw data to the user if the user has selected to view them from the main."""
    if i >= x:
        i == x
        
    print(df.head(i))

def main():
    """This function is the main function to get a user selected city and prompt the user for filters for the data and display stats if the user desires."""
    while True:
        city, month, day = get_filters()
  
        df = load_data(city, month, day)

        #Will show the time statistics for the given data if user inputs yes
        while True:
            show_time_stats = input('\nWould you like to show the time statistics? Enter yes or no.\n')
            if show_time_stats.lower() =='yes':
                time_stats(df, month, day)
                break
            elif show_time_stats.lower() =='no':
                break
            else:
                print('\nInvalid input. Please enter yes or no.\n')

        #Will show the station statistics for the given data if user inputs yes
        while True:
            show_station_stats = input('\nWould you like to show the station statistics? Enter yes or no.\n')
            if show_station_stats.lower() =='yes':
                station_stats(df)
                break
            elif show_station_stats.lower() =='no':
                break
            else:
                print('\nInvalid input. Please enter yes or no.\n')

        #Will show the trip duration statistics for the given data if user inputs yes
        while True:
            show_dur_stats = input('\nWould you like to show the trip duration statistics? Enter yes or no.\n')
            if show_dur_stats.lower() =='yes':
                trip_duration_stats(df)
                break
            elif show_dur_stats.lower() =='no':
                break
            else:
                print('\nInvalid input. Please enter yes or no.\n')

        #Will show the user statistics for the given data if user inputs yes
        while True:
            show_user_stats = input('\nWould you like to show the user statistics? Enter yes or no.\n')
            if show_user_stats.lower() =='yes':
                user_stats(df, city)
                break
            if show_user_stats.lower() =='no':
                break
        else:
            print('\nInvalid input. Please enter yes or no.\n')

        #Will show the raw data for the given data if user inputs yes
        show_raw_data = input('\nWould you like to show the raw data for this set? Enter yes or no.\n')
        if show_raw_data.lower() !='no':
            #use i as a counter variable for the number of rows to display
            i=5
            #use x as the number of rows in the dataset
            x = int(df.shape[0])
            get_raw_data(df, i, x)
            while True:
                i += 5
                show_add = input('\nWould you like to see additional data? Enter yes or no.\n')
                if show_add.lower() != 'no' :
                    get_raw_data(df, i, x)
                    if i >= x:
                        print('This is the all the raw data to display')
                        break
                else:
                    break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()