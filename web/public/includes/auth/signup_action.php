<?php
  include 'db.php';

  $name = $_POST['name'];
  $id = $_POST['id'];
  $pw = $_POST['pw'];
  $phone_num = $_POST['phone_num'];
  $email = $_POST['email'];

  $sql = "INSERT INTO teacher(t_name, t_uid, t_pw, t_phone, t_email) VALUES ('$name', '$id', '$pw', '$phone_num', '$email')";

  if($name == "" || $id == "" || $pw == "" || $phone_num == "" || $email == "") {
    echo '<script> alter("비어있는 항목이 있습니다");</script>';
    echo '<script> history.back();</script>';
  }
  else {
    mysqli_query($conn, $sql);
    echo '<script> alter("회원 가입 되었습니다.");</script>';
    echo '<script> location.replace(\'/capstone/login.php\');</script>';
  }
?>