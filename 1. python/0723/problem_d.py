import json


def max_revenue(movies):
    revenue_max = 0
    for i in range(0, len(movies)):
        m_number = movies[i]["id"]
        number_json = open(f'data/movies/{m_number}.json', encoding='UTF8')
        number_list = json.load(number_json)
        if number_list['revenue'] > revenue_max:
            revenue_max = number_list['revenue']
            max_title = number_list['title']
    return max_title

    # 여기에 코드를 작성합니다.  
        

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))