'''
PART2
'''


def read_file(file_name):
    import csv
    data = []
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            data.append(row)
    return data


# 1  What is the title of the most played game (i.e. sold the most copies)?
def get_most_played(file_name):
        data = read_file(file_name)
        game_name = data[0][0]
        game_sold = data[0][1]
        for row in data:
            if int(game_sold) < int(float(row[1])):
                game_name = row[0]
                game_sold = row[1]
        return game_name


# 2 How many copies have been sold total?
def sum_sold(file_name):
    data = read_file(file_name)
    counter = 0.0
    for row in data:
        counter += float(row[1])
    return counter


# 3 What is the average selling?
def get_selling_avg(file_name):
    data = read_file(file_name)
    counter = 0
    for row in data:
        counter += float(row[1])
        average_sold = counter / len(data)
    return average_sold


# 4 How many characters long is the longest title?
def count_longest_title(file_name):
    data = read_file(file_name)
    game_name = len(data[0][0])
    for row in data:
        if game_name < len(row[0]):
            game_name = len(row[0])
    return game_name


# 5 What is the average of the release dates?
def get_date_avg(file_name):
    import math
    data = read_file(file_name)
    counter = 0
    for row in data:
        counter += int(row[2])
        average_year = counter / len(data)
    return math.ceil(average_year)


# 6 What properties has a game?
def get_game(file_name, title):
    data = read_file(file_name)
    for row in data:
        if title in row:
            properties = [row[0], float(row[1]), int(row[2]), row[3], row[4]]
    return properties


# nice to have
# 1 How many games are there grouped by genre?
def count_grouped_by_genre(file_name):
    data = read_file(file_name)
    genre_list = [row[3] for row in data]
    genre_dict = {}
    for item in genre_list:
        if item in genre_dict:
            genre_dict[item] += 1
        else:
            genre_dict[item] = 1
    return genre_dict


# 2 What is the date ordered list of the games?
def get_date_ordered(file_name):
    from operator import itemgetter, attrgetter
    data = read_file(file_name)
    sort_by_alphabet = sorted(data, key=itemgetter(0))
    sorted_data = sorted(sort_by_alphabet, key=itemgetter(2), reverse=True)
    sorted_title = [row[0] for row in sorted_data]
    return sorted_title
