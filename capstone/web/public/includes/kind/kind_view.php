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
  
  <table>
  <?php
    $num = $_GET['num'];

		$sql = "SELECT * FROM child WHERE child_num = '$num'";
		$result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_assoc($result);
	?>
    <!--<tr>
      <td>이름: </td>
      <td><?php echo $row['child_name'];?></td>
    </tr>
    <tr>
      <td>원생 번호: </td>
      <td><?php echo $row['child_uid'];?></td>
    </tr>
    <tr>
      <td>나이: </td>
      <td><?php echo $row['child_age'];?></td>
    </tr>
    <tr>
      <td>생일: </td>
      <td><?php echo $row['child_birth'];?></td>
    </tr>
    <tr>
      <td>반: </td>
      <td><?php echo $row['child_class_id'];?></td>
    </tr>
    
    <tr>
      <td>
        <a href="/capstone/kind_update.php?num=<?php echo $row['child_num']?>">수정</a>
      </td>
    </tr>
    <tr>
      <td>
        <form action="./kind_delete.php" method="post">
          <button type="submit" onclick="child_del_check()" class="kind_delete_btn">삭제</button>
        <form>
      </td>
    </tr>
  </table>-->

  <style>

  .view_h1 {
      position: relative;
      left: 80px;
      top: 110px;
    }
    .kind_v{
    width:90%;
    height: 340%;
    border-top:2px solid 
    #bdbdbd;border-bottom:2px solid 
    #bdbdbd;font-family:"NanumGothic",sans-serif;
    position: relative;
    left: 70px;
    top: 140px;
    }
    .kind_v .qtit{
    text-align:left; 
    margin:50px 0 10px 0;
    }
    .kind_v tr{
    border-top:1px solid 
    #cdcdcd;
    }
    .kind_v tr:first-child{
    border-top:0;
    }
    .kind_v th{
    background:#f6f6f6; 
    width:20%;
    text-align:left; 
    padding-left:3%
    }
    .kind_v td{
    text-align:left;
    background:#fff;
    padding-top:1%!important;padding-bottom:1%!important;
    color:#5c5c5c;
    font-size:15px;
    line-height:20px;
    padding-left:3%;
    }
    .kind_v input[type="text"],
    .kind_v select{
    margin-right:1%;
    color:#5c5c5c;
    line-height:12px;
    font-size:14px;
    font-family:"NanumGothic",sans-serif;background:#f6f6f6;vertical-align:middle;
    border:1px solid #cdcdcd;padding:1%;
    }
    .kind_v select{
    padding:0.9%;
    }

    .kind_v .button{
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
    .kind_v .button a{
    color:#fff;
    }
    .kind_v .add{
    margin-top:1%;
    }
    .kind_v .wid10{
    width:10%;
    }
    .kind_v .name{
    width:20%;
    }
    .kind_v .wid30{
    width:30%;
    }
    .kind_v .wid53{
    width:40%;
    }

    .viewbtn{
    position: absolute;
    bottom: 100px;
    right: 300px;
    width:80%;
    }

    .viewbtn a{
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

    .viewbtn a:hover{
    background:#fff;
    color:#55BE9D;
    }


    .viewbtn_not{
    position: absolute;
    bottom: 100px;
    right: 100px;
    width:80%;
    }

    .viewbtn_not a{
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

    .viewbtn_not a:hover{
    background:#fff;
    color:#55BE9D;
    }
     </style>

  <main>
    <table class="kind_v">
        <div class="view_h1">
        <h1>원생 수정</h1>
      </div>
          <caption class="qtit">
            <form action="./php/kind_insertdb.php" method="post">
              <tr>
                  <th class="th" scope="row" >
                    <p>이름</p>
                  <td>
               <?php echo $row['child_name'];?>
                  </td>
              </tr>
              <tr>
                  <th class="th" >
                  <p>원생번호</p>
                  <td><?php echo $row['child_uid'];?></td></td>
              </tr>
              <tr>
                  <th class="th" scope="row">
                    <p>나이</p>
                  <td>
                    <?php echo $row['child_age'];?></td>
              </tr>
              <tr>
                  <th class="th" scope="row">
                    <p>생일</p>
                  <td>
                    <?php echo $row['child_birth'];?></td>
              </tr>
              <tr>
                  <th class="th" scope="row">
                    <p>반</p>
                    <td><?php echo $row['child_class_id'];?></td>
              </tr>

        </table>
                 
        <div class="viewbtn">
          <a href="/capstone/kind_update.php?num=<?php echo $row['child_num']?>" class="kind_insert">수정</a>
        </div>

        <div class="viewbtn_not">
          <a href="/capstone/php/kind_delete.php?num=<?php echo $row['child_num']?>" class="kind_insert_not">삭제</a>
        </div>

    </form>
  </main>
</body>
</html>