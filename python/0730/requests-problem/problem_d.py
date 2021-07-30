import requests
from tmdb import TMDBHelper
from pprint import pprint


def recommendation(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록을 출력.
    추천 영화가 없을 경우 [] 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    tmdb_helper = TMDBHelper('927de0df76ea553f0b9df58439356199')

    movie_id = tmdb_helper.get_movie_id(title)

    url = tmdb_helper.get_request_url(method=f'/movie/{movie_id}/recommendations', region='KR', language='ko')
    
    data = requests.get(url).json()
    if movie_id == None:
        return None
    else:
        title_data = data['results']
        title_list = []
        for i in range(0, len(title_data)):
            title_list.append(title_data[i]['title'])
        return title_list
    

if __name__ == '__main__':
    pprint(recommendation('기생충'))
    pprint(recommendation('그래비티'))
    pprint(recommendation('검색할 수 없는 영화'))

'''
['조커',
 '조조 래빗',
 '1917',
 '원스 어폰 어 타임 인… 할리우드',
 '결혼 이야기',
 '아이리시맨',
 '나이브스 아웃',
 '포드 V 페라리',
 '작은 아씨들',
 '라이트하우스',
 '미드소마',
 '언컷 젬스',
 '더 플랫폼',
 '스타워즈: 라이즈 오브 스카이워커',
 '두 교황',
 '애드 아스트라',
 '버즈 오브 프레이: 할리 퀸의 황홀한 해방',
 '그린 북',
 '살인의 추억',
 '토이 스토리 4',
 '스파이더맨: 파 프롬 홈']
[]
None
'''