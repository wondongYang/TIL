-- 주석
/* 
여러줄 주석 
SQL은 대소문자 구분x
기본 문법(변하지 않는 부분 - 대문자)
변수(변하는 부분 - 소문자)
*/
-- 데이터 전체 조회 SELECT
SELECT * FROM examples;

-- 테이블 생성
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
adress TEXT NOT NULL
);

-- 데이터 입력
INSERT INTO classmates (name,age) VALUES ('홍길동', 23);
INSERT INTO classmates VALUES ('홍길동', 30, '서울');
INSERT INTO classmates VALUES
('홍길동', 30, '서울'),
('김철수', 30, '대전'),
('이싸피', 26, '광주'),
('박삼성', 29, '구미'),
('최전자', 28, '부산');

-- 데이터 불러오기
SELECT * FROM classmates;

SELECT rowid, * FROM classmates;
SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
SELECT rowid, name FROM classmates WHERE adress='서울';
SELECT DISTINCT age FROM classmates;

-- 테이블 삭제
DROP TABLE classmates;

-- 데이터 삭제
DELETE FROM classmates WHERE rowid=5;

-- 데이터 수정
UPDATE classmates SET name='홍길동', adress='제주도' WHERE rowid=5;

CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

SELECT * FROM users WHERE age >= 30;
SELECT age, last_name FROM users WHERE age >= 30 AND last_name = '김';
SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users WHERE age >= 30;
SELECT first_name, MAX(balance) FROM users;
SELECT AVG(balance) FROM users WHERE age >= 30;
SELECT * FROM users WHERE age LIKE '2_';
SELECT * FROM users WHERE phone LIKE '02-%';
SELECT * FROM users WHERE first_name LIKE '%준';
SELECT * FROM users WHERE phone LIKE '%-5114-%';

SELECT * FROM users ORDER BY age ASC LIMIT 10;
SELECT * FROM users ORDER BY age ASC, last_name ASC LIMIT 10;
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;

SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;

CREATE TABLE articles (
    title TEXT NO NULL,
    content TEXT NOT NULL
);

INSERT INTO articles VALUES('1번제목', '1번내용');

ALTER TABLE articles RENAME TO news;
ALTER TABLE news ADD COLUMN created_at TEXT;
INSERT INTO news VALUES('제목', '내용', datetime('now'));
ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';