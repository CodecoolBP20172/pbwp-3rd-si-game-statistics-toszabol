'''
PART2
'''
import pprint
from reports import *

FILE_NAME = 'game_stat.txt'
pp = pprint.PrettyPrinter()


# Printing functions
pp.pprint(get_most_played(FILE_NAME))
pp.pprint(sum_sold(FILE_NAME))
pp.pprint(get_selling_avg(FILE_NAME))
pp.pprint(count_longest_title(FILE_NAME))
pp.pprint(get_date_avg(FILE_NAME))
pp.pprint(get_game(FILE_NAME, 'World of Warcraft'))
pp.pprint(count_grouped_by_genre(FILE_NAME))
pp.pprint(get_date_ordered(FILE_NAME))
