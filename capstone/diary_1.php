<!DOCTYPE html>
<?php 
include './php/session.php'; 
include './php/db.php';?>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="widli=device-widli, initial-scale=1.0">
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

  <div id="mainWrapper">
    <div class="search_diary">
      <select id='selSearchOption' >
        <option value='A'>이름+번호</option>
        <option value='B'>이름</option>
        <option value='C'>번호</option>
      </select>
        <input id='txtKeyWord' />
        <input type='button' value='검색'/>
    </div>

    <div class="date_diary">
      <tr>
        <td><p>날짜</p></td>
        <td><input type="date" name="날짜"></td>
      </tr>
    </div>
  </div>

  <table>
    <?php
      if(isset($_GET['page'])) {
        $page = $_GET['page'];
      }
      else {
        $page = 1;
      }

      $allPost = $row['cnt']; //전체 게시글의 수
      $onePage = 15; // 한 페이지에 보여줄 게시글의 수.
      $allPage = ceil($allPost / $onePage); //전체 페이지의 수
      
      if($page < 1 || ($allPage && $page > $allPage)) {
    ?>

      <script>
        alert("존재하지 않는 페이지입니다.");
        history.back();
      </script>

    <?php
        exit;
      }
      $oneSection = 10; //한번에 보여줄 총 페이지 개수(1 ~ 10, 11 ~ 20 ...)
      $currentSection = ceil($page / $oneSection); //현재 섹션
      $allSection = ceil($allPage / $oneSection); //전체 섹션의 수
      $firstPage = ($currentSection * $oneSection) - ($oneSection - 1); //현재 섹션의 처음 페이지
      
      if($currentSection == $allSection) {
        $lastPage = $allPage; //현재 섹션이 마지막 섹션이라면 $allPage가 마지막 페이지가 된다
      } 
      else {
        $lastPage = $currentSection * $oneSection; //현재 섹션의 마지막 페이
      }

      $prevPage = (($currentSection - 1) * $oneSection); //이전 페이지, 11~20일 때 이전을 누르면 10 페이지로 이동
      $nextPage = (($currentSection + 1) * $oneSection) - ($oneSection - 1); //다음 페이지, 11~20일 때 다음을 누르면 21 페이지로 이동
      $paging = '<ul>'; 

      if($page != 1) {
        $paging = "<li class='page page_start'><a href='./diary.php?page=1'>◀</a></li>";
      }
      
      if($currentSection != 1) {
        $paging = "<li class='page page_prev'><a href='./diary.php?page=".$prevPage ."'>◀</a></li>";
      }

      for($i = $firstPage; $i <= $lastPage; $i++) {
        if($i == $page) {
          $paging = "<li class='page current'>'.$i.'</li>";
        } else {
          $paging = "<li class='page'><a href='./diary.php?page=".$i."'>'.$i.'</a></li>";
        }
      }   
      
      if($currentSection != $allSection) { 
        $paging = "<li class='page page_next'><a href='./diary.php?page=".$nextPage."'>▶</a></li>";
      }

      if($page != $allPage) { 
        $paging = "<li class='page page_end'><a href='./diary.php?page=".$allPage."'></a></li>";
      }

      $paging = "</ul>";    

      $currentLimit = ($onePage * $page) - $onePage; //몇 번째의 글부터 가져오는지
      $sqlLimit = 'limit'.$currentLimit.', '.$onePage; //limit sql 구문
    ?>
    
      <tr>
        <td>번호</td>
        <td>제목</td>
        <td>작성일</td>
        <td>조회</td>
      </tr>
    <?php
      $sql = "SELECT * FROM diary_sentence ORDER BY diary_date DESC"/*.sqlLiMit*/;
      $result = mysqli_query($conn, $sql);
        while($row = mysqli_fetch_assoc($result)){
          $datetime = explode(' ', $row['diary_date']);
          $date = $datetime[0];
          $time = $datetime[1];
          if($date == Date('Y-m-d')){
            $row['diary_date'] = $time;
          }
          else{
            $row['diary_date'] = $date;
      
    ?>
      <tr>
        <a href="/capstone/diary_view.php?no=<?php echo $row['diary_num']?>">
          <td class="no"><?php echo $row['diary_num']?></td> 
          <td class="title"><?php echo $row['diary_write']?></td>
          <td class="date"><?php echo $row['diary_date']?></td>
        </a>
      </tr>
    </tbody>
    <?php  
          }
        }
    ?>
      <li>
        <div id="divPaging">
           <?php echo $paging ?>
        </div>
      </li>
      <div class="btn_dr">
        <button type="botton" onclick="location.href='./diary_write.html'">작성</button>
      </div>
    </id>
  </table>
</body>
</html>