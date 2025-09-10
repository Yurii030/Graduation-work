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
  <link href="https://fonts.googleapis.com/css?family=Roboto:300" rel="stylesheet">
  <link rel="icon" href="./img/icon.png"/>
  <link rel="stylesheet" href="./css/main.css"/>
  <script defer src="./js/main.js"></script>
  <script defer src="./js/login.js"></script>
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
  <?php if(!isset($_SESSION['id']) || !isset($_SESSION['name'])) { ?>
    <div class="login-page">
              <div class="form">
                <div class="text">
                  <h3>로그인</h3>
                 </div>
                <form action="./php/logindb.php" method="POST" class="register-form">
                  <input type="text" placeholder="name"/>
                  <input type="password" placeholder="password"/>
                  <input type="text" placeholder="email address"/>
                  <button>create</button>
                  <p class="message">이미 회원이신가요? <a href="#">로그인</a></p>
                </form>
                <form action="./php/logindb.php" method="POST" class="login-form">
                  <input name="id" type="text" placeholder="아이디"/>
                  <input name="pw" type="password" placeholder="비밀번호"/>
                  <button>로그인</button>
                  <p class="message">아직 회원이 아니신가요? <a href="./sign_up.php"> 회원가입 </a></p>
                </form>
              </div>
            </div>
        <?php } else {
            $user_id = $_SESSION['id'];
            $user_name = $_SESSION['name'];
            echo "<p>$user_name($user_id)님은 이미 로그인되어 있습니다.";
            echo "<p><button onclick=\"window.location.href='logout.php'\">로그아웃</button></p>";
        } ?>
        
        <?php echo urldecode($row);?>
  </main>
</body>
</html>