## 최종 GUI
import mysql.connector
import os
os.chdir('C:/anaconda/morpy/Bi_LSTM/')
import import_ipynb         ## ipynb(주피터 노트북) 파일 임포트를 위한 모듈
import Word2Vec as Word2Vec ## 벡터화 모듈
import Bi_LSTM as Bi_LSTM
import tensorflow as tf
from tkinter import *
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import gensim               ## 벡터화 모듈
import os

os.chdir('C:/anaconda/morpy/Bi_LSTM/data')
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

#데이터 베이스 정보
config = {
    "user": "yourID",
    "password": "yourPW",
    "host": "yourURL", #local
    "database": "data", #Database name
    "port": "3306" #port는 최초 설치 시 입력한 값(기본값은 3306)
}

def insert(title, kind):
    date = datetime.now()
    nowdate = date.strftime('%Y-%m-%d')
    conn = mysql.connector.connect(**config)
    # db select, insert, update, delete 작업 객체
    cursor = conn.cursor()
    user2 = user.get("1.0", "end")
    user2 = user2[:-1]
    cursor.execute("select num, name from kid")
    row = cursor.fetchall()
    
    #테이블 이름 탐색
    for i in range(len(row)):
        if int(user2) == row[i][0]:
            tablename = row[i][1] + str(row[i][0])
            
    print(tablename)
    sql ="insert into " + tablename +"(title, kinds, date) values(%s, %s, %s)"
    val = (title, kind ,nowdate)
    cursor.execute(sql,val)
    print("저장이 완료되었습니다.")
    conn.commit()

#텍스트 박스에서 입력된 값 출력
def bnt():
    result = txt.get("1.0","end")
    full, cname = Grade(result)
    insert(result, cname)
    txt2.set(full[0])
    txt3.set(full[1])
    txt4.set(full[2])
    txt5.set(full[3])
    txt6.set(full[4])
    txt7.set(result + "(은)는 " + cname + "(으)로  분류되었습니다")
    
#문장 입력 새창
def bnt2():
    #새창
    root2 = Toplevel(root)
    root2.title("일지작성")
    root2.configure(bg='white')
    root2.geometry("500x425")
    root2.resizable(False, False)
    title1 = Label(root2, text = "원생 번호", bg = 'white')
    title1.place(x = 1, y = 0)
    global user
    user = Text(root2, width=20, height = 1)
    user.place(x = 3, y = 25)
    title2 = Label(root2, text = "문장입력", bg = 'white')
    title2.place(x = 1, y = 70)
    #텍스트 박스 
    global txt
    txt = Text(root2, width=50, height = 3)
    txt.place(x = 3, y = 100)
    #입력 버튼
    btn = Button(root2, text = "입력", command = bnt, width = 5, height = 2)
    btn.place(x = 370, y = 100)
    global txt2 , txt3, txt4 ,txt5, txt6, txt7
    txt2 = StringVar()
    txt2.set("신체건강 %")
    label = Label(root2, textvariable = txt2, bg = 'white')
    label.place(x = 0, y = 200)
    txt3 = StringVar()
    txt3.set("의사소통 %")
    label2 = Label(root2,textvariable = txt3, bg = 'white')
    label2.place(x = 0, y = 225)
    txt4 = StringVar()
    txt4.set("사회관계 %")
    label3 = Label(root2,textvariable = txt4, bg = 'white')
    label3.place(x = 0, y = 250)
    txt5 = StringVar()
    txt5.set("예술경험 %")
    label4 = Label(root2,textvariable = txt5, bg = 'white')
    label4.place(x = 0, y = 275)
    txt6 = StringVar()
    txt6.set("자연탐구 %")
    label5 = Label(root2,textvariable = txt6, bg = 'white')
    label5.place(x = 0, y = 300)
    txt7 = StringVar()
    txt7.set("은 로 분류되었습니다.") 
    label6 = Label(root2, textvariable = txt7, bg = 'white')
    label6.place(x = 1, y = 375)

    title3 = Label(root2, text = "영역 :    %", bg = 'white')
    title3.place(x = 1, y = 170)
    title4 = Label(root2, text = "분류결과", bg = 'white')
    title4.place(x = 1, y = 345)
    
    #칸 나눔
    can = Canvas(root2,width = 500, height=0.01, bg='black',bd=1)
    can.place(x=0,y=16)
    can2 = Canvas(root2,width = 140, height=0.01, bg='#f1f3f5')
    can2.place(x=3,y=40)
    can4 = Canvas(root2,width = 500, height=0.01, bg='black',bd=1)
    can4.place(x=0,y=90)
    can5 = Canvas(root2,width = 350, height=0.01, bg='#f1f3f5')
    can5.place(x=3,y=140)
    can6 = Canvas(root2,width = 500, height=0.01, bg='black',bd=1)
    can6.place(x=0,y=190)
    can7 = Canvas(root2,width = 500, height=0.01, bg='black',bd=1)
    can7.place(x=0,y=365)
    
