# philosopher-lines-database-design-using-RDBMS

- 고대~근대 철학자들의 인용문으로 RDBMS 설계하기

## Data Source
This dataset is originally sourced from Project Gutenberg and privately owned PDFs as mentioned in the
[Kaggle dataset page](https://www.kaggle.com/datasets/kouroshalizadeh/history-of-philosophy/data).

## 전처리한 데이터 구조

![alt text](image.png)

- philosophy 스키마
  - philosopher_lines 테이블
    - title: 철학자 저서의 제목
    - author: 저자 이름
    - school: 철학 학파
    - sentence_ko: 한국어 문장
    - sentence_en: 영어 문장
    - original_publication_date: 원본 출판일
    - corpus_edition_date: 말뭉치 에디션 날짜
    - sentence_length: 문장 길이
    - tokenized_txt: 토큰화된 텍스트
    - lemmatized_str: 원형화된 문자열


## 1. 데이터베이스 설계 다이어그램(ERD)


## 2. MySQL 설정 및 데이터베이스 생성 스크립트

![image](https://github.com/user-attachments/assets/35e82363-9b77-4ad9-bbc9-9a68cf5a56ce)


- csv파일의 인코딩을 인식하지 못해서 json으로 변경 후 진행


### 스키마 및 테이블 생성 과정

### philosophy 스키마 생성

### 1. 첫 테이블 philosopher_lines;
![image](https://github.com/user-attachments/assets/3f3c97d7-465d-4a17-9e4e-7920652386c0)


### 2. 철학자 테이블 생성
CREATE TABLE IF NOT EXISTS philosophers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    school_id INT,
    FOREIGN KEY (school_id) REFERENCES philosophical_schools(id)
);

### 3. 철학 학파 테이블 생성
CREATE TABLE IF NOT EXISTS philosophical_schools (
    id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(255) NOT NULL UNIQUE
);

### 4. 철학 저서 테이블 생성 (DATE를 INT로 변경)
CREATE TABLE IF NOT EXISTS philosophical_works (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    original_publication_date INT,
    corpus_edition_date INT,
    FOREIGN KEY (author_id) REFERENCES philosophers(id)
);
