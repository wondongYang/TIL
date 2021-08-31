import requests
from tmdb import TMDBHelper
from pprint import pprint


def credits(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록과 목록을 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    tmdb_helper = TMDBHelper('927de0df76ea553f0b9df58439356199')

    movie_id = tmdb_helper.get_movie_id(title)

    url = tmdb_helper.get_request_url(method=f'/movie/{movie_id}/credits', language='ko')
    
    data = requests.get(url).json()
    if movie_id == None:
        return None
    else:
        cast_data = data['cast']
        cast_list = []
        for i in range(0, len(cast_data)):
            if cast_data[i]['cast_id'] < 10:
                cast_list.append(cast_data[i]['name'])
        crew_data = data['crew']
        crew_list = []
        for i in range(0, len(crew_data)):
            if crew_data[i]['department'] == 'Directing':
                crew_list.append(crew_data[i]['name'])
        return {'cast': cast_list, 'crew': crew_list}


    

if __name__ == '__main__':
    pprint(credits('기생충'))
    pprint(credits('검색할 수 없는 영화'))

'''
{'cast': ['Song Kang-ho',
          'Lee Sun-kyun',
          'Cho Yeo-jeong',
          'Choi Woo-shik',
          'Park So-dam',
          'Lee Jung-eun',
          'Jang Hye-jin'],
 'crew': ['Bong Joon-ho',
          'Park Hyun-cheol',
          'Han Jin-won',
          'Kim Seong-sik',
          'Lee Jung-hoon',
          'Yoon Young-woo']}
None
'''