#그래프 출력 입력화면
def btn3():
    global root3
    root3 = Toplevel(root)
    root3.title("그래프 출력")
    root3.geometry("225x225")
    root3.configure(bg = 'white')
    root3.resizable(False, False)
    global year , mon, kna
    knum = Label(root3, text = "원생 번호", bg = 'white')
    knum.place(x = 0, y= 0)
    kna = Text(root3, width=20, height = 1)
    kna.place(x = 3 , y = 30)
    ye = Label(root3, text = "년(ex. 2021)", bg = 'white')
    ye.place(x = 0, y = 60)
    year = Text(root3, width=20, height = 1)
    year.place(x= 3, y = 90)
    mo = Label(root3, text = "월(ex. 5)", bg = 'white')
    mo.place(x = 0 , y = 120)
    mon = Text(root3, width=20, height = 1)
    mon.place(x =3 , y = 150)
    btn = Button(root3, text = "검색" , command = btn4, width = 8, height = 2)
    btn.place(x = 150, y = 175)

    #줄
    can = Canvas(root3,width = 60, height=0.01, bg='black',bd=1)
    can.place(x=0,y=20)
    can2 = Canvas(root3,width = 60, height=0.01, bg='black',bd=1)
    can2.place(x=0,y=80)
    can3 = Canvas(root3,width = 60, height=0.01, bg='black',bd=1)
    can3.place(x=0,y=140)
    can4 = Canvas(root3,width = 140, height=0.01, bg='#f1f3f5')
    can4.place(x=3,y=47)
    can5 = Canvas(root3,width = 140, height=0.01, bg='#f1f3f5')
    can5.place(x=3,y=107)
    can6 = Canvas(root3,width = 140, height=0.01, bg='#f1f3f5')
    can6.place(x=3,y=167)
    
#월에 따른 값 얻어오기
def month(kin , ye2 ,mon):
    knum2 = kna.get("1.0","end")
    knum2 = knum2[:-1]
    #데이터베이스 접속
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    #테이블 이름 탐색
    cursor.execute("select num, name from kid")
    row = cursor.fetchall()
    for i in range(len(row)):
        if int(knum2) == row[i][0]:
            tablename = row[i][1] + str(row[i][0])
            
    cursor.execute("select kinds, date from "+ tablename)
    row = cursor.fetchall()
    kin = kin
    ins = [0,0,0,0,0]
    i = 0
    for i in range(len(row)):
        date = row[i][1]
        date_time = datetime.strptime(date, '%Y-%m-%d').date()
        dateyy = date_time.year
        if dateyy == ye2:
            #년월일중 월만 
            date = row[i][1]
            date_time = datetime.strptime(date, '%Y-%m-%d').date()
            datedd = date_time.month
            for j in range(len(kin)):
                if row[i][0] == kin[j]:
                    if datedd == mon:
                        ins[j] = ins[j] +1
    
    return ins

