<?php
include "config.php";
$id = $_GET['ID'];
mysqli_query($con, "DELETE FROM 'tblodo' WHERE Id = $id");
header("location:index.php");

?>