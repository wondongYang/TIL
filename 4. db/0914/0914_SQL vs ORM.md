

![image-20210914131000169](C:\Users\82108\AppData\Roaming\Typora\typora-user-images\image-20210914131000169.png)

## 1. SQL Query

위 countries 테이블을 바탕으로 아래 문제에 해당하는 SQL query문을 작성하고 실행하시오..

1. countries 테이블을 생성하시오.

   ```sqlite
   CREATE TABLE coutries (
   room_num TEXT,
   check_in TEXT,
   check_out TEXT,
   grade TEXT,
   price INTEGER
   );
   ```

2. 데이터를 입력하시오.

   ```sqlite
   INSERT INTO countries VALUES
   ('B203', '2019-12-31', '2020-01-03', 'suite', 900),
   ('1102', '2020-01-04', '2020-01-08', 'suite', 850),
   ('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
   ('807', '2020-01-04', '2020-01-07', 'superior', 300);
   ```

3) 테이블의 이름을 hotels로 변경하시오.

   ```sqlite
   ALTER TABLE countries RENAME TO hotels;
   ```

4. 객실 가격을 내림차순으로 정렬하여 상위 2개의 room_num과 price를 조회하시오.

   ```sqlite
   SELECT room_num, price FROM hotels
   ORDER BY price DESC LIMIT 2;
   ```

5. grade 별로 분류하고 분류된 grade 개수를 내림차순으로 조회하시오.

   ```sqlite
   SELECT grade, count(*) FROM hotels
   GROUP BY grade ORDER BY count(*) DESC;
   ```

6. 객실의 위치가 지하 혹은 등급이 deluxe인 객실의 모든 정보를 조회하시오.

   ```sqlite
   SELECT * FROM hotels
   WHERE room_num LIKE 'B%' OR grade = 'deluxe';
   ```

7) 지상층 객실이면서 2020년 1월 4일에 체크인 한 객실의 목록을 price 오름차순으로 조회하시오.

   ```sqlite
   SELECT * FROM hotels
   WHERE room_num NOT LIKE 'B%' AND check_in = '2020-01-04' ORDER BY price;
   ```



## 2.  SQL ORM 비교하기

주어진 정보를 활용하여 작성된 SQL문과 대응하는 ORM문을 작성하고 실행하시오.

![image-20210914131151914](C:\Users\82108\AppData\Roaming\Typora\typora-user-images\image-20210914131151914.png)

1. user 테이블 전체 데이터를 조회하시오.

   ```sqlite
   SELECT * FROM users_user;
   ```

   ```shell
   users_user.objects.all()
   ```

2. id가 19인 사림의 age를 조회하시오. 

   ```sqlite
   SELECT age FROM users_user WHERE id = 19;
   ```

   ```shell
   users_user.objects.get(pk=19)
   ```

3. 모든 사람의 age를 조회하시오. 

   ```sqlite
   SELECT age FROM users_user;
   ```

   ```shell
   users_user.objects.all().values('age')
   ```

4. age가 40 이하인 사림들의 id와 balance를 조회하시오. 

   ```sqlite
   SELECT id, balance FROM users_user WHERE age <= 40;
   ```

   ```shell
   users_user.objects.filter(age<=40).values('id', 'balance')
   ```

5. ast_name이 ‘김’이고 balance가 500 이상인 사람들의 first_name을 조회하시오. 

   ```sqlite
   SELECT first_name FROM users_user
   WHERE last_name = '김' AND balance >= 500;
   ```

   ```shell
   users_user.objects.filter(last_name='김', balance>=500).values('first_name')
   ```

6. first_name이 ‘수’로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회하시오. 

   ```sqlite
   SELECT balance FROM users_user
   WHERE first_name LIKE '%수' AND country = '경기도';
   ```

   ```shell
   users_user.objects.filter(first_name__endswith='수', country='경기도').values('balance')
   ```

7. balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수를 구하시오. 

   ```sqlite
   SELECT COUNT(*) FROM users_user
   WHERE balance >= 2000 OR age <= 40;
   ```

   ```shell
   from django.db.models import Q
   users_user.objects.filter(Q(balance>=2000)|Q(age<=40)).count()
   ```

8. phone 앞자리가 ‘010’으로 시작하는 사람의 총원을 구하시오. 

   ```sqlite
   SELECT COUNT(*) FROM users_user
   WHERE phone LIKE '010%';
   ```

   ```shell
   users_user.objects.filter(phone__startswith='010').count()
   ```

9. 이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정하시오. 

   ```sqlite
   UPDATE users_user SET country = '경기도'
   WHERE first_name = '옥자' AND last_name = '김';
   
   SELECT country FROM users_user
   WHERE first_name = '옥자' AND last_name = '김';
   ```

   ```shell
   user = User.object.get(first_name='옥자', last_name='김')
   user.country = '경기도'
   user.save()
   user.country
   ```

10. 이름이 ‘백진호’인 사람을 삭제하시오. 

    ```sqlite
    DELETE users_user
    WHERE first_name = '진호' AND last_name = '백';
    
    SELECT * FROM users_user
    WHERE first_name = '진호' AND last_name = '백';
    ```

    ```shell
    User.objects.get(first_name='진호', last_name='백').delete()
    ```

11. balance를 기준으로 상위 4명의 first_name, last_name, balance를 조회하시오. 

    ```sqlite
    SELECT first_name, last_name, balance FROM users_user
    ORDER BY balance DESC LIMIT 4;
    ```

    ```shell
    users_user.objects.order_by('-balance')[0:4].values('first_name', 'last_name', 'balance')
    ```

12. phone에 ‘123’을 포함하고 age가 30미만인 정보를 조회하시오

    ```sqlite
    SELECT * FROM users_user
    WHERE phone LIKE '%123%' AND age < 30;
    ```

    ```shell
    users_user.objects.get(phone__containes=='123', age<30)
    ```

13. phone이 ‘010’으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오. 

    ```sqlite
    SELECT DISTINC country FROM users_user
    WHERE phone LIKE '010%';
    ```

    ```shell
    users_user.objects.get(phone__startswith=='010').values('country')
    ```

14. 모든 인원의 평균 age를 구하시오. 

    ```sqlite
    SELECT AVE(age) FROM users_user;
    ```

    ```shell
    from django.db.models import Avg
    users_user.objects.aggregate(Avg('age'))
    ```

15. 박씨의 평균 balance를 구하시오

    ```sqlite
    SELECT AVG(balance) FROM users_user
    WHERE last_name = '박';
    ```

    ```shell
    from django.db.models import Avg
    users_user.objects.filter(last_name='박').aggregate(Avg('balance'))
    ```

16. 경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오. 

    ```sqlite
    SELECT MAX(balance) FROM users_user
    WHERE country = '경상북도';
    ```

    ```shell
    from django.db.models import Max
    users_user.objects.filter(country='경상북도').aggregate(Max('balance'))
    ```

17. 제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오

    ```sqlite
    SELECT first_name FROM users_user
    WHERE country = '제주특별자치도' ORDER BY balance DESC LIMIT 1;
    ```

    ```shell
    from django.db.models import Max
    users_user.objects.filter(country='제주특별자치도').aggregate(Max('balance')).values('first_name')
    ```
    
    