#그래프 출력
def btn4():
    kname2 = kna.get("1.0","end")
    kname2 = kname2[:-1]
    ye2 = year.get("1.0","end") 
    mon2 = mon.get("1.0","end")
    root4 = Toplevel(root3)
    root4.title(mon2 + "월 Grape")
    root4.resizable(False, False)
    #btn3 텍스트박스에서 입력값 확인
    kin = ["신체건강", "의사소통", "사회관계","예술경험","자연탐구"]
    #월 출력함수 호출
    ins = month(kin,int(ye2), int(mon2))
    industry = kin
    fluctuations = ins
    #차트 사이즈
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(1,1,1)
    #y축 개수, 카테고리에 따라 숫자 변동
    ypos = np.arange(5)
    #그래프 색
    color = ['blue', 'skyblue' , '#A2E9FF'] 
    rects = plt.barh(ypos, fluctuations, align='center', height= 0.5, color = color)
    plt.yticks(ypos, industry)
    plt.xlim([0,10])
    
    #테이블 탐색
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("select num, name from kid")
    row = cursor.fetchall()
    for i in range(len(row)):
        if int(kname2) == row[i][0]:
            kk = row[i][1]
    plt.xlabel(kname2+"번 "+ kk +"의 각 영역별 교육횟수")
    canvas = FigureCanvasTkAgg(fig, master=root4)
    canvas.draw()
    canvas.get_tk_widget().pack()


#일별 일지 출력
def btn6():
    root6 = Toplevel(root)
    root6.title("일지출력")
    root6.geometry("225x225")
    root6.configure(bg = 'white')
    root6.resizable(False, False)
    label = Label(root6, text = "원생 번호" , bg = 'white')
    label.place(x = 0, y = 0)
    global gnu
    gnu = Text(root6, width=20, height = 1)
    gnu.place(x = 3, y = 30)
        
    ye = Label(root6, text = "날짜(ex.2021-XX-XX) ", bg = 'white')
    ye.place(x = 0 , y = 70 )

    global txt10
    txt10 = Text(root6, width=20, height = 1)
    txt10.place(x = 3, y = 100)
    btn7 = Button(root6, text = "검색" , command = dayreport, width = 8, height = 2)
    btn7.place(x = 100, y = 150)

    can = Canvas(root6,width = 120, height=0.01, bg='black',bd=1)
    can.place(x=0,y=20)
    can2 = Canvas(root6,width = 120, height=0.01, bg='black',bd=1)
    can2.place(x=0,y=90)
    can3 = Canvas(root6,width = 140, height=0.01, bg='#f1f3f5')
    can3.place(x=0,y=50)
    can4 = Canvas(root6,width = 140, height=0.01, bg='#f1f3f5')
    can4.place(x=0,y=117)
    
    
