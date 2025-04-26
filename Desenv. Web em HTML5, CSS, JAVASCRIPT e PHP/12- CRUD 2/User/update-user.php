<?php
require_once("../Service/Database.php");

$db = new Database();

$id = $_GET['id'];
$name = $_GET['name'];
$email = $_GET['email'];
$password = $_GET['password'];

//var_dump($_GET);
try {

  $sql = "update user set name='$name', email='$email',
              password='$password'
              where id = '$id'
              ";
//echo "$sql";
  
 $db->exec($sql);
  
 echo "<script>
  window.location.replace('list-user.php');
  </script>";
  
}catch(PDOException $e ) {
  var_dump($e->getMessage());
}


