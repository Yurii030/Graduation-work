<?php
  session_start(); 
  include 'db.php';

  $name = $_POST['name'];
  $pw = $_POST['pw'];
  $pw_re = $_POST['pw_re'];
  $phone_num = $_POST['phone_num'];
  $email = $_POST['email'];

  $userid = $_SESSION['id'];

  $sql = "SELECT * FROM teacher WHERE t_uid = '$userid'";
  $result = mysqli_query($conn, $sql);
  $row = mysqli_fetch_assoc($result);

  if ($pw != $pw_re) {
    echo "<script>alert('비밀번호가 맞지 않습니다.')</script>";
    echo "<script>location.replace('/capstone/index.php');</script>";
    exit;
  }
  else{
    echo "<script>alert('비밀번호가 일치합니다.')</script>";
    $sql = "UPDATE teacher set t_name = '$name', t_pw = '$pw', t_phone = '$phone_num', t_email = '$email' WHERE t_uid = '$userid'";
    $result = mysqli_query($conn, $sql);
    echo "<script>location.replace('/capstone/my_info.php');</script>";
    exit;
  }
?>