def dayreport():
     
    dae = txt10.get("1.0","end")
    da = dae[:-1]
    k = gnu.get("1.0","end")
    k = k[:-1]
    
    #테이블 이름 탐색
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("select num, name from kid")
    row = cursor.fetchall()
    global tn
    for i in range(len(row)):
        if int(k) == row[i][0]:
            tn = row[i][1] + str(row[i][0])
            gname = row[i][1]
    cursor.execute("select title, kinds, date from "+ tn)
    row = cursor.fetchall()
    tit = []
    kind = []
    date = []
    global tv1
    tv1 = tv2 = tv3 = tv4 = tv5 = tv6 = tv7 = tv8 = tv9 = tv10 = tv11 = tv12 =  tv13 = tv14 = tv15 = "-"
    for i in range(len(row)):
        dat = row[i][2]
        if dat == da:
            tit.append(row[i][0])
            kind.append(row[i][1])
            date.append(row[i][2])
            
    cnt = 0
    for i in range(len(tit)):
        if cnt == 0 and kind[i] == "신체건강":
            tv1 = tit[i]
            cnt = cnt+1
        elif cnt == 1 and kind[i] == "신체건강":
            tv2 = tit[i]
            cnt = cnt+1
        elif cnt == 2 and kind[i] == "신체건강":
            tv3 = tit[i]

    cnt = 0

    for i in range(len(tit)):
        if cnt == 0 and kind[i] == "의사소통":
            tv4 = tit[i]
            cnt = cnt+1
        elif cnt == 1 and kind[i] == "의사소통":
            tv5 = tit[i]
            cnt = cnt+1
        elif cnt == 2 and kind[i] == "의사소통":
            tv6 = tit[i]

    cnt = 0
            
    for i in range(len(tit)):
        if cnt == 0 and kind[i] == "사회관계":
            tv7 = tit[i]
            cnt = cnt+1
        elif cnt == 1 and kind[i] == "사회관계":
            tv8 = tit[i]
            cnt = cnt+1
        elif cnt == 2 and kind[i] == "사회관계":
            tv9 = tit[i]

    cnt = 0
            
    for i in range(len(tit)):
        if cnt == 0 and kind[i] == "예술경험":
            tv10 = tit[i]
            cnt = cnt+1
        elif cnt == 1 and kind[i] == "예술경험":
            tv11 = tit[i]
            cnt = cnt+1
        elif cnt == 2 and kind[i] == "예술경험":
            tv12 = tit[i]

    cnt = 0
            
    for i in range(len(tit)):
        if cnt == 0 and kind[i] == "자연탐구":
            tv13 = tit[i]
            cnt = cnt+1
        elif cnt == 1 and kind[i] == "자연탐구":
            tv14 = tit[i]
            cnt = cnt+1
        elif cnt == 2 and kind[i] == "자연탐구":
            tv15 = tit[i]

    cnt = 0
    
    root5 = Toplevel(root)
    root5.title("일지")
    root5.configure(bg='white')
    root5.geometry("600x561")
    root5.resizable(False, False)
    tit = Label(root5, text = "유아 관찰 일지", bg = 'white',font=("sans-serif","20"), width = 100)
    tit.pack()
    kn = Label(root5, text = "이름 : "+gname, bg ='white')
    kn.place(x = 390, y = 35)
    da2 = Label(root5, text = "날짜 : "+da, bg ='white')
    da2.place(x = 480, y = 35)


    #각영역 제목
    cla = Label(root5, text = "신체건강", bg = 'white')
    cla.place(x= 30, y = 100)
    cla2 = Label(root5, text = "의사소통", bg = 'white')
    cla2.place(x= 30, y = 200)
    cla3 = Label(root5, text = "사회관계", bg = 'white')
    cla3.place(x= 30, y = 300)
    cla4 = Label(root5, text = "예술경험", bg = 'white')
    cla4.place(x= 30, y = 400)
    cla5 = Label(root5, text = "자연탐구", bg = 'white')
    cla5.place(x= 30, y = 500)

    #신체건강영역 문장
    tx1 = StringVar()
    tx1.set(tv1)
    vari1 = Label(root5,textvariable = tx1, bg = 'white', height = 2)
    vari1.place(x=120, y = 70)
    tx2 = StringVar()
    tx2.set(tv2)
    vari2 = Label(root5,textvariable = tx2, bg = 'white', height = 2)
    vari2.place(x=120, y = 100)
    tx3 = StringVar()
    tx3.set(tv3)
    vari3 = Label(root5,textvariable = tx3, bg = 'white', height = 2)
    vari3.place(x=120, y = 130)

    #의사소통영역 문장
    tx4 = StringVar()
    tx4.set(tv4)
    vari4 = Label(root5,textvariable = tx4, bg = 'white')
    vari4.place(x=120, y = 170)
    tx5 = StringVar()
    tx5.set(tv5)
    vari5 = Label(root5,textvariable = tx5, bg = 'white')
    vari5.place(x=120, y = 200)
    tx6 = StringVar()
    tx6.set(tv6)
    vari6 = Label(root5,textvariable = tx6, bg = 'white')
    vari6.place(x=120, y = 230)

    #사회관계영역 문장
    tx7 = StringVar()
    tx7.set(tv7)
    vari7 = Label(root5,textvariable = tx7, bg = 'white')
    vari7.place(x=120, y = 270)
    tx8 = StringVar()
    tx8.set(tv8)
    vari8 = Label(root5,textvariable = tx8, bg = 'white')
    vari8.place(x=120, y = 300)
    tx9 = StringVar()
    tx9.set(tv9)
    vari9 = Label(root5,textvariable = tx9, bg = 'white')
    vari9.place(x=120, y = 330)

    #예술경험영역 문장
    tx10 = StringVar()
    tx10.set(tv10)
    vari10 = Label(root5,textvariable = tx10, bg = 'white')
    vari10.place(x=120, y = 370)
    tx11 = StringVar()
    tx11.set(tv11)
    vari11 = Label(root5,textvariable = tx11, bg = 'white')
    vari11.place(x=120, y = 400)
    tx12 = StringVar()
    tx12.set(tv12)
    vari12 = Label(root5,textvariable = tx12, bg = 'white')
    vari12.place(x=120, y = 430)

    #자연탐구영역 문장
    tx13 = StringVar()
    tx13.set(tv13)
    vari13 = Label(root5,textvariable = tx13, bg = 'white')
    vari13.place(x=120, y = 470)
    tx14 = StringVar()
    tx14.set(tv14)
    vari14 = Label(root5,textvariable = tx14, bg = 'white')
    vari14.place(x=120, y = 500)
    tx15 = StringVar()
    tx15.set(tv15)
    vari15 = Label(root5,textvariable = tx15, bg = 'white')
    vari15.place(x=120, y = 530)

    #칸 나누기
    can = Canvas(root5,width = 600, height=0.01, bg='black',bd=1)
    can.place(x=0,y=55)
    can2 = Canvas(root5,width = 600, height=0.1, bg='black',bd=1)
    can2.place(x=0,y=155)
    can3 = Canvas(root5,width = 600, height=0.1, bg='black',bd=1)
    can3.place(x=0,y=255)
    can4 = Canvas(root5,width = 600, height=0.1, bg='black',bd=1)
    can4.place(x=0,y=355)
    can5 = Canvas(root5,width = 600, height=0.1, bg='black',bd=1)
    can5.place(x=0,y=455)
    can5 = Canvas(root5,width = 600, height=0.1, bg='black',bd=1)
    can5.place(x=0,y=555)
    can5 = Canvas(root5,width = 600, height=0.1, bg='black',bd=1)
    can5.place(x=0,y=555)
    can6 = Canvas(root5,width = 0.1, height=550, bg='black', bd=1)
    can6.place(x=100,y=55)

    #삭제 버튼
    remo1 = Button(root5, text = "삭제" , command =lambda : remo(tv1,da), width = 3, height = 1, repeatdelay = 1000)
    remo1.place(x = 550, y = 65)
    remo2 = Button(root5, text = "삭제" , command =lambda : remo(tv2,da), width = 3, height = 1, repeatdelay = 1000)
    remo2.place(x = 550, y = 95)
    remo3 = Button(root5, text = "삭제" , command =lambda : remo(tv3,da), width = 3, height = 1, repeatdelay = 1000)
    remo3.place(x = 550, y = 125)
    remo4 = Button(root5, text = "삭제" , command =lambda : remo(tv4,da), width = 3, height = 1, repeatdelay = 1000)
    remo4.place(x = 550, y = 165)
    remo5 = Button(root5, text = "삭제" , command =lambda : remo(tv5,da), width = 3, height = 1, repeatdelay = 1000)
    remo5.place(x = 550, y = 195)
    remo6 = Button(root5, text = "삭제" , command =lambda : remo(tv6,da), width = 3, height = 1, repeatdelay = 1000)
    remo6.place(x = 550, y = 225)
    remo7 = Button(root5, text = "삭제" , command =lambda : remo(tv7,da), width = 3, height = 1, repeatdelay = 1000)
    remo7.place(x = 550, y = 265)
    remo8 = Button(root5, text = "삭제" , command =lambda : remo(tv8,da), width = 3, height = 1, repeatdelay = 1000)
    remo8.place(x = 550, y = 295)
    remo9 = Button(root5, text = "삭제" , command =lambda : remo(tv9,da), width = 3, height = 1, repeatdelay = 1000)
    remo9.place(x = 550, y = 325)
    remo10 = Button(root5, text = "삭제" , command =lambda : remo(tv10,da), width = 3, height = 1, repeatdelay = 1000)
    remo10.place(x = 550, y = 365)
    remo11 = Button(root5, text = "삭제" , command =lambda : remo(tv11,da), width = 3, height = 1, repeatdelay = 1000)
    remo11.place(x = 550, y = 395)
    remo12 = Button(root5, text = "삭제" , command =lambda : remo(tv12,da), width = 3, height = 1, repeatdelay = 1000)
    remo12.place(x = 550, y = 425)
    remo13 = Button(root5, text = "삭제" , command =lambda : remo(tv13,da), width = 3, height = 1, repeatdelay = 1000)
    remo13.place(x = 550, y = 465)
    remo14 = Button(root5, text = "삭제" , command =lambda : remo(tv14,da), width = 3, height = 1, repeatdelay = 1000)
    remo14.place(x = 550, y = 495)
    remo15 = Button(root5, text = "삭제" , command =lambda : remo(tv15,da), width = 3, height = 1, repeatdelay = 1000)
    remo15.place(x = 550, y = 525)

