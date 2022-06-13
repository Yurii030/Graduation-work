<!DOCTYPE html>
<?php 
  include './php/session.php'; 
  include './php/db.php';
?>
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


<style>

.act_text {
  position: relative;
  top: -300px;
  left: 620px;
  font-size: xx-large;
}

  .bookinfo {
  font-family: 'Jua', sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #55BE9D;  
  width: 20%;
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 25px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
  margin-top: 100px;
  text-align: center;
  margin-right: 100px;
  position: relative;
  left: 200px;
}

.toyinfo {
  font-family: 'Jua', sans-serif;
  text-transform: uppercase;
  outline: 0;
  background: #55BE9D;  
  width: 20%;
  border: 0;
  padding: 15px;
  color: #FFFFFF;
  font-size: 25px;
  -webkit-transition: all 0.3 ease;
  transition: all 0.3 ease;
  cursor: pointer;
  margin-top: 100px;
  text-align: center;
  margin-right: 100px;
  position: relative;
  left: 900px;
  top: 35px;
}

</style>

 <main>
 <form class="check">
  <p class= bookinfo>
      <a href="./act_book.php">책</a>
   </p>
  
   <p class=toyinfo>
      <a href="./act_toy.php">장난감</a>
   </p>

   <div class="act_text">
     <h3>활동 정보</h3>
   </div> 
</main>
</body>
</html>