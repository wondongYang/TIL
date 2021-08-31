from io import IOBase
import json
from pprint import pprint


def movie_info(movie, genres):
    ids_list = movie['genre_ids']
    names_list = []
    for i in range(0, len(genres)):
        for j in range(0, len(ids_list)):
            if genres[i]['id'] == ids_list[j]:
                names = genres[i]['name']
                names_list.append(names)
    key_list = ['genre_ids', 'id', 'overview', 'poster_path', 'title', 'vote_average']
    data = {}
    for key in key_list:
        data[key] = movie[key]
    data.pop('genre_ids')
    data['genre_names'] = names_list
    return data
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))