def remo(tv,da):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("select title, date from "+ tn)
    row = cursor.fetchall()
    for i in range(len(row)):
        if da == row[i][1]:
            if tv == row[i][0]:
                cursor.execute("Delete from "+tn+" WHERE title = '%s'" %tv)
                conn.commit()
                remov = Toplevel(root)
                remov.title("삭제")
                remov.configure(bg='white')
                remov.geometry("200x50")
                remov.resizable(False, False)
                label = Label(remov, text ="문장이 삭제되었습니다." , bg = 'white')
                label.pack()
                label2 = Label(remov, text ="일지를 다시 불러와 주세요." , bg = 'white')
                label2.pack()

#원생 관리 창
def kid():
    root7 = Toplevel(root)
    root7.title("원생 관리")
    root7.configure(bg='white')
    root7.geometry("620x280")
    root7.resizable(False, False)
    
    # 원생 등록 라벨
    label = Label(root7, text ="원생 등록" , bg = 'white')
    label.place(x = 0, y = 0)
    label2 = Label(root7, text ="이름" , bg = 'white')
    label2.place(x = 0, y = 30)
    label3 = Label(root7, text ="반" , bg = 'white')
    label3.place(x = 0, y = 75)
    label4 = Label(root7, text ="생일(ex.201X-XX-XX)" , bg = 'white')
    label4.place(x = 0, y = 120)
    label5 = Label(root7, text ="실행결과" , bg = 'white')
    label5.place(x = 0, y = 190)

    global lab1
    lab1 = StringVar()
    lab1.set("~~~는 ~번으로 저장되었습니다.")
    lav2 = Label(root7,textvariable = lab1, bg = 'white')
    lav2.place(x=0, y = 220)
    
    #텍스트 박스
    global txe1, txe2, txe3
    txe1 = Text(root7, width=20, height = 1)
    txe1.place(x= 3, y = 55)
    txe2 = Text(root7, width=20, height = 1)
    txe2.place(x= 3, y = 100)
    txe3 = Text(root7, width=20, height = 1)
    txe3.place(x= 3, y = 145)

    #버튼
    btn = Button(root7, text = "등록", command = inkid, width = 5, height = 2)
    btn.place(x = 120, y = 170)

    #원생 조회
    label6 = Label(root7, text ="원생 조회" , bg = 'white')
    label6.place(x = 200, y = 0)
    label7 = Label(root7, text ="원생 번호" , bg = 'white')
    label7.place(x = 200, y = 30)

    #텍스트박스
    global txe4
    txe4 = Text(root7, width=20, height = 1)
    txe4.place(x= 203, y = 55)
    
    #버튼
    btn2 = Button(root7, text = "조회", command = sekid, width = 5, height = 2)
    btn2.place(x = 320, y = 170)
    
    #원생 삭제
    label8 = Label(root7, text ="원생 삭제" , bg = 'white')
    label8.place(x = 400, y = 0)
    label9 = Label(root7, text ="원생 번호" , bg = 'white')
    label9.place(x = 400, y = 30)
    label10 = Label(root7, text ="실행 결과" , bg = 'white')
    label10.place(x = 400, y = 190)
    
    #텍스트박스
    global txe5
    txe5 = Text(root7, width=20, height = 1)
    txe5.place(x= 403, y = 55)
    
    global lab3
    lab3 = StringVar()
    lab3.set("~번 ~~~의 정보가 삭제되었습니다.")
    lav3 = Label(root7,textvariable = lab3, bg = 'white')
    lav3.place(x=400, y = 220)
    
    #버튼
    btn3 = Button(root7, text = "삭제", command = remkid, width = 5, height = 2)
    btn3.place(x = 520, y = 170)
    
    #칸나누기
    can = Canvas(root7 ,width = 700,height=0.01, bg='black',bd=1)
    can.place(x=0,y=20)
    can2 = Canvas(root7 ,width = 0.01, height=300, bg='black',bd=1)
    can2.place(x=190,y=0)
    can3 = Canvas(root7 ,width = 0.01, height=300, bg='black',bd=1)
    can3.place(x=390,y=0)
    
