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
    <div class="read_list_wrap">
      <table class="read_list">
          <p class="jb-text">게시판</p>
          <thead>
              <tr>
                  <th>책번호</th>
                  <th>제목</th>
                  <th>출판사</th>
                  <th>작가</th>
                  <th>가격</th>
                  <th>반</th>
              </tr>
          </thead>
                    
      <tbody>
			<?php
      
				$sql = 'SELECT * FROM book_info';
				$result = mysqli_query($conn, $sql);
        if(mysqli_num_rows($result) > 0) {
          while($row = mysqli_fetch_assoc($result)){

			?>

<tr>
            <td> <?php  echo $row['book_uid']?></td>
             <td><?php echo $row['book_title'];?></a></td>
            <td><?php echo $row['publisher']?></td>
            <td><?php echo $row['author']?></td>
            <td><?php echo $row['book_price']?></td>
            <td><?php echo $row['book_class']?></td>
          </tr>
          
<?php  
          }
        }
			?>
        </tbody>
 
      <tr>
      
      </tr>
	</table>  
      
</body>
</html>