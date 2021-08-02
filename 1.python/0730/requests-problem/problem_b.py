import requests
from tmdb import TMDBHelper
from pprint import pprint


def vote_average_movies():
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    tmdb_helper = TMDBHelper('927de0df76ea553f0b9df58439356199')

    url = tmdb_helper.get_request_url(region='KR', language='ko')

    data = requests.get(url).json()
    popular_movies = data['results']
    high_vote = []
    for i in range(0, len(popular_movies)):
        if popular_movies[i]['vote_average'] >= 8.0:
            high_vote.append(popular_movies[i])
    return high_vote


if __name__ == '__main__':
    pprint(vote_average_movies())

'''
[{'adult': False,
  'backdrop_path': '/yizL4cEKsVvl17Wc1mGEIrQtM2F.jpg',
  'genre_ids': [28, 878],
  'id': 588228,
  'original_language': 'en',
  'original_title': 'The Tomorrow War',
  'overview': '현재로 긴급 메시지를 전하기 위해 2051년에서 온 한 무리의 시간 여행자들이 도착한다. 메세지의 내용은 30년 '     
              '동안 미래 인류가 치명적인 외계 종족과 세계 전쟁에서 지고 있다는 것. 인류가 생존할 수 있는 유일한 희망은 현재 '
              '세계의 군인과 민간인들이 미래로 보내서 전쟁에 참여하는 것이다. 어린 딸을 위해 세상을 구하기로 결심한 댄 '     
              '포레스터는 지구의 운명을 다시 쓰기 위해 뛰어난 과학자와 사이가 멀어진 아버지와 함께 팀을 이룬다.',
  'popularity': 2514.554,
  'poster_path': '/34nDCQZwaEvsy4CFO5hkGRFDCVU.jpg',
  'release_date': '2021-07-02',
  'title': '내일의 전쟁',
  'video': False,
  'vote_average': 8.2,
  'vote_count': 2971},
 {'adult': False,
  'backdrop_path': '/620hnMVLu6RSZW6a5rwO8gqpt0t.jpg',
  'genre_ids': [16, 35, 10751, 14],
  'id': 508943,
  'original_language': 'en',
  'original_title': 'Luca',
  'overview': '이탈리아 리비에라의 아름다운 해변 마을, 바다 밖 세상이 궁금하지만, 두렵기도 한 호기심 많은 소년 루카. 자칭 '  
              '인간세상 전문가 알베르토와 함께 모험을 감행하지만, 물만 닿으면 바다 괴물로 변신하는 비밀 때문에 아슬아슬하기만
 '
              '하다. 새로운 친구 줄리아와 함께 젤라또와 파스타를 실컷 먹고 스쿠터 여행을 꿈꾸는 여름은 그저 즐겁기만 한데…', 
  'popularity': 2543.232,
  'poster_path': '/pMDSbOXeQInoMAa0YgezBRnCDuz.jpg',
  'release_date': '2021-06-17',
  'title': '루카',
  'video': False,
  'vote_average': 8.1,
  'vote_count': 3312},
 {'adult': False,
  'backdrop_path': '/6MKr3KgOLmzOP6MSuZERO41Lpkt.jpg',
  'genre_ids': [35, 80],
  'id': 337404,
  'original_language': 'en',
  'original_title': 'Cruella',
  'overview': '재능은 있지만 밑바닥 인생을 살던 에스텔라는 우여곡절 끝에 런던에 오게 된다. 그곳에서 운명처럼 재스퍼와 '      
              '호레이스를 만난 에스텔라는 뛰어난 패션 감각을 이용해 완벽한 변장과 빠른 손놀림으로 런던 거리를 싹쓸이한다. '  
              '도둑질이 지겹게 느껴질 때 쯤, 꿈에 그리던 리버티 백화점에 들어가게 된 에스텔라. 그곳에서 런던 패션계를 꽉 '   
              '쥐고 있는 남작 부인을 만나 충격적 사건을 겪게 되며, 에스텔라는 런던 패션계를 발칵 뒤집을 파격 아이콘 '        
              '크루엘라로 새롭게 태어나게 되는데...',
  'popularity': 1373.017,
  'poster_path': '/rJkDiGzHgFNBf8LUHX8IOL0IiVh.jpg',
  'release_date': '2021-05-26',
  'title': '크루엘라',
  'video': False,
  'vote_average': 8.4,
  'vote_count': 4418},
 {'adult': False,
  'backdrop_path': '/inJjDhCjfhh3RtrJWBmmDqeuSYC.jpg',
  'genre_ids': [28, 12, 14],
  'id': 399566,
  'original_language': 'en',
  'original_title': 'Godzilla vs. Kong',
  'overview': '콩과 보호자들은 정착할 수 있는 곳을 찾아 특별하고 강력한 유대감을 형성하고 있는 지아와 함께 여정을 떠나게 '   
              '된다. 그러던 중 지구 파괴를 위한 회심의 날을 휘두르는 고질라와 마주하게 되고, 보이지 않는 힘에 의해 맞붙게 '  
              '된 두 전설의 대결은 지구 깊은 곳에 도사린 수수께끼의 시작에 불과할 뿐이었는데…',
  'popularity': 839.661,
  'poster_path': '/sqo672rKMXiLRC5kVcGvBRebkp.jpg',
  'release_date': '2021-03-25',
  'title': '고질라 VS. 콩',
  'video': False,
  'vote_average': 8,
  'vote_count': 6526},
 {'adult': False,
  'backdrop_path': '/xPpXYnCWfjkt3zzE0dpCNME1pXF.jpg',
  'genre_ids': [16, 28, 12, 14],
  'id': 635302,
  'original_language': 'ja',
  'original_title': '劇場版「鬼滅の刃」無限列車編',
  'overview': '혈귀로 변해버린 여동생 네즈코를 인간으로 되돌릴 단서를 찾아 비밀조직 귀살대에 들어간 탄지로. 젠이츠, 이노스케 
와 '
              '새로운 임무 수행을 위해 무한열차에 탑승 후 귀살대 최강 검사 염주 렌고쿠와 합류한다. 달리는 무한열차에서 '     
              '승객들이 하나 둘 흔적 없이 사라지자 숨어있는 식인 혈귀의 존재를 직감하는 렌고쿠. 귀살대 탄지로 일행과 최강 '  
              '검사 염주 렌고쿠는 어둠 속을 달리는 무한열차에서 모두의 목숨을 구하기 위해 예측불가능한 능력을 가진 혈귀와 '  
              '목숨을 건 혈전을 시작하는데...',
  'popularity': 775.967,
  'poster_path': '/m2FNRngyJMyxLatBMJR8pbeG2v.jpg',
  'release_date': '2021-01-27',
  'title': '극장판 귀멸의 칼날: 무한열차 편',
  'video': False,
  'vote_average': 8.4,
  'vote_count': 1430},
 {'adult': False,
  'backdrop_path': '/pcDc2WJAYGJTTvRSEIpRZwM3Ola.jpg',
  'genre_ids': [28, 12, 14, 878],
  'id': 791373,
  'original_language': 'en',
  'original_title': "Zack Snyder's Justice League",
  'overview': '슈퍼맨이 죽고 지구에 어둠의 그림자가 드리운다. 마더박스를 차지하기 위해 빌런 스테픈울프가 파라데몬 군단을 이끌
고 '
              '지구에 온 것이다. 지구를 지키기 위해 목숨을 바친 슈퍼맨의 희생이 헛되지 않도록 하기 위해 브루스 웨인은 '      
              '다이애나 프린스와 적에 맞서기로 한다. 배트맨과 원더 우먼은 새로이 등장한 위협에 맞서 싸우기 위해 특별한 능력을
 '
              '가진 메타휴먼, 아쿠아맨과 사이보그, 플래시를 찾아가 설득하여 힘을 합친다. 드디어 한 팀이 된 저스티스 리그. '  
              '혹시 스테픈울프와 데사드 그리고 다크사이드를 물리치기에 너무 늦어버린 것이 아닐까?',
  'popularity': 670.865,
  'poster_path': '/qd7iPB26bwMPZqRcnflzAeDkMn.jpg',
  'release_date': '2021-03-18',
  'title': '잭 스나이더의 저스티스 리그',
  'video': False,
  'vote_average': 8.4,
  'vote_count': 6149}]
'''