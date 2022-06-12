import secrets
import pandas as pd
import requests

#match = False

res = requests.get('https://api.jikan.moe/v4/genres/anime')
genre_list = []
for i in range(0, 76):
    genre_list.append(str(res.json()['data'][i]['name']))

col = ['GENRES']
df = pd.DataFrame(genre_list, columns=col)
pd.set_option('display.max_rows', None)


print('Welcome to anime recommender!')
type = input('Anime type: [TV / Movie]? ').lower()
print(df)
mood = input('Genre? ').lower()

i = secrets.randbelow(2000)
response = requests.get(f'https://api.jikan.moe/v4/anime/{i}')

anime_type = str(response.json()['data']['type']).lower()
try:
    anime_genre1 = str(response.json()['data']['genres'][0]['name']).lower()
    anime_genre2 = str(response.json()['data']['genres'][1]['name']).lower()
    anime_genre3 = str(response.json()['data']['genres'][2]['name']).lower()
except IndexError:
    pass

anime_title = response.json()['data']['title']
anime_synopsis = response.json()['data']['synopsis']
if anime_type == type and anime_genre1 == mood:
    print('\nYour anime recommendation is: \n')
    print(anime_title)
    print(anime_synopsis)
    #match = True
elif anime_type == type and anime_genre2 == mood:
    print(anime_title)
    print(anime_synopsis)
elif anime_type == type and anime_genre3 == mood:
    print(anime_title)
    print(anime_synopsis)
else:
    print('No match!')
    print(anime_type)
    print(anime_genre1)
    print(anime_title)
    print(anime_synopsis)
