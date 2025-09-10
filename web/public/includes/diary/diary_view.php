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
  
  <!--<article class="boardArticle">
  <?php
    $uid = $_GET['uid'];
    $date = $_GET['date'];
    
    $sql = "SELECT * FROM diary_sentence INNER JOIN diary_board ON diary_sentence.diary_child_uid = diary_board.board_child_uid AND diary_sentence.diary_date = diary_board.board_date WHERE diary_child_uid = '$uid' AND diary_date='$date'";
    $result = mysqli_query($conn, $sql);
    $row = mysqli_fetch_assoc($result);
  ?>
    <table>
      <tr><p>유아관찰일지</p></tr>
      
      <tr>
        <td><p>아동 ID</p></td>
        <td><?php echo $row['diary_child_uid']?></td>
        <td><p>영역</p></td>
        <td><?php echo $row['diary_area']?></td>
      </tr>
    
      <tr>
        <td><p>날짜</p></td>
        <td><?php echo $row['diary_date']?></td>
      </tr>
    
      <tr>
        <th scope="row"><label for="sentence">관찰내용</label></th>
        <td><?php echo $row['diary_sentence']?></td>
      </tr> 

      <tr>
        <th><a href="./diary_write.php?uid=<?php echo $row['board_child_uid']?>&date=<?php echo $row['board_date']?>">수정</a></th>
        <td><a href="./diary_delete.php?uid=<?php echo $row['board_child_uid']?>&date=<?php echo $row['board_date']?>">삭제</a></td>
      </tr> 
      

				
    </table>

  </article>-->

  <style>

  .dry_h1 {
      position: relative;
      left: 80px;
      top: 110px;
    }
    .diary_v{
    width:90%;
    height: 340%;
    border-top:2px solid 
    #bdbdbd;border-bottom:2px solid 
    #bdbdbd;font-family:"NanumGothic",sans-serif;
    position: relative;
    left: 70px;
    top: 140px;
    }
    .diary_v .qtit{
    text-align:left; 
    margin:50px 0 10px 0;
    }
    .diary_v tr{
    border-top:1px solid 
    #cdcdcd;
    }
    .diary_v tr:first-child{
    border-top:0;
    }
    .diary_v th{
    background:#f6f6f6; 
    width:20%;
    text-align:left; 
    padding-left:3%
    }
    .diary_v td{
    text-align:left;
    background:#fff;
    padding-top:1%!important;padding-bottom:1%!important;
    color:#5c5c5c;
    font-size:15px;
    line-height:20px;
    padding-left:3%;
    }
    .diary_v input[type="text"],
    .diary_v select{
    margin-right:1%;
    color:#5c5c5c;
    line-height:12px;
    font-size:14px;
    font-family:"NanumGothic",sans-serif;background:#f6f6f6;vertical-align:middle;
    border:1px solid #cdcdcd;padding:1%;
    }
    .diary_v select{
    padding:0.9%;
    }

    .diary_v .button{
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
    .diary_v .button a{
    color:#fff;
    }
    .diary_v .add{
    margin-top:1%;
    }
    .diary_v .wid10{
    width:10%;
    }
    .diary_v .name{
    width:20%;
    }
    .diary_v .wid30{
    width:30%;
    }
    .diary_v .wid53{
    width:40%;
    }

    .dry_v_btn{
    position: absolute;
    bottom: 200px;
    right: 300px;
    width:80%;
    }

    .dry_v_btn a{
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

    .dry_v_btn a:hover{
    background:#fff;
    color:#55BE9D;
    }


    .dry_v_btn_not{
    position: absolute;
    bottom: 200px;
    right: 100px;
    width:80%;
    }

    .dry_v_btn_not a{
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

    .dry_v_btn_not a:hover{
    background:#fff;
    color:#55BE9D;
    }
 
</style>

  <table class="diary_v">
        <div class="dry_h1">
        <h1>원생 관찰일지</h1>
      </div>
          <caption class="qtit">
            <form action="./php/kind_updatedb.php" method="post">
              <tr>
                  <th class="th" scope="row" >
                    <p>아동 ID</p>
                  <td>
               <?php echo $row['diary_child_uid']?>
                  </td>
              </tr>
              <tr>
                  <th class="th" >
                  <p>날짜</p>
                  <td><?php echo $row['diary_date']?></td>
              </tr>
              <tr>
                  <th class="th" >
                  <p>관찰내용</p>
                  <td><?php
                      echo "(".$row['diary_area'].")".$row['diary_sentence']."<br>";
                       if (mysqli_num_rows($result) > 0) {
                        while($row = mysqli_fetch_assoc($result)) {
                        echo "(".$row['diary_area'].")";
                        echo $row['diary_sentence']. "<br>";
                        }
                      }else{
                        echo "테이블에 데이터가 없습니다.";
                        }
                      
                    ?></td>
                    
                  </tr>
        </table>
        <div class="dry_v_btn">
          <a href="./diary_write.php?uid=<?php echo $row['board_child_uid']?>&date=<?php echo $row['board_date']?>" class="diary_view">수정</a>
        </div>

        <div class="dry_v_btn_not">
          <a href="./diary_delete.php?uid=<?php echo $row['board_child_uid']?>&date=<?php echo $row['board_date']?>" class="diary_view_not">삭제</a>
        </div>
</body>
</html>