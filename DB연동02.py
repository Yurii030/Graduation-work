## DB에 직접 문장 삽입
## 데이터 베이스 연동 mysql.coonector모듈
import mysql.connector

## 데이터 베이스 정보
config = {
    "user": "yourID",
    "password": "yourPW",
    "host": "yourURL", #local
    "database": "data", #Database name
    "port": "3306" #port는 최초 설치 시 입력한 값(기본값은 3306)
}

## 문장 입력 및 DB 삽입
def typing(category):
    while(True):
        print("종료 : end")
        tmp = input(category + '영역 문장 입력 : ')
        
        ## 반복 종료
        if tmp == "end":
            break
        else:
            sentence.append(tmp)
        
    ## 반복문으로 리스트에 있는 문장들을 데이터베이스에 저장
    for i in sentence:
        encoded = i.encode('euc-kr', 'ignore').decode('euc-kr')
        cursor.execute(f"insert into {category}(title) values('{encoded}')")


## 카테고리
cat = {1 : 'body', 2 : 'comm', 3 : 'social', 4 : 'art', 5 : 'science'}

## DB에 연결
conn = mysql.connector.connect(**config)

## db select, insert, update, delete 작업 객체
cursor = conn.cursor()

## DB에 연결
conn = mysql.connector.connect(**config)

## db select, insert, update, delete 작업 객체
cursor = conn.cursor()

## 무한 루프
while(True):
    ## 문장 리스트 초기화
    sentence = []
    print("문장을 입력할 영억 선택")
    print("1 : body\n2 : comm\n3 : social\n4 : art\n5 : science")
    print("종료 : 0, 6")
    sel = int(input("영역 : "))
    
    ## 반복 종료
    if sel == 0 or sel == 6:
        break
    
    print(cat[sel] + '영역')
    typing(cat[sel])

print("COMMIT..")
# Commit
conn.commit()
