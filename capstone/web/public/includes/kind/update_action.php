<?php
  include 'db.php';

  $num = $_GET['num'];

  $child_name = $_POST['name'];
  $child_uid = $_POST['id'];
  $child_age = $_POST['age'];
  $child_class_id = $_POST['class'];

  $sql = "SELECT * FROM child WHERE child_num = '$num'";
  $result = mysqli_query($conn, $sql);
  $row = mysqli_fetch_assoc($result);

  if($child_name == ""){
    $sql = "UPDATE * FROM child set $child_name = 'child_name' WHERE child_num = '$num'";
    echo '<script> location.replace(\'/capstone/kind_inq.php\');</script>';
  }
  else if ($child_uid == "" ){
    $sql = "UPDATE * FROM child set $child_uid = 'child_uid' WHERE child_num = '$num'";
    echo '<script> location.replace(\'/capstone/kind_inq.php\');</script>';
  }
  else if ($child_age == "" ){
    $sql = "UPDATE * FROM child set $child_age = 'child_age' WHERE child_num = '$num'";
    echo '<script> location.replace(\'/capstone/kind_inq.php\');</script>';
  }
  else if ( $child_class_id == ""){
    $sql = "UPDATE * FROM child set $child_class_id = 'child_class_id' WHERE child_num = '$num'";
    echo '<script> location.replace(\'/capstone/kind_inq.php\');</script>';
  }
?>