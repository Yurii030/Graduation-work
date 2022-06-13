<?php
    session_start();
    session_destroy();
    echo "<script>window.location.replace('/capstone/login.php');</script>"
?>