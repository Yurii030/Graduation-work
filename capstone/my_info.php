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
                echo "<a href=\"./my_info.php\">$username($userid)님</a>";
                echo "<a href=\"./php/logout.php\">로그아웃</a>";
            }
          ?>
        </li>
    </ul>
  </header>
<?php
  $sql = "SELECT * FROM teacher WHERE t_uid = '$userid'";
  $result = mysqli_query($conn, $sql);
  $row = mysqli_fetch_assoc($result);
?>
  <!--<main>
    <form action="./php/my_infodb.php" method="post">
      <table>
        <tr>
          <td>이름: </td>
          <td><input name="name" type="text"></td>
        </tr>
        <tr>
          <td>아이디: </td>
          <td><?php $row['t_uid']?></td>
        </tr>
        <tr>
          <td>비밀번호: </td> 
          <td><input name="pw" type="password"></td>
        </tr>
        <tr>
          <td>비밀번호 확인: </td>
          <td><input name="pw_re" type="password_re"></td>
        </tr>
        <tr>
          <td>생일: </td>
          <td><?php $row['t_birth']?></td>
        </tr>
        <tr>
          <td>전화번호: </td>
          <td><input name="phone_num" type="text"></td>
        </tr>
        <tr>
          <td>이메일: </td>
          <td><input name="email" type="text"></td>
        </tr>
        <tr>
          <td><input name="update_info" type="submit" value="정보 변경"></td>
        </tr>
        <tr>
          <td>
          <a href="withdrawal.php" class="delete">회원탈퇴</a>
          </td>
        </tr>
      </table>
    </form>
  </main>--><!--$_COOKIE-->
  <main>
  <form action="./php/my_infodb.php" method="post" class = "joinForm">
                                                                                               
   <h2>내 정보</h2>
   <div class="textForm">
     <input name="name" type="text" class="name" placeholder="이름">
   </div>
   <div class="textForm">
   <?php echo $row['t_uid']?>
   </div>
   <div class="textForm">
     <input name="pw" type="password" class="pw" placeholder="비밀번호">
    </div>
    <div class="textForm">
     <input name="pw_re" type="password" class="pw" placeholder="비밀번호 확인">
    </div>
    <div class="textForm">
   <?php echo $row['t_birth']?>
   </div>
   <div class="textForm">
     <input name="phone_num" type="text" class="cellphoneNo" placeholder="전화번호">
   </div>
    <div class="textForm">
     <input name="email" type="text" class="email" placeholder="이메일">
   </div>
  

  <div class="infobtn">
    <button id = "info_b">회원정보 수정</button>
  </div>
</form>

<div class="deletebtn">
    <button onclick="window.location.href='./withdrawal.php'" id = "delete">회원탈퇴</button>
  </div>
  
  </main>
  
</body>
</html>