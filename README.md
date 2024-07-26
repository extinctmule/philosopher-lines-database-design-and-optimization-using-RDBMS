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

## 추가할 테이블

### 1. philosophical_works 철학 저서 테이블

- philosophical_works
  - title
  - author_id
  - publication_date
