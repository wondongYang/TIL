import requests
from tmdb import TMDBHelper


def popular_count():
    """
    popular 영화목록의 개수 출력.
    """
    tmdb_helper = TMDBHelper('927de0df76ea553f0b9df58439356199')

    url = tmdb_helper.get_request_url(region='KR', language='ko')

    data = requests.get(url).json()
    popular_movies = data['results']
    return len(popular_movies)
    

if __name__ == '__main__':
    print(popular_count()) #=> 20
