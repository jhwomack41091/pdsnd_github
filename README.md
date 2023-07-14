>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

# Bike Share data exploration using python
 This python project will provide basic statistics information from bike share data csv files from different cities.

## Date created 2023-07-10 18:11:00 PM
--------------------------------------

## Description
--------------
 Will provide data for either Chicago, New York City, or Washington DC based on user selection.
 Prompts the user with multiple options to select filter for the data files.
  ### Filter by: 
   * Month
   * Day
   * Both Month and Day
   * Additionally can select No time filter to show all data

 Will provide statistics for the following pieces of information from the user selected city. The user can select which set of statistics they want to view.
  * Time Statistics
    - Will display the month with the most bike rentals, if the user has not selected a month to filter by.
    - Will display the most common day of the week that users are renting bikes, if the user has not selected a day to filter by.
    -W hich hour of the day is the most common for users renting bikes.
  * Bike station rental and trip statistics
    - Find the most common station that users are renting from.
    - Find the most common station that users are returning/dropping bikes off at.
    - Find the most frequently traveled path, based on starting station and end station.
    - Find the least frequently traveled path, based on starting station and end station.
  * Trip duration statistics
    - Total travel time, based on any user provided month and/or day filters
    - Average travel time, based on any user provided month and/or day filters
    - What is the longest trip time, based on any user provided month and/or day filters
  * User statistics
    - Displays a count of each user type _Customer, Subscriber, Dependant_
    - Will display the earliest, most recent, and most common birth year among users.
    - If data is available, a count for the gender of users will be displayed _Male, Female_
  * Finally the user can select if they wish to view the raw data
    - The user will be shown 5 lines of data at a time, and can view as much or little data they wish to see. If any at all.

Once the user has finished viewing the statistics and/or raw data based on their selected city and time filters, they will be prompted to either restart to select different inputs or exit.
This python script does include basic error handling for incorrect or un recognized inputs.

### Files used
 This project was completed using:
 + Chicago.csv
 + New_York_City.csv
 + Washington.csv

### Credits
 + Utilizing a python key search [function](https://www.learnbyexample.org/python-nested-dictionary/).
     - 
     ```
     for id, info in months.items():
             for key in info:
                 if info[key] == pop_month_num:
                     pop_month_name = months[id]['full']
     ```
 + Gathered assistance to get the least common value from a csv column by putting the data into a python dataframe.
     - [pandas.pydata.org](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nsmallest.html)
     - [appsloveworld](https://www.appsloveworld.com/pandas/100/33/pandas-least-frequent-value-in-column)
 + Found a helpful solution to calculating a user friendly way to display times for statistics, data provided in seconds.
     - Breaks down data from seconds to days, hours, minutes and seconds rounded up to the nearest second.
         - [studytonight](https://www.studytonight.com/python-howtos/how-to-convert-seconds-to-hours-minutes-and-seconds-in-python)
 + To assist with writing and properly formatting ***README.md*** files
     - [docs.github.com](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#headings)