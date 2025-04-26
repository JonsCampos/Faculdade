<?php
require_once("../Service/Database.php");

$db = new Database();

$name = $_GET['name'];
$email = $_GET['email'];
$password = $_GET['password'];

//var_dump($_GET);
try {

  // SQL 
  $res = $db->exec(
    "CREATE TABLE IF NOT EXISTS user (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      email TEXT, 
      password TEXT,
      name TEXT
    )"
  );

  $sql = "INSERT INTO user (name, email, password) 
          VALUES ('$name', '$email', '$password')";

 $db->exec($sql);
  
  echo "<script>
  window.location.replace('list-user.php');
  </script>";
  
}catch(PDOException $e ) {
  var_dump($e->getMessage());
}


