import json



def dec_movies(movies):
    dec_title = []
    for i in range(0, len(movies)):
        m_number = movies[i]["id"]
        title_json = open(f'data/movies/{m_number}.json', encoding='UTF8')
        title_list = json.load(title_json)
        release_date = title_list['release_date']
        if release_date.split('-')[1] == '12':
            print(title_list['title'])
            dec_title.append(title_list['title'])
    return dec_title
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))