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
      <a href="./act_info.html">활동 정보</a>
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
  <form action="./php/signupdb.php" method="POST" class="joinForm">
                                                                                               
   <h2>회원가입</h2>
   <div class="textForm">
     <input name="name" type="text" class="name" placeholder="이름">
   </div>
   <div class="textForm">
     <input name="id" type="text" class="id" placeholder="아이디">
     </input>
   </div>
   <div class="textForm">
     <input name="pw" type="password" class="pw" placeholder="비밀번호">
    </div>
   <div class="textForm">
     <input name="phone_num" type="number" class="cellphoneNo" placeholder="전화번호">
   </div>
    <div class="textForm">
     <input name="email" type="text" class="email" placeholder="이메일">
   </div>
   <div class="signbtn">
        <button id = "sign">회원가입</button>
      </div>
  </form>
  
  </main>
</body>
</html>