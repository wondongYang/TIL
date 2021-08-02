import json
from pprint import pprint


def movie_info(movies, genres):
    data_list = []
    names_lists = []
    for k in range(0, len(movies)):
        names_list = []
        ids_list = movies[k]['genre_ids']
        for i in range(0, len(genres)):
            for j in range(0, len(ids_list)):
                if genres[i]['id'] == ids_list[j]:
                    names = genres[i]['name']
                    names_list.append(names)
        names_lists.append(names_list)
        key_list = ['genre_ids', 'id', 'overview', 'poster_path', 'title', 'vote_average']
        data = {}
        for key in key_list:
          data[key] = movies[k][key]
        data.pop('genre_ids')
        data['genre_names'] = names_list
        data_list.append(data)
    return data_list
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))