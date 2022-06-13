<?php
  include 'db.php';

  $num = $_GET['num'];
  
  $sql = "DELETE FROM child WHERE child_num = '$num'";
  $result = mysqli_query($conn, $sql);
  $row = mysqli_fetch_assoc($result);

  //echo "<script>alert(\"정상처리 되었습니다.\");
  //location.href = \"index.php\";</script>";
?>