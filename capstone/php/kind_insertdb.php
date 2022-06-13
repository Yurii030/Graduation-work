<?php
  include 'db.php';

  $name = $_POST['name'];
  $num = $_POST['number'];
  $age = $_POST['age'];
  $birth = $_POST['birth'];
  $class = $_POST['class'];

  $sql = "INSERT INTO child(child_uid, child_name, child_age, child_birth, child_class_id) VALUES ('$num', '$name', '$age', '$birth', '$class')";

  if($num == "" || $name == "" || $age == "" || $birth == "" || $class == "" ) {
    echo '<script> alter("비어있는 항목이 있습니다");</script>';
    
  }
  else {
    mysqli_query($conn, $sql);
    echo '<script> alter("원아 등록 되었습니다.");</script>';
    echo '<script> location.replace(\'/capstone/kind_inq.php\');</script>';
  }
?>