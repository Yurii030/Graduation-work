<?php

  include 'db.php';

  $userid = $_POST['id'];
  $userpw = $_POST['pw'];

  $sql = "SELECT * FROM teacher WHERE t_uid = '$userid' AND t_pw = '$userpw'";
  $result = mysqli_query($conn, $sql);
  $row = mysqli_fetch_assoc($result);

  if($row){
    session_start();
    $_SESSION['id'] = $row['t_uid'];
    $_SESSION['name'] = $row['t_name'];
    echo "<script>alert('로그인에 성공했습니다!');";
    echo "window.location.replace('/capstone/index.php');</script>";
    exit;
  }else{
    echo "<script>alert('아이디 혹은 비밀번호가 잘못되었습니다.');";
    //echo "window.location.replace('/capstone/login.php');</script>";
  }
?>