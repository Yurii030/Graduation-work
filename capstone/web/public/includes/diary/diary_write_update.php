<?
  include 'db.php';

  $child_uid = $_POST['diary_child_uid'];
  $sen = $_POST['sentence'];

  $sql = "INSERT INTO sentence (s_c_uid, sentence) VALUES ('$child_uid', '$sen')";
  $result = mysqli_query($conn, $sql);

  if($result){
    $msg = "정상적으로 글이 등록되었습니다.";
    echo "window.location.replace('/capstone/diary.php');</script>";
  } 
  else{ 
  $err = "글을 등록하지 못했습니다.";

	}
?>
