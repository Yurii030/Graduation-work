<!DOCTYPE html>
<?php 
include './php/session.php'; 
include './php/db.php';?>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>3멍 1냥 캡스톤 디자인</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jua&display=swap" rel="stylesheet">
  <link rel="icon" href="./img/icon.png"/>
  <link rel="stylesheet" href="./css/main.css"/>
  <script defer src="./js/main.js"></script>
  <style>
      /* Form */

    .text_h1 {
      position: relative;
      left: 80px;
      top: 110px;
    }
    .question{
    width:90%;
    height: 340%;
    border-top:2px solid 
    #bdbdbd;border-bottom:2px solid 
    #bdbdbd;font-family:"NanumGothic",sans-serif;
    position: relative;
    left: 70px;
    top: 140px;
    }
    .question .qtit{
    text-align:left; 
    margin:50px 0 10px 0;
    }
    .question tr{
    border-top:1px solid 
    #cdcdcd;
    }
    .question tr:first-child{
    border-top:0;
    }
    .question th{
    background:#f6f6f6; 
    width:20%;
    text-align:left; 
    padding-left:3%
    }
    .question td{
    text-align:left;
    background:#fff;
    padding-top:1%!important;padding-bottom:1%!important;
    color:#5c5c5c;
    font-size:15px;
    line-height:20px;
    padding-left:3%;
    }
    .question input[type="text"],
    .question select{
    margin-right:1%;
    color:#5c5c5c;
    line-height:12px;
    font-size:14px;
    font-family:"NanumGothic",sans-serif;background:#f6f6f6;vertical-align:middle;
    border:1px solid #cdcdcd;padding:1%;
    }
    .question select{
    padding:0.9%;
    }

    .question .button{
    margin-right:1%;
    line-height:12px;
    font-size:14px;
    font-family:"NanumGothic",sans-serif;
    background:#5e5e5e;
    vertical-align:middle;
    border:1px solid #5e5e5e;
    padding:1%;
    cursor:pointer;
    }
    .question .button a{
    color:#fff;
    }
    .question .add{
    margin-top:1%;
    }
    .question .wid10{
    width:10%;
    }
    .question .name{
    width:20%;
    }
    .question .wid30{
    width:30%;
    }
    .question .wid53{
    width:40%;
    }

    #kbtn {
  margin-right: 4px; 
}

.kindbtn button {
  border: 1px solid #55BE9D;
  background-color: #55BE9D;
  color: white;
  padding: 20px;
  font-size: x-large;
  font-weight: 900;
  border-radius:2em;
  position: absolute;
  bottom: 72px;
  right: 1000px;
  width: 8%;
}

#kindbtn button:hover {
  color: white;
  background-color: #55BE9D;
}

    .kindbtn_not{
    position: absolute;
    bottom: 100px;
    right: 100px;
    width:80%;
    }

    .kindbtn_not a{
    width:10%;
    margin:0 auto;
    display:block;
    padding:0.7em 1.5em 0.8em 1.5em;
    font-size:25px;
    color:#fff;
    border:1px solid #55BE9D;
    border-radius:2em;
    background:#55BE9D;
    text-align:center;
    letter-spacing:-0.5px; 
    font-weight:bold;
    position: relative;
    top: 25px;
    
    }

    .kindbtn_not a:hover{
    background:#fff;
    color:#55BE9D;
    }
 
</style>
</head>
<body>
<header>
    <ul class="nav">
      <div class="logo">
        <li>
        <a href="./index.php">
          <img src="./img/logo_big.png" alt="Logo">
        </a>
        </li>
      </div>
      <li>
      <a href="./kind_inq.php">원아 조회</a>
      </li>
      <li>
        <a href="./diary.php">일지 조회</a>
      </li>
      <li>
        <a href="./diary_chart.php">일지 통계</a>
      </li>
      <li>
        <a href="./act_info.php">활동 정보</a>
      </li>
      <li class="login">
        <?php
            if(!isset($_SESSION['id']) || !isset($_SESSION['name'])) {
                echo "<a href=\"./login.php\">로그인/회원가입</a>";
            } else {
                $userid = $_SESSION['id'];
                $username = $_SESSION['name'];
                echo "<a href=\"./my_info.php\">$username($userid)님 환영합니다.</a>";
                echo "<a href=\"./php/logout.php\">로그아웃</a>";
            }
          ?>
        </li>
    </ul>
  </header>

  <main>
    <table class="question">
        <div class="text_h1">
        <h1>원생 등록</h1>
      </div>
          <caption class="qtit">
            <form action="./php/kind_insertdb.php" method="post">
              <tr>
                  <th class="th" scope="row" >
                    <p>이름</p>
                  <td>
               <input type="text" title="이름" name="name" class="name" placeholder="이름을 입력하세요" />
                  </td>
              </tr>
              <tr>
                  <th class="th" >
                  <p>아이디</p>
                  <td> <input type="text" name="number" class="number" title="아이디" placeholder="예 원생 아이디: "></td></td>
              </tr>
              <tr>
                  <th class="th" scope="row">
                    <p>나이</p>
                  <td>
                    <input type="text" name="age" title="나이" placeholder="예 : 5"></td>
              </tr>
              <tr>
                  <th class="th" scope="row">
                    <p>생일</p>
                  <td>
                    <input type="text" name="birth" class="birth" title="생일" placeholder="예 : 2017.08.03"></td>
              </tr>
              <tr>
                  <th class="th" scope="row">
                    <p>반</p>
                    <td><input type="text" name="class" class="class" title="반" placeholder="예 : 5A"></td>
              </tr>

        </table>
                 
        <div class="kindbtn">
          <button onclick="window.location.href='./kind_inq.php'" class="kind_insert">등록</button>
        </div>

        <div class="kindbtn_not">
          <a href="./kind_inq.php" class="kind_insert_not">취소</a>
        </div>

    </form>
  </main>
  
</body>
</html>