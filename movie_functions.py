import pandas as pd
import numpy as np
import string
def parse_str(s):
    ''' convert s to a list of numbers
        example:
        input: s = '[12, 14, 10751]'
        output: ['12', '14', '10751']
    '''
    # strip all punctuation from a string
    s = s.translate(str.maketrans('', '', string.punctuation))
    # string to list
        # alternative: s_list = [int(n) for n in s.split()]
    return s.split()


def id_genre():
    tmdb_genres=[{'id': 28, 'name': 'Action'},
            {'id': 12, 'name': 'Adventure'},
            {'id': 16, 'name': 'Animation'},
            {'id': 35, 'name': 'Comedy'},
            {'id': 80, 'name': 'Crime'},
            {'id': 99, 'name': 'Documentary'},
            {'id': 18, 'name': 'Drama'},
            {'id': 10751, 'name': 'Family'},
            {'id': 14, 'name': 'Fantasy'},
            {'id': 36, 'name': 'History'},
            {'id': 27, 'name': 'Horror'},
            {'id': 10402, 'name': 'Music'},
            {'id': 9648, 'name': 'Mystery'},
            {'id': 10749, 'name': 'Romance'},
            {'id': 878, 'name': 'Science Fiction'},
            {'id': 10770, 'name': 'TV Movie'},
            {'id': 53, 'name': 'Thriller'},
            {'id': 10752, 'name': 'War'},
            {'id': 37, 'name': 'Western'}]
    # create a dict with {id_value1:genre1, id_value2:genre2} from tmdb_genres
    genre_dict = {}
    for pair in tmdb_genres:
        genre_dict[pair['id']] = pair['name']
    return genre_dict
