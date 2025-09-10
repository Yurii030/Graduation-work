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

  <li>
    <a class="bgimg">
      <img src="./img/www.png" alt="bgimg">
       </a>
      </li>
      

    </div>
    <div class="box">
      <div class="container-1">
          <span class="icon"><i class="fa fa-search"></i></span>
          <input type="search" id="search" placeholder="Search...">
      </div>
    <div class="img">
      <img src="./img/11.png" alt="kid_search" id="kid_src">
     </div>
     <div class="img3">
      <img src="./img/3.png" alt="kid_search" id="kid2_src">
     </div>
     <div class="text-on-img">
      <div class="background-wrap">
        <div class="content">
          <SPAN onclick="location.href='./kind_inq.html'"> 원생 관리 </SPAN>
         </div>
      </div>
    </div>
      <div class="img2">
      <img src="./img/22.png" alt="diary" id="dry"/>
     </div>
     <div class="img4">
       <img src="./img/4.png" alt="diary" id="dry2">
     </div>
     <div class="text-on-img2">
      <div class="background-wrap2">
        <div class="content2">
          <SPAN onclick="location.href='./diary_read.html'"> 일지 조회 </SPAN>
        </div>
      </div>
    </div>
  </li>
</body>
</html>