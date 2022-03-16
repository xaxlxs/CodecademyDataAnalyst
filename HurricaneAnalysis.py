# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# write your update damages function here:
def update_damages(damages):
    updated_damages = []
    for i in damages:
        if i == "Damages not recorded":
            updated_damages.append(i)
        else:
            damage = float(i[:-1])
            if i[-1] == 'M':
              updated_damages.append(damage*1000000)
            if i[-1] == 'B':
              updated_damages.append(damage*1000000000)
    return updated_damages
total_damages = update_damages(damages)
# print(total_damages)


# write your construct hurricane dictionary function here:
def names_dict(names, months, years, max_sustained_winds, areas_affected, total_damages, deaths):
  dictionary = {}
  for name, month, year, wind, area, damage, death in zip(names, months, years, max_sustained_winds, areas_affected, total_damages, deaths):
    dictionary.update({name:{"Name":name, "Month":month, "Year":year, "Max Sustained Winds":wind, "Areas Affected":area, "Damage":damage, "Deaths":death}})
  return dictionary

hurricanes_by_name = names_dict(names, months, years, max_sustained_winds, areas_affected, total_damages, deaths)
# print(hurricanes_by_name)


# write your construct hurricane by year dictionary function here:
def years_dict(names, months, years, max_sustained_winds, areas_affected, total_damages, deaths):
  dictionary = {}
  for name, month, year, wind, area, damage, death in zip(names, months, years, max_sustained_winds, areas_affected, total_damages, deaths):
    dictionary.update({year:{"Name":name, "Month":month, "Year":year, "Max Sustained Winds":wind, "Areas Affected":area, "Damage":damage, "Deaths":death}})
  return dictionary

hurricanes_by_year = years_dict(names, months, years, max_sustained_winds, areas_affected, total_damages, deaths)
# print(hurricanes_by_year)


# write your count affected areas function here:
def count_area(areas_affected):
  dictionary = {}
  for storm in areas_affected:
    for area in storm:
      if area not in dictionary:
        dictionary.update({area:1})
      else:
        count = dictionary.get(area)
        dictionary.update({area:count+1})
  return dictionary

count_of_areas = count_area(areas_affected)
# print(count_of_areas)


# write your find most affected area function here:
def most_affected(dic):
  location = ""
  times = 0
  for storm, time in dic.items():
    if time > times:
      times = time
      location = storm
  return location, times
most_affected_area, times_affected = most_affected(count_of_areas)
# print(most_affected_area, times_affected)


# write your greatest number of deaths function here:
def greatest_deaths(dic):
  location = ""
  count = 0
  for storm, stats in dic.items():
    if stats.get("Deaths") > count:
      count = stats.get("Deaths")
      location = storm
  return location, count
greatest_number_deaths = greatest_deaths(hurricanes_by_name)
# print(greatest_number_deaths)


# write your catgeorize by mortality function here:
mortality_scale = {0:0, 1:100, 2:500, 3:1000, 4:10000}
mortality_ratings = {0:[],1:[],2:[],3:[],4:[],5:[]}
def mortality_rating(dic, scale):
  for storm, stats in dic.items():
    if stats.get("Deaths") == 0:
      rating = 0
    elif stats.get("Deaths") <= 100:
      rating = 1
    elif stats.get("Deaths") <= 500:
      rating = 2
    elif stats.get("Deaths") <= 1000:
      rating = 3
    elif stats.get("Deaths") <= 10000:
      rating = 4
    else:
      rating = 5
    if rating not in mortality_ratings:
      mortality_ratings.update({rating:[storm]})
    else:
      mortality_ratings[rating].append(storm)
  return mortality_ratings
mortalities = mortality_rating(hurricanes_by_name, mortality_scale)
# print(mortalities)


# write your greatest damage function here:
def greatest_damages(dic):
  greatest = ""
  damages = 0
  for storm, stats in dic.items():
    if type(stats.get("Damage")) == str:
      continue
    if stats.get("Damage") > damages:
      damages = stats.get("Damage")
      greatest = stats.get("Name")
  return greatest, damages
most_damaging_storm, cost = greatest_damages(hurricanes_by_name)
# print(most_damaging_storm, cost)


# write your catgeorize by damage function here:
damage_scale = {0:0, 1:100000000, 2:1000000000, 3:10000000000, 4:50000000000}
damage_ratings = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
def damage_rating(dic, scale):
  rating = 0
  for stats in dic.values():
    if type(stats.get("Damage")) == str:
      continue
    if stats.get("Damage") == scale.get(0):
      rating = 0
    elif stats.get("Damage") <= scale.get(1):
      rating = 1
    elif stats.get("Damage") <= scale.get(2):
      rating = 2
    elif stats.get("Damage") <= scale.get(3):
      rating = 3
    elif stats.get("Damage") <= scale.get(4):
      rating = 4
    else:
      rating = 5
    damage_ratings[rating].append(stats.get("Name"))
  return damage_ratings
ratings = damage_rating(hurricanes_by_name, damage_scale)
# print(ratings)
