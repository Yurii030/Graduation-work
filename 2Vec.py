from konlpy.tag import Okt ##konlpy에서 OKt형태소 분석기 사용
from gensim.models import Word2Vec ## Train을 위한 모듈(gensim+word2vec모델만들어서 사용)
import mariadb ##db연동을 위한 모듈
import sys ##파이썬 대화형 프롬프트사용을 위한 모듈
import os  ##작업 디렉토리 지정을 위한 모듈
os.chdir('E:\\senier_project\\run\\Data\\')
twitter = Okt() ## Okt객체 생성 메서드
## 데이터베이스정보
def dbconnect():
        conn = mariadb.connect(
            user="root",
            password="root",
            host="127.0.0.1",
            port=3306,
            database="category"
            )
        return conn

def value(conn,category):
    cur = conn.cursor()
    # connection 객체로부터 cursor()메서드를 호출
    sql=sql = "SELECT * FROM " + category
    cur.execute(sql) # 데이터 행의 개수
    result= cur.fetchall() ##모든 데이터 한꺼번에 호출
    db_result = []
    for i in result:
        db_result.append([i[0], category])##리스트 마지막에 값추가
    return db_result
## 영역분류
cat = ['body', 'comm', 'social', 'art', 'science']
line=[]

conn = dbconnect()
try:
    for i in cat:
        line += value(conn,i)
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
    
token = []
embeddingmodel = []

for i in line:
    content = i[1]  # csv에서 뉴스 제목 또는 뉴스 본문 column으로 변경
    sentence = twitter.pos(i[0], norm=True, stem=True)
    temp = []
    temp_embedding = []
    all_temp = []
    for k in range(len(sentence)):
        temp_embedding.append(sentence[k][0])
        temp.append(sentence[k][0] + '/' + sentence[k][1])
    all_temp.append(temp)
    embeddingmodel.append(temp_embedding)
    category = i[1]  # csv에서 category column으로 변경
    category_number_dic = {'body': 0, 'comm': 1, 'social': 2, 'art': 3, 'science': 4}
    all_temp.append(category_number_dic.get(category))
    token.append(all_temp)
print("토큰 처리 완료")


embeddingmodel = []
for i in range(len(token)):
    temp_embeddingmodel = []
    for k in range(len(token[i][0])):
        temp_embeddingmodel.append(token[i][0][k])
    embeddingmodel.append(temp_embeddingmodel)
embedding = Word2Vec(embeddingmodel, size=300, window=5, min_count=10, sg=1)
embedding.save('post.embedding')
print('exit')
