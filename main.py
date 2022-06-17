import secrets
from typing import Match
import pandas as pd
import requests
import pprint
import time
import csv

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
        time.sleep(5)
        response = requests.get(f'https://api.jikan.moe/v4/anime/{1}')
        # pprint.pprint(response.json())
        anime_type = str(response.json()['data']['type']).lower()
    try:
        anime_genre1 = str(
            response.json()['data']['genres'][0]['name']).lower()
    except IndexError:
        response = requests.get(f'https://api.jikan.moe/v4/anime/{1}')
        anime_type = str(response.json()['data']['type']).lower()
        anime_genre1 = str(
            response.json()['data']['genres'][0]['name']).lower()
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

    anime_img = response.json().get('data', {}).get(
        'images', {}).get('jpg', {}).get('large_image_url', {})
    anime_title = response.json().get('data', {}).get('title', {})
    anime_rating = response.json().get('data', {}).get('rating', {})
    anime_score = response.json().get('data', {}).get('score', {})
    anime_synopsis = response.json().get('data', {}).get('synopsis', {})

    if anime_type == type and anime_genre1 == mood:
        print('\nYour anime recommendation is: \n')
        print(anime_img)
        print(anime_title)
        print(anime_rating)
        print(f'{anime_score}/10')
        print(anime_synopsis)
        data = [[anime_img], [anime_title], [anime_rating],
                [f'{anime_score}/10'], [anime_synopsis]]
        file = open("results.csv", "w", newline="")
        writer = csv.writer(file)
        writer.writerows(data)
        file.close()
        match = True
    elif anime_type == type and anime_genre2 == mood:
        print('\nYour anime recommendation is: \n')
        print(anime_img)
        print(anime_title)
        print(anime_rating)
        print(f'{anime_score}/10')
        print(anime_synopsis)
        data = [[anime_img], [anime_title], [anime_rating],
                [f'{anime_score}/10'], [anime_synopsis]]
        file = open("results.csv", "w", newline="")
        writer = csv.writer(file)
        writer.writerows(data)
        file.close()
        match = True
    elif anime_type == type and anime_genre3 == mood:
        print('\nYour anime recommendation is: \n')
        print(anime_img)
        print(anime_title)
        print(anime_rating)
        print(f'{anime_score}/10')
        print(anime_synopsis)
        data = [[anime_img], [anime_title], [anime_rating],
                [f'{anime_score}/10'], [anime_synopsis]]
        file = open("results.csv", "w", newline="")
        writer = csv.writer(file)
        writer.writerows(data)
        file.close()
        match = True
    else:
        print('No match!')

    return match
