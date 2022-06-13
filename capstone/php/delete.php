<?php
  include 'db.php';
  include 'session.php';

  $id = $_SESSION['id'];

  $sql = "DELETE FROM teacher WHERE t_uid = '$id'";
  $result = mysqli_query($conn, $sql);

  unset($_SESSION["id"]);
  unset($_SESSION["name"]);

  mysqli_close($conn);

  echo "<script>alert(\"정상처리 되었습니다.\");
  location.href = \"/capstone/index.php\";</script>";
?>