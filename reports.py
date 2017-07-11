def read_file(file_name):
    import csv
    data = []
    with open(file_name) as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            data.append(row)
    return data

def count_games(file_name):
    data = read_file(file_name)
    return len(data)


def decide(file_name, year):
    data = read_file(file_name)
    for row in data:
        if row[2] == str(year):
            return True
    return False


def get_latest(file_name):
    data = read_file(file_name)
    game_name = data[0][0]
    game_release = data[0][2]
    for row in data:
        if int(game_release) < int(row[2]):
            game_name = row[0]
            game_release = row[2]
    return game_name


def count_by_genre(file_name, genre):
    data = read_file(file_name)
    counter = 0
    for row in data:
        if genre == row[3]:
            counter += 1
    return counter


def get_line_number_by_title(file_name, title):
    data = read_file(file_name)
    line_number = 1
    for row in data:
        if title == row[0]:
            return line_number
        line_number += 1
    raise ValueError

def get_genres(file_name):
    data = read_file(file_name)
    genres = set()
    for row in data:
        genres.add(row[3])
    return sorted(list(genres))


def when_was_top_sold_fps(file_name):
    data = read_file(file_name)
    game_sold = 0
    game_release = 0
    for row in data:
        if row[3] == "First-person shooter" and game_sold < float(row[1]):
            game_sold = float(row[1])
            game_release = int(row[2])
    if game_release > 0:
        return game_release
    raise ValueError