def inkid():
    knn = txe1.get("1.0", "end")
    knn = knn[:-1]
    cla = txe2.get("1.0", "end")
    cla = cla[:-1]
    bir = txe3.get("1.0", "end")
    bir = bir[:-1]
    conn = mysql.connector.connect(**config)
    # db select, insert, update, delete 작업 객체
    cursor = conn.cursor()
    cursor.execute("select num from kid")
    row = cursor.fetchall()
    num1 = row[len(row)-1][0] +1
    sql ="insert into kid(num, name, class, birth) values(%s, %s, %s, %s)"
    val = (num1, knn, cla , bir)
    cursor.execute(sql,val)
    tablename = knn+str(num1)
    sql = "CREATE table " + tablename + "(title VARCHAR(500), kinds varchar(200) not null, date varchar(200) not null)"
    cursor.execute(sql)
    conn.commit()
    lab1.set(knn + "는 " +str(num1) + "번으로 저장되었습니다")

def sekid():
    root8 = Toplevel(root)
    root8.title("원생 조회")
    root8.configure(bg='white')
    root8.geometry("230x200")
    root8.resizable(False, False)
    kna = ""
    kclass = ""
    kbirth  = ""
    #원생 번호 입력
    knu = txe4.get("1.0", "end")
    knu = knu[:-1]
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("select num, name, class, birth from kid")
    row = cursor.fetchall()
    i = 0
    for i in range(len(row)):
        if int(knu) == row[i][0]:
            kna = row[i][1]
            kclass = row[i][2]
            kbirth = row[i][3]
            
    #원생 정보 라벨
    label = Label(root8, text ="원생 정보" , bg = 'white', font = (10))
    label.place(x = 0, y = 0)
    label2 = Label(root8, text ="이름" , bg = 'white')
    label2.place(x = 0, y = 30)
    label3 = Label(root8, text ="번호" , bg = 'white')
    label3.place(x = 0, y = 75)
    label4 = Label(root8, text ="반" , bg = 'white')
    label4.place(x = 0, y = 120)
    label5 = Label(root8, text ="생일" , bg = 'white')
    label5.place(x = 0, y = 165)
    
    #원생 정보 변화라벨
    lab1 = StringVar()
    lab1.set(kna)
    labe1 = Label(root8,textvariable = lab1, bg = 'white')
    labe1.place(x = 50, y = 30)
    lab2 = StringVar()
    lab2.set(knu)
    labe2 = Label(root8,textvariable = lab2, bg = 'white')
    labe2.place(x = 50, y = 75)
    lab3 = StringVar()
    lab3.set(kclass)
    labe3 = Label(root8,textvariable = lab3, bg = 'white')
    labe3.place(x = 50, y = 120)
    lab4 = StringVar()
    lab4.set(kbirth)
    labe4 = Label(root8,textvariable = lab4, bg = 'white')
    labe4.place(x = 50, y = 165)

    can = Canvas(root8 ,width = 300,height=0.01, bg='black',bd=1)
    can.place(x=0,y=20)
    can2 = Canvas(root8 ,width = 0.01, height=300, bg='black',bd=1)
    can2.place(x=40,y=20)
    can3 = Canvas(root8 ,width = 300,height=0.01, bg='black',bd=1)
    can3.place(x=0,y=57)
    can4 = Canvas(root8 ,width = 300,height=0.01, bg='black',bd=1)
    can4.place(x=0,y=102)
    can5 = Canvas(root8 ,width = 300,height=0.01, bg='black',bd=1)
    can5.place(x=0,y=147)
    
