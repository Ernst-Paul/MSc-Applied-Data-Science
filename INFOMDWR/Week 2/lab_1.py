import pandas as pd

world = pd.read_csv(filepath_or_buffer = '/Users/e.p.swens/Desktop/python/Data/world.csv', delimiter=',',
     doublequote=True, quotechar='"',na_values = ['na', '‐', '.', ''], encoding = "ISO‐8859‐1")
game = pd.read_csv(filepath_or_buffer = '/Users/e.p.swens/Desktop/python/Data/game.csv', delimiter=',',
     doublequote=True, quotechar='"',na_values = ['na', '‐', '.', ''], encoding = "ISO‐8859‐1")
goal = pd.read_csv(filepath_or_buffer = '/Users/e.p.swens/Desktop/python/Data/goal.csv', delimiter=',',
     doublequote=True, quotechar='"',na_values = ['na', '‐', '.', ''], encoding = "ISO‐8859‐1")
movies = pd.read_csv(filepath_or_buffer = '/Users/e.p.swens/Desktop/python/Data/movies.csv', delimiter=',',
     doublequote=True, quotechar='"',na_values = ['na', '‐', '.', ''], encoding = "ISO‐8859‐1")
nobel = pd.read_csv(filepath_or_buffer = '/Users/e.p.swens/Desktop/python/Data/nobel.csv', delimiter=',',
     doublequote=True, quotechar='"',na_values = ['na', '‐', '.', ''], encoding = "ISO‐8859‐1")

# Question 1.
# If you know that in the world table, the continent of the countries Armenia,
# Azerbaijan, Russia, Georgia and Turkey is not Europe. Write a query that
# returns the total area of the European countries after adding the area of
# these countries.
ans_1 = sum(world['area'][(world['continent'] == 'Europe') | (world['name'].isin(["Armenia",
"Azerbaijan", "Russia", "Georgia", "Turkey"]))])
print(ans_1)

# Question 2.
# Write a query that returns the names of the players in the German team who
# scored at least one goal with the name of the stadium where they scored the
# goals.
game_goal = pd.merge(game, goal, left_on='id', right_on='matchid')
ans_2 = game_goal[['player','stadium']][game_goal['teamid'] == 'GER']
#print(ans_2)

# Question 3.
# Write a query which would show the players and their teams for those who
# have scored against France (FRA) in Donbass Arena.
game_goal = pd.merge(game, goal, left_on='id', right_on='matchid')
ans3 = game_goal[['player', 'teamid', 'stadium']][((game_goal['team1'] == 'FRA') |
            (game_goal['team2'] == 'FRA')) & (game_goal['teamid'] != 'FRA')
            & (game_goal['stadium'] == 'Donbass Arena')]
#print(ans_3)

# Question 4.
# Write a query that displays the name and the the average population of the
# continent in the world table.
world_proj = world[['continent', 'population']][:]
ans_4 = world_proj.groupby(['continent']).mean()
#print(ans_4)

# Question 5.
# Write a query to return the number of missing values in each column of the
# world table [only in Python for now]. Use the world table.
ans_5 = pd.isna(world).sum()
#print(ans_5)

# Question 6.
# Write a query that lists the countries with no missing values in their gdp.
# Use the world table. 1
ans_6 = world.dropna(subset=['gdp'])
#print(ans_6[['name','gdp']])

# Question 7.
# Write a query that lists the countries with no missing values in any of their
# attributes [only in Python for now]. Use the world table.
ans_7 = world.dropna()
#print(ans_7[['name','gdp']])

# Question 8.
# Write a query to calculate the average budget for movies produced in USA
# since 2010 (incl. 2010). Use the movies table.
movies_2010 = movies[['movie_title','title_year','budget']][(movies['title_year'] >= 2010)]
ans_8 = movies_2010['budget'].mean()
#print(round(ans_8))

# Question 9.
# Write a query to count the number of unique directors by names. Use the
# movies table.
ans_9 = len(pd.unique(movies['director_name']))
#print(ans_9)

# Question 10.
# Write a query that returns the years in which no Nobel price is given for
# physics. Use the nobel table.
all_yr = pd.DataFrame(data = {'yr': range(1901,2017)})
nobel_yr = pd.merge(all_yr,nobel[:][nobel['subject'] == 'Physics'],
         how='left', on='yr')
ans_10 = nobel_yr[nobel_yr.isna().any(axis=1)]
#print(ans_10)

# Question 11.
# Write a query to count the number of Nobel price winners from Netherlands.
# Use nobel table.
# Not possible at least not with the given noble.csv

# Question 12.
# Write a query to find the number of Nobel price winners of each country.
# Use nobel table.
# Not possible at least not with the given noble.csv
