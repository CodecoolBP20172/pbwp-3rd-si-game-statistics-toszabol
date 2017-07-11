from reports import *

FILE_NAME = 'game_stat.txt'


# Export functions
def write_line(file_handler, line):
    file_handler.writelines(str(line) + '\n')


export = open('export.txt', 'w')
write_line(export, count_games(FILE_NAME))
write_line(export, decide(FILE_NAME, 2004))
write_line(export, get_latest(FILE_NAME))
write_line(export, count_by_genre(FILE_NAME, 'RPG'))
write_line(export, get_line_number_by_title(FILE_NAME, 'The Sims 3'))
write_line(export, get_genres(FILE_NAME))
write_line(export, when_was_top_sold_fps(FILE_NAME))
export.close()