def remkid():
    knum = txe5.get("1.0","end")
    knum = knum[:-1]
    print(knum)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("select num, name from kid")
    row = cursor.fetchall()
    print(row)
    for i in range(len(row)):
        if int(knum) == row[i][0]:
            knam = row[i][1]
            tablename = row[i][1] + str(row[i][0])
            cursor.execute("Delete from kid WHERE num = '%s'" %knum)
            cursor.execute("DROP TABLE " + tablename)
            conn.commit()
            lab3.set(knum +"번 " + knam +"의 정보가 삭제 되었습니다")
            
def main():
   #메인화면
    global root
    root = Tk()
    root.title("일지 작성 프로그램")
    root.geometry("300x470")
    root.configure(bg= 'white')
    root.resizable(width=False, height = False)
    
    labe = Label(root,text = "일지작성 프로그램" , bg = 'white', font = ('bold', 15))
    labe.place(x = 67, y = 255)
    can = Canvas(root, width = 180, height=0.01, bg='black', bd=1)
    can.place(x=60,y=280)
    #메인 그림
    imgObj = PhotoImage(file = "ddd2.png")
    imgLabel = Label(root)
    imgLabel.config(image=imgObj)
    imgLabel.pack()

    #버튼
    btn = Button(root, text = "일지 작성", command = bnt2, width = 15, height= 3, bg = "white")
    btn2 = Button(root, text = "월별 그래프", command = btn3, width = 15, height = 3, bg =  "white")
    btn5 = Button(root, text = "일지 출력", command = btn6, width = 15, height = 3, bg =  "white")
    btn7 = Button(root, text = "원생 관리", command = kid, width = 15, height= 3, bg =  "white")
    btn.place(x = 160, y = 300)
    btn2.place(x = 160, y = 380)
    btn5.place(x = 30, y = 380)
    btn7.place(x = 30, y = 300)
    
    root.mainloop()

