## 1. 진행 과정

1. TMDBHelper 클래스의 get_ruquest_url 함수를 활용하여 크롤링을 진행할 사이트의 url을 지정

2. requests를 이용하여 url에서 data를 수집

3. data 속의 특정 리스트를 할당 

4. 기존 리스트에서 조건에 만족하는 값들을 새로운 리스트에 추가

5. 문제에 만족하는 리스트를 return

   ex) problem_d

```python
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
    url = tmdb_helper.get_request_url(method=f'/movie/{movie_id}/recommendations', region='KR', language='ko') #=> 1
    
    data = requests.get(url).json() #=> 2
    if movie_id == None:
        return None
    else:
        title_data = data['results'] #=> 3
        title_list = []
        for i in range(0, len(title_data)):
            title_list.append(title_data[i]['title']) #=> 4
        return title_list #=> 5
```



## 2. 학습한 내용

- 반복되는 내용을 클래스를 생성하여 줄이는 방법

- url 정보를 통해 그 속의 데이터를 반환받을 수 있다는 점

  

## 3. 느낀점

- 코드가 길어질수록 반복되는 표현이 많아지기 마련
- 단순한 리스트, 식 등이 아닌 긴 문자열이나 함수값 또한 클래스를 통해서 모든사람이 알아보기 쉽고 간단한 코드로 구성할 수 있음
- 이러한 구조를 단순화시키는 작업에 익숙해져야겠다고 느낌