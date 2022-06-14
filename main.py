import secrets
from typing import Match
import pandas as pd
import requests
import pprint
import time

res = requests.get('https://api.jikan.moe/v4/genres/anime')
match = True
genre_list = []

for i in range(0, 76):
    genre_list.append(str(res.json()['data'][i]['name']))

col = ['GENRES']
df = pd.DataFrame(genre_list, columns=col)
pd.set_option('display.max_rows', None)


def find_anime(type, mood):
    match = False
    i = secrets.randbelow(2000)
    response = requests.get(f'https://api.jikan.moe/v4/anime/{i}')
    # pprint.pprint(response.json())
    try:
        anime_type = str(response.json()['data']['type']).lower()
    except KeyError:
        time.sleep(10)
        response = requests.get(f'https://api.jikan.moe/v4/anime/{1}')
        anime_type = str(response.json()['data']['type']).lower()
    try:
        anime_genre1 = str(
            response.json()['data']['genres'][0]['name']).lower()
    except IndexError:
        pass
    try:
        anime_genre2 = str(
            response.json()['data']['genres'][1]['name']).lower()
    except IndexError:
        anime_genre2 = str(
            response.json()['data']['genres'][0]['name']).lower()
    try:
        anime_genre3 = str(
            response.json()['data']['genres'][2]['name']).lower()
    except IndexError:
        anime_genre3 = str(
            response.json()['data']['genres'][0]['name']).lower()

    anime_title = response.json().get('data', {}).get('title', {})
    anime_rating = response.json().get('data', {}).get('rating', {})
    anime_score = response.json().get('data', {}).get('score', {})
    anime_synopsis = response.json().get('data', {}).get('synopsis', {})

    if anime_type == type and anime_genre1 == mood:
        print('\nYour anime recommendation is: \n')
        print(anime_title)
        print(anime_rating)
        print(f'{anime_score}/10')
        print(anime_synopsis)
        match = True
    elif anime_type == type and anime_genre2 == mood:
        print('\nYour anime recommendation is: \n')
        print(anime_title)
        print(anime_rating)
        print(f'{anime_score}/10')
        print(anime_synopsis)
        match = True
    elif anime_type == type and anime_genre3 == mood:
        print('\nYour anime recommendation is: \n')
        print(anime_title)
        print(anime_rating)
        print(f'{anime_score}/10')
        print(anime_synopsis)
        match = True
    else:
        print('No match!')

    return match