def Convert2Vec(model_name, sentence):
    word_vec = []
    sub = []
    model = gensim.models.word2vec.Word2Vec.load(model_name)
    for word in sentence:
        if (word in model.wv.vocab):
            sub.append(model.wv[word])
        else:
            sub.append(np.random.uniform(-0.25, 0.25, 300))  # used for OOV words
    word_vec.append(sub)
    return word_vec

def Grade(sentence):
    full = []
    cname = []
    pnuml = []
    
    tokens = W2V.tokenize(sentence)
    embedding = Convert2Vec('post.embedding', tokens)
    zero_pad = W2V.Zero_padding(embedding, Batch_size, Maxseq_length, Vector_size)
    global sess
    result = sess.run(prediction, feed_dict={X: zero_pad, seq_len: [len(tokens)]}) # tf.argmax(prediction, 1)이 여러 prediction 값중 max 값 1개만 가져옴
    point = result.ravel().tolist()
    ## ** 카테고리에 맞게 수정 ** ##
    Tag = ['body', 'comm', 'social', 'art', 'science']
    tag_name = {'body': '신체건강', 'comm':'의사소통', 'social':'사회관계', 'art':'예술경험', 'science':'자연탐구'}
    for t, i in zip(Tag, point):
        """if len(t) <= 6:
            print(t, '\t\t', round(i * 100, 2), "%")
        else:
            print(t, '\t', round(i * 100, 2), "%")"""
        pNum = round(i * 100, 2)
        percent = tag_name[t] + ' : ' + str(round(i * 100, 2)) + "%"
        
        
        cname.append(tag_name[t])
        pnuml.append(pNum)
        
        full.append(percent)
    maxnum = max(pnuml)
    cindex = 0
    cindex = pnuml.index(maxnum)
        
    
    return full, cname[cindex]
        
W2V = Word2Vec.Word2Vec()

Batch_size = 1
Vector_size = 300
Maxseq_length = 500  # Max length of training data
learning_rate = 0.001
lstm_units = 128
## ** 카테고리에 개수 ** ##
num_class = 5
keep_prob = 1.0

X = tf.compat.v1.placeholder(tf.float32, shape = [None, Maxseq_length, Vector_size], name = 'X')
Y = tf.compat.v1.placeholder(tf.float32, shape = [None, num_class], name = 'Y')
seq_len = tf.compat.v1.placeholder(tf.int32, shape = [None])

BiLSTM = Bi_LSTM.Bi_LSTM(lstm_units, num_class, keep_prob)

with tf.compat.v1.variable_scope("loss", reuse = tf.compat.v1.AUTO_REUSE):
    logits = BiLSTM.logits(X, BiLSTM.W, BiLSTM.b, seq_len)
    loss, optimizer = BiLSTM.model_build(logits, Y, learning_rate)

prediction = tf.nn.softmax(logits)  # softmax

saver = tf.compat.v1.train.Saver()
init = tf.compat.v1.global_variables_initializer()
## 학습시킨 모델의 이름 ##
modelName = "Bi_LSTM.model"

sess = tf.Session()
sess.run(init)
## 모델을 불러옴 ##
saver.restore(sess, modelName)
main()
